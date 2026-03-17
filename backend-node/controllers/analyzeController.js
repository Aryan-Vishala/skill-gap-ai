const mlService = require("../services/mlService");
const fs = require("fs");
const axios = require("axios");

exports.analyzeResume = async (req, res) => {

  try {

    const filePath = req.file.path;
    const jobDescription = req.body.job_description;
    const githubUsername = req.body.github_username;

    let githubSkills = "";

    // 🔹 Fetch GitHub skills if username provided
    if (githubUsername) {

      const githubRes = await axios.get(
        `http://localhost:5000/api/github/${githubUsername}`
      );

      githubSkills = githubRes.data.skillsText;
    }

    // 🔹 Combine job + GitHub
    const finalJobText = jobDescription + " " + githubSkills;

    const result = await mlService.analyze(filePath, finalJobText);

    fs.unlinkSync(filePath);

    res.json({
      ...result,
      github_skills: githubSkills
    });

  } catch (error) {

    console.error("Error:", error.message);

    res.status(500).json({
      error: "Analysis failed"
    });

  }

};