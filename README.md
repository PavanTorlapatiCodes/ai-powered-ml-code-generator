# AI-Powered Machine Learning Code Generator

An AI-powered application that helps users generate Python machine-learning code from uploaded datasets and natural-language prompts. Built using Python, Gradio, Gemini AI, and smolagents.

## Project Overview

The AI-Powered ML Code Generator allows users to upload a dataset, describe a machine-learning task, and receive a generated solution containing Python code and model output.

The application provides a simple web interface for experimenting with common machine-learning tasks without manually writing the entire workflow.

## Features

- Upload CSV and Excel datasets.
- Generate machine-learning code using natural-language prompts.
- Predict customer spending using Linear Regression.
- Classify customer tiers using Decision Tree.
- Segment customers using K-Means clustering.
- Display generated Python code and model responses.
- Interactive web interface built with Gradio.
- Gemini AI integration through smolagents and LiteLLM.

## Technologies Used

- **Python** – Core programming language.
- **Gradio** – Interactive web application interface.
- **Google Gemini AI** – AI model for generating machine-learning solutions.
- **smolagents** – AI agent framework.
- **LiteLLM** – LLM integration.
- **Pandas & NumPy** – Data handling and numerical operations.
- **Scikit-learn** – Machine-learning algorithms and preprocessing.

## Example Use Cases

### 1. Customer Spending Prediction
Generate a Linear Regression solution to predict customer spending and evaluate it using MAE and R².

### 2. Customer Tier Classification
Generate a Decision Tree classification solution to predict customer tiers and evaluate model accuracy.

### 3. Customer Segmentation
Apply K-Means clustering to customer spending and order data to discover three customer groups.

## Project Workflow

1. Upload a CSV or Excel dataset.
2. Enter a machine-learning query or select a quick-start prompt.
3. The AI agent processes the request.
4. The application displays the generated code and model response.
5. Review the generated solution and its results.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ai-powered-ml-code-generator.git
cd ai-powered-ml-code-generator
```

Install the required packages:

```bash
pip install gradio smolagents litellm pandas numpy scikit-learn openpyxl
```

## Gemini API Configuration

Create a Gemini API key through Google AI Studio.

Set the API key in PowerShell:

```powershell
$env:GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
```

Keep your API key private. Never upload it to GitHub.

## Run the Application

```bash
python ml_code_generator_recruiter_ui.py
```

Open the local Gradio URL displayed in your terminal, usually:

```text
http://127.0.0.1:7860
```

## Example Prompt

```text
Generate machine learning code to predict Total_Spent
using Linear Regression. Display the complete Python
code and the actual results, including MAE and R².
```

## Project Structure

```text
ai-powered-ml-code-generator/
│
├── ml_code_generator_recruiter_ui.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Security and Usage Notes

- Keep Gemini API keys in environment variables.
- Do not upload private datasets or customer personal information.
- Review generated Python code before running it.
- Generated metrics should be treated as actual results only when the corresponding code has been executed successfully.
- Model availability and API usage limits depend on your Gemini account and selected model.

## Future Improvements

- Add support for more machine-learning algorithms.
- Add downloadable generated Python scripts.
- Improve code execution and result visualization.
- Support more dataset formats.
- Add model comparison and performance reports.

## Author

**Pavan Kumar Torlapati**

GitHub: https://github.com/PavanTorlapatiCodes

LinkedIn: https://linkedin.com/in/pavan-torlapati-7543732ba

---

*An AI-assisted machine-learning project built to make data science workflows easier through natural-language instructions.*
