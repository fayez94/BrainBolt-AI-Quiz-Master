## 🌟 BrainBolt - AI Quiz Master
BrainBolt is an AI-powered Multiple Choice Question (MCQ) generator built using LangChain and OpenAI's GPT model. This tool processes text input (from PDF or TXT files), generates MCQs, evaluates their complexity, and formats them for easy readability. The project is developed with Streamlit for an interactive UI.  

## 🚀 Features

1. **MCQ Generation:** Creates structured multiple-choice questions from input text.  

2. **AI-Powered Evaluation:** Reviews question complexity and adjusts tone accordingly.  

3. **PDF/TXT Support:** Extracts text from PDF and TXT files.  

4. **Logging System:** Tracks process execution and errors.  

5. **Streamlit UI:** User-friendly interface for easy interaction.  

## 📂 Folder Structure
```
BrainBolt/
│── Input for inference/      # Folder for input text/PDF files
│── experiment/               # Contains Jupyter notebooks for testing
│   └── openMCQ.ipynb         # Defines MCQ templates and calls LangChain model
│── mcqgenerator.egg-info/    # Package metadata
│── src/                      # Source code folder
│   ├── experiment/
│   │   └── logger.py         # Logs execution details
│   ├── mcqgenerator/
│   │   ├── MCQGenerator.py   # Core logic for generating and evaluating MCQs
│   │   ├── utils.py          # File handling and MCQ formatting utilities
│   │   ├── setup.py          # Package setup file
│── logs/                     # Stores execution logs
│── StreamlitAPP.py           # Streamlit-based UI for user interaction
│── README.md                 # Project documentation
│── requirements.txt          # Dependencies list
│── Response.json             # Sample output data
│── test.py                   # Testing script
```

## 🛠 Installation  
Clone the repository and install dependencies:
```  
git clone https://github.com/fayez94/BrainBolt-AI-Quiz-Master.git
cd BrainBolt-AI-Quiz-Master
pip install -r requirements.txt
```

## 📌 Usage  
Run Streamlit UI:
```  
streamlit run StreamlitAPP.py
```

Use MCQ Generator Directly:  
```
from src.mcqgenerator.MCQGenerator import generate_and_evaluate_quiz

input_data = {
    "text": "Sample text for quiz generation.",
    "number": 5,
    "subject": "Science",
    "tone": "formal",
    "response_json": "{}"
}
output = generate_and_evaluate_quiz(input_data)
print(output)
```

## 🔑 Key Components  
📝 MCQGenerator.py  
* Generates and evaluates MCQs using LangChain & OpenAI GPT.  
* Uses SequentialChain for structured MCQ generation & evaluation.  
* Implements logging for error handling.  

📂 utils.py  
* read_file(file): Extracts text from PDF/TXT files.  
* get_table_data(quiz_str): Converts MCQ JSON output into a table format.  

📜 logger.py  
* Creates timestamped logs in the logs/ folder.  
* Helps debug and track execution details.  