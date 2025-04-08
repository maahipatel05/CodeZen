# 🚀 Smart Code Assistant

Smart Code Assistant is a final year project developed to assist developers in writing cleaner, bug-free, and optimized code using the power of AI. It leverages the Llama 3.2:7B model via Ollama, backed by a Flask API, and features a sleek, user-friendly frontend.

---

## 🔍 Features

- 🔎 Detects and corrects bugs in code
- ⚡ Optimizes code for time and space complexity
- 🧠 Powered by Llama 3.2:7B model (local inference)
- 🖥️ Simple and responsive frontend interface
- 🐳 Dockerized for easy deployment
- 🔄 CI/CD integration via GitHub Actions

---

## 🧱 Technology Stack

- **Model**: Llama 3.2:7B via Ollama
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **CI/CD**: GitHub Actions
- **Containerization**: Docker + Docker Hub

---

## 🔁 Project Flow

1. **User selects an operation**:
   - `Find Bugs`
   - `Optimize Code`

2. **Code is submitted** via the frontend

3. Flask backend forms a dynamic prompt:
   - If "Find Bugs": `"Find bugs in this code and give the correct version."`
   - If "Optimize Code": `"Optimize the given code for best time and space complexity."`

4. The prompt is passed to the **Llama 3.2:7B** model via Ollama server

5. Response is received and displayed in the UI

---

## 📦 Docker Setup

```bash
# Build Docker Image
docker build -t codezen .

# Run the container
docker run -p 1234:1234 codezen
