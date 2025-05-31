import User from "../models/User.js";
import File from "../models/File.js";

export const getAllUsers = async (req, res) => {
  const users = await User.find();
  res.json(users);
};

export const banUser = async (req, res) => {
  const user = await User.findByIdAndUpdate(
    req.params.id,
    { isBanned: true },
    { new: true }
  );
  res.json(user);
};

export const getAllFiles = async (req, res) => {
  const files = await File.find().populate("user", "email name");
  res.json(files);
};
