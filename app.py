from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"

def chat_with_ollama(prompt, task):
    """
    Sends the prompt to Ollama API for processing.
    """
    if task == "bugs":
        formatted_prompt = (
            "Your task is to identify and correct **only syntax and logic errors** in the following code.\n"
            "**Strict Rules:**\n"
            "- **DO NOT** change any words, variable names, function names, or strings.\n"
            "- **DO NOT** replace or 'correct' user-defined text. If a string is 'ho', it must remain 'ho'.\n"
            "- **DO NOT** reword print statements or modify messages in any way.\n"
            "- **DO NOT** introduce synonyms or alternative spellings.\n"
            "- Fix **only syntax issues** (e.g., missing brackets, incorrect indentation, misplaced symbols).\n"
            "- Fix **only clear logical errors** (e.g., undefined variables, incorrect function calls, missing return statements).\n"
            "- **Do NOT optimize or improve the code beyond fixing errors.**\n"
            "\n**Example:**\n"
            "🔴 **Incorrect Fix:** `print('ho')` → `print('hello')` 🚫 **WRONG! DO NOT CHANGE!**\n"
            "✅ **Correct Fix:** `print('ho')` → `print('ho')` (if missing a closing quote)\n"
            "\n**Return the corrected code with explanations.**\n\n"
            "**Code:**\n```python\n" + prompt + "\n```\n"
        )
    else:
         formatted_prompt = (
            "Your task is to optimize the following code **only for time and space complexity** without changing its behavior.\n"
            "**Strict Rules:**\n"
            "- **DO NOT** change any functionality, variable names, function names, or string outputs.\n"
            "- **DO NOT** alter print messages, return values, or expected outputs.\n"
            "- **DO NOT** add unnecessary changes—modify only where efficiency can be improved.\n"
            "- **DO NOT** introduce new libraries unless explicitly required for optimization.\n"
            "- Optimize loops, recursion, and data structures where necessary.\n"
            "- Remove redundant computations or unnecessary memory usage.\n"
            "\n**Example:**\n"
            "🔴 **Incorrect Optimization:** `print('Processing...')` → `print('Working...')` 🚫 **WRONG! DO NOT CHANGE TEXT!**\n"
            "✅ **Correct Optimization:** Using set for faster lookup instead of looping through a list.\n"
            "\n**Return the optimized code with explanations.**\n\n"
            "**Code:**\n```python\n" + prompt + "\n```\n"
        )


    payload = {
        "model": "llama3.2:7b",
        "prompt": formatted_prompt,
        "stream": False,
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "Error processing request")

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/bug_fixing", methods=["GET", "POST"])
def bug_fixing():
    corrected_code = ""
    if request.method == "POST":
        user_code = request.form.get("code")
        if user_code:
            corrected_code = chat_with_ollama(user_code, "bugs")
    return render_template("bug_fixing.html", corrected_code=corrected_code)

@app.route("/code_optimization", methods=["GET", "POST"])
def code_optimization():
    corrected_code = ""
    if request.method == "POST":
        user_code = request.form.get("code")
        if user_code:
            corrected_code = chat_with_ollama(user_code, "optimize")
    return render_template("code_optimization.html", corrected_code=corrected_code)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/methodology")
def methodology():
    return render_template("methodology.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=1234)
