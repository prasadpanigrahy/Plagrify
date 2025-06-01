from flask import Flask

app = Flask(__name__)

@app.before_first_request
def foo():
    print("First request!")

if __name__ == '__main__':
    app.run(debug=True)
