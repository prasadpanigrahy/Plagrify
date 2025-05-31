import File from "../models/File.js";
import fs from "fs";
import path from "path";

function getSimilarity(content1, content2) {
  const words1 = content1.split(/\W+/);
  const words2 = content2.split(/\W+/);
  const common = words1.filter((word) => words2.includes(word)).length;
  return (common / Math.max(words1.length, words2.length)) * 100;
}

export const uploadFile = async (req, res) => {
  const file = req.files.file;
  const filepath = `uploads/${Date.now()}-${file.name}`;
  file.mv(filepath, async (err) => {
    if (err) return res.status(500).send(err);

    const content = fs.readFileSync(filepath, "utf-8");
    const files = await File.find();
    let maxSim = 0;

    for (const f of files) {
      const oldContent = fs.readFileSync(`uploads/${f.filename}`, "utf-8");
      maxSim = Math.max(maxSim, getSimilarity(content, oldContent));
    }

    const newFile = await File.create({
      user: req.user._id,
      filename: path.basename(filepath),
      similarityScore: maxSim,
    });

    res.json({ similarity: maxSim, file: newFile });
  });
};

export const getUserFiles = async (req, res) => {
  const files = await File.find({ user: req.user._id });
  res.json(files);
};
