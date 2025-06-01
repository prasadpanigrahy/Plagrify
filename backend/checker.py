from flask import Blueprint, render_template, request, session, redirect, send_file, abort
import os
from models import Upload, User
from database import db
from difflib import SequenceMatcher
from datetime import datetime
from werkzeug.utils import secure_filename
import io
from fpdf import FPDF  # Ensure fpdf is installed: pip install fpdf

checker_bp = Blueprint('checker', __name__)
UPLOAD_FOLDER = 'backend/uploads'

@checker_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')
    scores = []
    error = None
    success_message = None

    if request.method == 'POST':
        files = request.files.getlist('files')
        
        if len(files) != 2:
            error = "Please upload exactly two files."
            return render_template('dashboard.html', error=error)
        
        contents = []
        try:
            for file in files:
                filename = secure_filename(file.filename)
                content = file.read()  # Read bytes
                
                # Save file
                path = os.path.join(UPLOAD_FOLDER, filename)
                file.seek(0)  # reset stream position to start before saving
                file.save(path)

                # Try decode to text for similarity, fallback to empty string if fails
                try:
                    text = content.decode('utf-8', errors='ignore')
                except Exception:
                    text = ""

                contents.append((filename, text))
            
            # Calculate similarity between two files only
            sim = SequenceMatcher(None, contents[0][1], contents[1][1]).ratio()
            scores.append((f"{contents[0][0]} vs {contents[1][0]}", sim))

            # Store upload history with the similarity score
            for fname, _ in contents:
                upload = Upload(user_id=session['user_id'], filename=fname,
                                similarity_score=sim,
                                created_at=datetime.now())
                db.session.add(upload)
            db.session.commit()
            
            success_message = "Files processed successfully!"
        except Exception as e:
            error = f"An error occurred: {str(e)}"
    
    return render_template('dashboard.html', scores=scores, error=error, success_message=success_message)


@checker_bp.route('/history')
def history():
    if 'user_id' not in session:
        return redirect('/login')
    uploads = Upload.query.filter_by(user_id=session['user_id']).all()
    return render_template('history.html', uploads=uploads)


@checker_bp.route('/download_report/<int:upload_id>/<format>')
def download_report(upload_id, format):
    upload = Upload.query.get_or_404(upload_id)
    
    report_text = (
        f"Filename: {upload.filename}\n"
        f"Similarity Score: {(upload.similarity_score * 100):.2f}%\n"
        f"Compared On: {upload.created_at.strftime('%Y-%m-%d %H:%M')}"
    )
    
    if format == 'txt':
        return send_file(
            io.BytesIO(report_text.encode('utf-8')),
            mimetype='text/plain',
            as_attachment=True,
            download_name=f"plagiarism_report_{upload.id}.txt"
        )
    elif format == 'pdf':
        from fpdf import FPDF
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for line in report_text.split('\n'):
            pdf.cell(200, 10, txt=line, ln=True)
        
        pdf_bytes = pdf.output(dest='S').encode('latin1')  # get PDF as string, encode to bytes
        pdf_output = io.BytesIO(pdf_bytes)
        pdf_output.seek(0)
        
        return send_file(
            pdf_output,
            mimetype='application/pdf',
            as_attachment=True,
            download_name=f"plagiarism_report_{upload.id}.pdf"
        )
    else:
        abort(400, 'Unsupported format')