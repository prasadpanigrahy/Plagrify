import mongoose from "mongoose";

const fileSchema = new mongoose.Schema({
  user: { type: mongoose.Schema.Types.ObjectId, ref: "User" },
  filename: String,
  similarityScore: Number,
  createdAt: { type: Date, default: Date.now },
});

export default mongoose.model("File", fileSchema);
