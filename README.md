# CodeZen

CodeZen is a small web app that uses a locally running LLaMA 3.2 (7B) model to help with two things every developer runs into constantly: finding bugs in code and making code run faster or use less memory. Jinay Shah and I built it together as our final year project.

The idea behind it was pretty simple. A lot of "AI code helper" tools will happily rewrite your code into something that technically works but barely resembles what you wrote, renamed variables, reworded strings, different structure entirely. That's not very useful if you're trying to actually learn from a mistake or keep your own style. So we set ourselves a constraint: the assistant should point out what's wrong and fix only that, nothing more.

## What it does

CodeZen has two modes.

**Find bugs.** Paste in code that isn't working and the model looks for syntax and logic errors only. It's instructed not to rename variables, "correct" your strings, or reword your print statements just because it thinks it knows better.

**Optimize code.** Paste in working code and the model suggests changes purely for time and space efficiency, things like swapping a list lookup for a set, removing redundant computation, tightening up a loop. The behavior and output of your code are expected to stay exactly the same.

Both modes run on prompts we wrote and rewrote a lot of times to get the model to actually respect those boundaries. That part of the project took longer than building the app itself.

## How it's built

- **Model:** LLaMA 3.2 (7B), run locally through Ollama
- **Backend:** Flask, which builds the prompt, sends it to Ollama, and returns the response to the page
- **Frontend:** plain HTML, CSS, and JavaScript, kept intentionally simple
- **Tests:** pytest, covering each route in the app
- **CI/CD:** a GitHub Actions pipeline that runs the test suite on every push, then builds and pushes a Docker image to Docker Hub
- **Containerization:** Docker

## Running it locally

You'll need Ollama installed and running, with the `llama3.2:7b` model pulled.

```bash
git clone https://github.com/maahipatel05/CodeZen.git
cd CodeZen
pip install -r requirements.txt
python app.py
```

The app will be available at `http://localhost:1234`.

## Running it with Docker

```bash
docker build -t codezen .
docker run -p 1234:1234 codezen
```

## Running the tests

```bash
pytest
```

## Project layout

```
CodeZen/
├── app.py                   Flask app and the Ollama integration
├── templates/               Pages: home, bug fixing, optimization, about, methodology, contact
├── static/                  CSS, JS, images
├── test_app.py              Route level tests
├── Dockerfile
└── .github/workflows/       CI/CD pipeline (test, build, push to Docker Hub)
```

## Built by

Maahi Patel and Jinay Shah, as our final year project.
