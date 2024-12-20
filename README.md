
# GGUF Model WebApp

This project is a lightweight web application that uses a [GGUF](https://github.com/ggerganov/llama.cpp) language model to transform journalistic or opinionated text into objective, fact-based writing. It leverages `llama.cpp` for efficient local inference and serves the functionality via a Flask web server.

## Features

- Processes text using GGUF models for local inference.
- Transforms opinionated or subjective content into a more neutral, factual format.
- User-friendly web interface with real-time results.
- Flask backend and HTML/JavaScript frontend.

---

## Prerequisites

Before starting, ensure you have the following:

1. **`llama.cpp`**: Clone and build the llama.cpp repository:
   ```bash
   git clone https://github.com/ggerganov/llama.cpp.git
   cd llama.cpp
   make
   ```

2. **GGUF Model**: Download a compatible GGUF model (e.g., LLaMA 2) from [Hugging Face](https://huggingface.co/) or other sources and place it in a known directory.

3. **Python**: Install Python (>=3.8) and `pip`.

4. **Dependencies**: Install the required Python packages:
   ```bash
   pip install flask flask-cors
   ```

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/gguf-webapp.git
   cd gguf-webapp
   ```

2. **Configure Paths**:
   - Edit `app.py` to specify the paths to your GGUF model and the `llama.cpp` executable:
     ```python
     LLAMA_EXECUTABLE = "/path/to/llama.cpp/main"
     GGUF_MODEL = "/path/to/your/model.gguf"
     ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

4. **Access the Web Interface**:
   Open your browser and navigate to [http://localhost:5000](http://localhost:5000).

---

## Usage

### Input
1. Enter text in the text area on the web page.
2. Click "Process Text."

### Output
- The application will process the input using the GGUF model and display the transformed, objective version.

---

## Project Structure

```
gguf-webapp/
├── app.py                # Flask backend for processing requests
├── public/               # Static files served by Flask
│   ├── index.html        # Frontend for user interaction
├── README.md             # Project documentation
```

---

## Customization

1. **Modify the Prompt**:
   - Adjust the prompt in `app.py` to suit your specific use case:
     ```python
     base_prompt = """You are an expert editor and linguistic analyst..."""
     ```

2. **Add Frontend Features**:
   - Enhance the `index.html` to include options for model selection, advanced settings, or styling updates.

---

## Packaging as an Executable

To package the project into a standalone executable:

1. Install `PyInstaller`:
   ```bash
   pip install pyinstaller
   ```

2. Build the `.exe`:
   ```bash
   pyinstaller --onefile app.py
   ```

3. The generated `.exe` will be located in the `dist` folder.

---

## Troubleshooting

- **Issue: `llama.cpp` fails to run**
  - Ensure the paths in `app.py` point to valid GGUF model and `llama.cpp` executable locations.
  - Verify that `llama.cpp` runs correctly by testing it from the terminal:
    ```bash
    ./main -m /path/to/your/model.gguf -p "Test prompt"
    ```

- **Issue: Python error on startup**
  - Confirm all dependencies are installed:
    ```bash
    pip install flask flask-cors
    ```

- **Issue: Output is incomplete or malformed**
  - Check that your GGUF model supports the text input length and language used.

---

## Credits

- **`llama.cpp`**: Lightweight inference engine for LLaMA models ([GitHub](https://github.com/ggerganov/llama.cpp)).
- **GGUF Models**: Open-access language models optimized for CPU/GPU inference.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

### **How to Use This README**
1. Replace the placeholder text (e.g., `/path/to/your/model.gguf`).
2. Add your repository URL in the cloning section.
3. Include links to your GitHub profile or project details in the credits if applicable.

This README is comprehensive and provides users with everything they need to run, customize, and troubleshoot the project.
