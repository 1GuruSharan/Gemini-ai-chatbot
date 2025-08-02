const axios = require("axios");

// Secure API Key (Use environment variables in production)
const API_KEY = "AIzaSyD_y7b-knG9NGvXepm3Kp8NerUuquOflW0";
const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${API_KEY}`;

const requestData = {
  contents: [
    { parts: [{ text: "Generate a JavaScript function to sort an array." }] }
  ],
};

axios.post(url, requestData)
  .then(response => console.log(response.data))
  .catch(error => console.error("Error:", error));
