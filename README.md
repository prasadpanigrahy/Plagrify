# Plagrification - Web-based Plagiarism Checker

Plagrification is a full-stack web application that allows users to upload documents and receive a similarity score. An admin can view all user activity and ban/remove users if necessary.

---

## 🌐 Tech Stack

- **Frontend:** React (Vite)
- **Backend:** Node.js, Express
- **Database:** MongoDB (Atlas)
- **Authentication:** JWT

---

## 🧾 Features

- User registration and login
- Upload documents and receive similarity scores
- Track upload history
- Admin dashboard to manage users and files

---

## 📁 Project Structure

```
plagrification/
├── backend/
│   ├── models/          # Mongoose schemas
│   ├── routes/          # API route handlers
│   ├── middlewares/     # Auth middleware
│   ├── uploads/         # File uploads
│   └── server.js        # Main Express server
└── frontend/
    └── src/
        ├── pages/       # React pages
        ├── App.jsx
        └── main.jsx
```

---

## 🛠️ Setup Instructions

### 🔧 Prerequisites

- Node.js & npm
- MongoDB Atlas account
- Render account (for deployment)

### 🔑 Environment Variables

Create `backend/.env`:

```env
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_jwt_secret
```

### ▶️ Run Locally

```bash
# Backend
cd backend
npm install
node server.js

# Frontend
cd frontend
npm install
npm run dev
```

---

## 🚀 Deployment on Render

### 1. **MongoDB Atlas**

- Create a free cluster at [mongodb.com/cloud](https://www.mongodb.com/cloud)
- Whitelist your IP & get the connection URI

### 2. **Deploy Backend**

- Go to [Render](https://render.com) → New Web Service
- Connect your repo, select `backend/` folder
- Set:
  - **Build Command:** `npm install`
  - **Start Command:** `node server.js`
  - Add environment variables: `MONGO_URI`, `JWT_SECRET`

### 3. **Deploy Frontend**

- On Render → New Static Site
- Point to `frontend/`
- Set:
  - **Build Command:** `npm run build`
  - **Publish Directory:** `dist`

---

## 🔧 Vite Proxy for Local Dev

Create `frontend/vite.config.js`:

```js
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/api": {
        target: "http://localhost:5000",
        changeOrigin: true,
        secure: false,
      },
    },
  },
});
```

---

## ✨ Future Improvements

- Add real NLP-based similarity comparison (e.g., cosine similarity)
- File type validation (PDF, DOCX support)
- User profile management

---

## 🧑‍💻 Author

Made with 💡 by Prasad Panigrahy
