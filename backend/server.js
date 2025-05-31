import express from "express";
import dotenv from "dotenv";
import mongoose from "mongoose";
import cors from "cors";
import authRoutes from "./routes/authRoutes.js";
import fileRoutes from "./routes/fileRoutes.js";
import adminRoutes from "./routes/adminRoutes.js";
import { authenticateUser } from "./middlewares/authMiddleware.js";
import fileUpload from "express-fileupload";

dotenv.config();
const app = express();
const PORT = process.env.PORT || 5000;

// ✅ CORS Setup
app.use(
  cors({
    origin: "https://plagrification-frontend.onrender.com", // ⬅️ Frontend URL
    credentials: true,
  })
);

app.use(express.json());
app.use(fileUpload());
app.use("/uploads", express.static("uploads"));

// Routes
app.use("/api/auth", authRoutes);
app.use("/api/files", authenticateUser, fileRoutes);
app.use("/api/admin", authenticateUser, adminRoutes);

// MongoDB
mongoose
  .connect(process.env.MONGO_URI)
  .then(() => app.listen(PORT, () => console.log(`Server running on ${PORT}`)))
  .catch((err) => console.log(err));
