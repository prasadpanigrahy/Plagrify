import React, { useEffect, useState } from "react";
import axios from "axios";

const AdminPanel = () => {
  const [users, setUsers] = useState([]);
  const [files, setFiles] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const headers = {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      };
      const [userRes, fileRes] = await Promise.all([
        axios.get("/api/admin/users", { headers }),
        axios.get("/api/admin/files", { headers }),
      ]);
      setUsers(userRes.data);
      setFiles(fileRes.data);
    };
    fetchData();
  }, []);

  const banUser = async (id) => {
    await axios.put(
      `/api/admin/ban/${id}`,
      {},
      {
        headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
      }
    );
    setUsers(users.map((u) => (u._id === id ? { ...u, isBanned: true } : u)));
  };

  return (
    <div>
      <h2>Admin Panel</h2>
      <h3>Users</h3>
      <ul>
        {users.map((user) => (
          <li key={user._id}>
            {user.email} ({user.role}) - {user.isBanned ? "Banned" : "Active"}
            {!user.isBanned && (
              <button onClick={() => banUser(user._id)}>Ban</button>
            )}
          </li>
        ))}
      </ul>
      <h3>Files</h3>
      <ul>
        {files.map((file) => (
          <li key={file._id}>
            {file.filename} - {file.similarityScore.toFixed(2)}% (by{" "}
            {file.user.email})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AdminPanel;
