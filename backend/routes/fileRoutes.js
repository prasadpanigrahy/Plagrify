import express from "express";
import { uploadFile, getUserFiles } from "../controllers/fileController.js";
const router = express.Router();

router.post("/upload", uploadFile);
router.get("/", getUserFiles);

export default router;
