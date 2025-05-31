const API_BASE_URL = "https://plagrification-backend.onrender.com"; // Replace with backend Render URL

// Example usage
export const loginUser = async (credentials) => {
  const res = await fetch(`${API_BASE_URL}/api/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(credentials),
    credentials: "include",
  });
  return res.json();
};
