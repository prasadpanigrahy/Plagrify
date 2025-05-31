import React, { useEffect, useState } from "react";
import axios from "axios";

const HistoryPage = () => {
  const [records, setRecords] = useState([]);

  useEffect(() => {
    const fetchHistory = async () => {
      const res = await axios.get("/api/files", {
        headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
      });
      setRecords(res.data);
    };
    fetchHistory();
  }, []);

  return (
    <div>
      <h2>Your History</h2>
      <ul>
        {records.map((record) => (
          <li key={record._id}>
            {record.filename} - {record.similarityScore.toFixed(2)}%
          </li>
        ))}
      </ul>
    </div>
  );
};

export default HistoryPage;
