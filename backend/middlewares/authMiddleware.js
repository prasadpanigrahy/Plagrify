import jwt from "jsonwebtoken";
import User from "../models/User.js";

export const authenticateUser = async (req, res, next) => {
  const token = req.headers.authorization?.split(" ")[1];
  if (!token) return res.status(401).json({ msg: "Access denied" });

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    const user = await User.findById(decoded.id);
    if (!user || user.isBanned)
      return res.status(403).json({ msg: "Banned or invalid" });
    req.user = user;
    next();
  } catch (err) {
    res.status(401).json({ msg: "Invalid token" });
  }
};

export const requireAdmin = (req, res, next) => {
  if (req.user.role !== "admin")
    return res.status(403).json({ msg: "Admins only" });
  next();
};
