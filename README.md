# Text Summarization Tool

This Python script summarizes text using the Ollama API and the Qwen2 0.5B model. It can take a text file as a parameter or direct text input and return the summary.

## Prerequisites

- Python 3.x
- `requests` library
- `click` library

You can install the required libraries using:

pip install requests click

Summarizing a Text File
To summarize the content of a text file, use the --file option:
python summarize_text.py --file path/to/your/textfile.txt



Summarizing Direct Text Input
To summarize a direct text input, use the --text option:
python summarize_text.py --text "Your text goes here."