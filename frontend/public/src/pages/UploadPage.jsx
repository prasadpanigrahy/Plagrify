// src/pages/UploadPage.jsx
import React, { useState } from "react";
import axios from "axios";

const UploadPage = () => {
  const [file, setFile] = useState(null);
  const [similarity, setSimilarity] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);
    const res = await axios.post("/api/files/upload", formData, {
      headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
    });
    setSimilarity(res.data.similarity);
  };

  return (
    <div>
      <h2>Upload File</h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Check Similarity</button>
      {similarity !== null && <p>Similarity Score: {similarity.toFixed(2)}%</p>}
    </div>
  );
};

export default UploadPage;
