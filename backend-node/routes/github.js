const express = require("express");
const axios = require("axios");
const skills = require("../skills");

const router = express.Router();

router.get("/:username", async (req, res) => {

  const username = req.params.username;

  try {

    const response = await axios.get(
      `https://api.github.com/users/${username}/repos`
    );

    const repos = response.data;

    let skillsSet = new Set();

    repos.forEach(repo => {

      // 1️⃣ Check language
      if (repo.language) {

        const lang = repo.language.toLowerCase();

        if (skills.includes(lang)) {
          skillsSet.add(lang);
        }
      }

      // 2️⃣ Check description
      if (repo.description) {

        const words = repo.description
          .toLowerCase()
          .replace(/[^a-zA-Z0-9 ]/g, "")
          .split(" ");

        words.forEach(word => {

          if (skills.includes(word)) {
            skillsSet.add(word);
          }

        });

      }

    });

    const skillsText = Array.from(skillsSet).join(" ");

    res.json({ skillsText });

  } catch (error) {

    console.error("GitHub error:", error.message);

    res.status(500).json({
      error: "GitHub fetch failed"
    });

  }

});

module.exports = router;