# selfai_tool_kit.py
import requests
import json
import subprocess
import re
import pyfiglet
import time

api_key = 'sk-proj-getyourown'

def runinput(input_content,GPTMODEL):
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": GPTMODEL,
        "messages": [{"role": "user", "content": input_content}],
        "temperature": 0.7
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps(data))
    output = response.json()['choices'][0]['message']['content']
    return output


def save_output_to_script_file(output):
    # Assuming 'output' contains the response from runinput function
    parts = output.split('XXX')
    if len(parts) >= 3:
        code = parts[1].strip()  # Extracts the content between the first pair of 'XXX'

        # Filter out any lines containing triple quotes
        filtered_code = "\n".join([line for line in code.split('\n') if '```' not in line])

        # Save the filtered code to a file
        with open('generated_script.py', 'w') as file:
            file.write(filtered_code)
    return(filtered_code)


def run_script():
    # Run the script and capture the combined standard output and standard error
    result = subprocess.run(
        ['python', 'generated_script.py'],  # Make sure this is the correct path to your Python script
        text=True,           # Ensure the output is captured as text
        capture_output=True  # Capture both stdout and stderr
    )

    # Extract the last 100 characters of the output
    output = result.stdout + result.stderr
    last_100_chars = output[-1000:]

    return last_100_chars


def check_for_outcome(script_output):
    f1_score = 0.0
    if "F1 SCORE" in script_output:
        has_f1_score = "YES"
        match = re.search(r"F1 SCORE\s*:\s*([0-9\.]+)", script_output)
        if match:
            f1_score = float(match.group(1))
    else:
        has_f1_score = "NO"
    
    return has_f1_score, f1_score




def print_big(text, color_code="\033[35m"):  # Default to purple color
    text=str(text)
    # ANSI escape sequence for resetting color
    reset = "\033[0m"

    # Generate ASCII art using pyfiglet
    ascii_art = pyfiglet.figlet_format(text, font="ansi_regular")  # Change the font as necessary

    # Combine the color, ASCII art text, and reset code
    colored_text = f"{color_code}{ascii_art}{reset}"

    # Print the colored ASCII art text
    print(colored_text)



def do_pause():
    # time.sleep(2)
    input("Press Enter to continue...")



