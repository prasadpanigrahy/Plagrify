import express from "express";
import {
  getAllUsers,
  banUser,
  getAllFiles,
} from "../controllers/adminController.js";
import { requireAdmin } from "../middlewares/authMiddleware.js";

const router = express.Router();
router.use(requireAdmin);

router.get("/users", getAllUsers);
router.put("/ban/:id", banUser);
router.get("/files", getAllFiles);

export default router;
