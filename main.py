# import requests
# import json

# url = "http://localhost:11434/api/generate"

# headers = {
#     "Content-Type": "application/json"
# }

# data = {
#     "model": "qwen2:0.5b",
#     "prompt": "Why is the sky blue?",
#     "stream": False
# }

# response = requests.post(url, headers=headers, data=json.dumps(data))

# if response.status_code == 200:  # Corrected status code check
#     try:
#         data = response.json()  # Using response.json() to directly parse the response to a dictionary
#         actual_response = data.get("response", "No response key found")
#         print(actual_response)
#     except json.JSONDecodeError:
#         print("Error: Failed to parse JSON response")
# else:
#     print("Error:", response.status_code, response.text)

import click
import requests
import json

API_URL = "http://localhost:11434/api/generate"
HEADERS = {"Content-Type": "application/json"}

def summarize_text(text):
    data = {
        "model": "qwen2:0.5b",
        "prompt": text,
        "stream": False
    }
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(data))
    if response.status_code == 200:
        try:
            data = response.json()
            return data.get("response", "No response key found")
        except json.JSONDecodeError:
            return "Error: Failed to parse JSON response"
    else:
        return f"Error: {response.status_code} {response.text}"

@click.command()
@click.option('--file', type=click.File('r'), help='Path to the text file to summarize.')
@click.option('--text', type=str, help='Text to summarize.')
def summarize(file, text):
    """
    This command-line tool summarizes the given text or text file.
    """
    if file:
        text_content = file.read()
        summary = summarize_text(text_content)
    elif text:
        summary = summarize_text(text)
    else:
        click.echo("Please provide either a text file or text input.")
        return

    click.echo("Summary:")
    click.echo(summary)

if __name__ == '__main__':
    summarize()
