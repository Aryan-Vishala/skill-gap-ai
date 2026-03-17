const axios = require("axios");
const fs = require("fs");
const FormData = require("form-data");

exports.analyze = async (filePath, jobDescription) => {

  const formData = new FormData();

  formData.append("file", fs.createReadStream(filePath));
  formData.append("job_description", jobDescription);

  const response = await axios.post(
    "http://127.0.0.1:8000/analyze-resume",
    formData,
    {
      headers: formData.getHeaders()
    }
  );

  return response.data;
};