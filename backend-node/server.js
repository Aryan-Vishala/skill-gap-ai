const express = require("express");
const cors = require("cors");
const analyzeRoute = require("./routes/analyze");
const githubRoute = require("./routes/github");

const app = express();

app.use(cors());
app.use(express.json());

app.get("/", (req, res) => {
  res.send("Developer Skill Gap Analyzer Backend Running");
});

app.use("/api/analyze", analyzeRoute);
app.use("/api/github", githubRoute);


const PORT = 5000;

app.listen(PORT, () => {
  console.log(`Node server running on port ${PORT}`);
});