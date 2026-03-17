const express = require("express");
const multer = require("multer");
const analyzeController = require("../controllers/analyzeController");

const router = express.Router();

const upload = multer({ dest: "uploads/" });

router.post("/", upload.single("file"), analyzeController.analyzeResume);

module.exports = router;