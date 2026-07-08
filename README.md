# 🤖 AI Code Reviewer

An AI-powered Code Reviewer that analyzes source code, detects syntax and logical errors, suggests optimizations, estimates time and space complexity, and generates improved code using a **locally hosted Large Language Model (LLM)**.

The application is built using **Python**, **Streamlit**, **Ollama**, and **DeepSeek-Coder**, allowing completely offline AI-powered code analysis without relying on paid cloud APIs.

---

## 📌 Features

- 🔍 Detects syntax and logical errors
- 💡 Suggests code improvements and best practices
- ⚡ Recommends code optimizations
- 📊 Estimates time and space complexity
- ✨ Generates refactored code
- 🌐 Supports multiple programming languages
- 🔒 Works completely offline using Ollama
- 🎨 Interactive and user-friendly Streamlit interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Ollama
- DeepSeek-Coder LLM
- Requests Library
- Scikit-learn
- Git & GitHub

---

## 📂 Project Structure

```
ai-code-reviewer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── reviewer.py
│   └── prompt_template.py
│
├── evaluation/
│   ├── evaluate.py
│   └── test_dataset.json
│
└── .gitignore
```

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-code-reviewer.git
cd ai-code-reviewer
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Download Ollama from:

https://ollama.com/download

Verify installation

```bash
ollama --version
```

---

## 5. Download the DeepSeek Model

```bash
ollama pull deepseek-coder
```

---

## 6. Run the Application

```bash
python -m streamlit run app.py
```

Open your browser and visit

```
http://localhost:8501
```

---

# 🧠 How It Works

1. User pastes source code into the application.
2. User selects the programming language.
3. A structured prompt is generated.
4. The prompt is sent to DeepSeek-Coder through Ollama.
5. The AI analyzes the submitted code.
6. The review is displayed, including:
   - Syntax and logical errors
   - Improvement suggestions
   - Optimization recommendations
   - Time and space complexity
   - Refactored code

---

# 📊 Performance Evaluation

The AI Code Reviewer was evaluated using a manually curated benchmark dataset consisting of **100 code snippets** containing both correct implementations and intentionally buggy programs across multiple programming languages.

### Evaluation Metrics

| Metric | Result |
|---------|--------|
| **Dataset Size** | **100 Programs** |
| **Accuracy** | **45.00%** |
| **Precision** | **47.37%** |
| **Recall** | **90.00%** |
| **F1-Score** | **62.07%** |

### Interpretation

- Successfully detected **90% of buggy programs** in the evaluation dataset.
- Demonstrated strong bug detection capability with high recall.
- Lower precision indicates that some correct programs were incorrectly classified as buggy (false positives).
- Future improvements include refining prompts, expanding the benchmark dataset, and improving structured output parsing to reduce false positives.

---

# 📈 Benchmark Dataset

The evaluation dataset contains examples of:

- Syntax Errors
- Logical Errors
- Runtime Errors
- Missing Semicolons
- Missing Colons
- Incorrect Comparisons (`=` vs `==`)
- Infinite Loops
- Array Index Errors
- Missing Return Statements
- Correct Programs

Supported languages include:

- Python
- C
- C++
- Java

---

# 🚀 Future Enhancements

- 📂 Source code file upload
- 📁 Batch code review
- ⭐ Code quality score
- 📄 PDF review report generation
- 🔗 GitHub repository integration
- 📊 Analytics dashboard
- 🌍 Cloud deployment
- 🤖 Multi-model LLM support

---

# 💼 Resume Highlights

- Developed an AI-powered Code Reviewer using **Python**, **Streamlit**, **Ollama**, and **DeepSeek-Coder**.
- Integrated a locally hosted Large Language Model for offline code analysis.
- Implemented automated detection of syntax and logical errors with optimization recommendations.
- Designed a modular architecture using REST API communication with Ollama.
- Built an evaluation pipeline using **Scikit-learn** to measure Accuracy, Precision, Recall, and F1-Score on a benchmark dataset of 100 programs.

---

# 📸 Screenshots

## Home Page

_Add screenshot here_

---

## Code Review Output

_Add screenshot here_

---

## Performance Evaluation

_Add screenshot here_

---

# 👨‍💻 Author

**Maanya K**

Bachelor of Engineering (Artificial Intelligence & Data Science)

M. S. Ramaiah Institute of Technology



# 📄 License

This project is licensed for educational and portfolio purposes.

---

⭐ If you found this project useful, consider giving it a star on GitHub!
