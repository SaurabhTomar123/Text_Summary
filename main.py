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
    
#ensures that the script can be run as a standalone command-line tool.
if __name__ == '__main__':
    summarize()
