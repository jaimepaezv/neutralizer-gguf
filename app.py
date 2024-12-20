
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import subprocess

# Configuration
LLAMA_EXECUTABLE = "/path/to/llama.cpp/main"  # Path to the llama.cpp executable
GGUF_MODEL = "/path/to/your/model.gguf"       # Path to the GGUF model

# Flask app setup
app = Flask(__name__, static_folder="public")
CORS(app)

# Prompt template
base_prompt = """You are an expert editor and linguistic analyst. Your goal is to take a piece of journalistic or opinionated text and transform it into a more objective, neutral, and fact-based version. Specifically, do the following:

1. Remove or rephrase subjective, emotional, or sensational adjectives and adverbs.
2. Eliminate or refine phrases that suggest certainty, widespread knowledge, or bias without evidence.
3. Avoid diminishing the factual core. Do not remove essential information; instead, reshape it to make it more neutral.
4. Maintain logical flow and coherence. Ensure each sentence connects properly and that the narrative is clear.
5. Present critical thought factually. Use neutral language and indicate sources when mentioned.

Below is the text. Transform it accordingly:

"""

# API to process text
@app.route("/process-text", methods=["POST"])
def process_text():
    try:
        data = request.json
        user_text = data.get("text", "")

        if not user_text:
            return jsonify({"error": "No text provided"}), 400

        # Construct the full prompt
        prompt = base_prompt + user_text

        # Execute llama.cpp with the model and prompt
        command = f'{LLAMA_EXECUTABLE} -m {GGUF_MODEL} -p "{prompt}"'
        result = subprocess.run(command, capture_output=True, text=True, shell=True)

        if result.returncode != 0:
            return jsonify({"error": "Error running the GGUF model"}), 500

        # Return the transformed text
        return jsonify({"transformedText": result.stdout.strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Serve the frontend
@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
