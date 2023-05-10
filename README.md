# Resume Parser
This is a Python script that extracts information from resumes (in .pdf or .docx format) and saves it to a CSV file. It uses the OpenAI API to extract information like name, phone number, CGPA, skills, and college.

## Installation
1. Clone the repository from GitHub: git clone https://github.com/your-username/your-repo.git
2. Install the required packages using pip install -r requirements.txt.
3. Update the config.json file in the root directory of the project with your OpenAI API key:
{ "openai_api_key": "your_openai_api_key" }

  
## Usage
1. Place the resumes you want to process in the ./resume directory.
2. Run the script using python app.py.
3. The script will extract information from each resume and save it to ./output.csv.

## Limitations
The script currently only extracts information from resumes in .pdf or .docx format.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.