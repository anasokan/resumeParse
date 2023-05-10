import os
import re
import pdfplumber
from docx import Document
import openai

resumes_dir = './resume'
csv_path = './output.csv'
with open('config.json') as f:
    config = json.load(f)
openai.api_key = config["openai_api_key"]


openai.api_key = openai_api_key

class ResumeParser:
    def init(self):
        print(f'start 21')
        self.process_resumes()

    def process_resumes(self):
        #openai_api = Api(api_key=openai_api_key)
        print(f'Ostarted')
        with open(csv_path, 'w') as csv_file:
            header = ['name', 'phone', 'cgpa', 'skills', 'college']
            csv_file.write(','.join(header) + '\n')

            for file in os.listdir(resumes_dir):
                file_ext = os.path.splitext(file)[1]

                if file_ext.lower() not in ['.pdf', '.docx']:
                    continue

                file_path = os.path.join(resumes_dir, file)

                if file_ext.lower() == '.pdf':
                    with pdfplumber.open(file_path) as pdf:
                        text = ''.join([page.extract_text() for page in pdf.pages])
                elif file_ext.lower() == '.docx':
                    doc = Document(file_path)
                    text = '\n'.join([para.text for para in doc.paragraphs])

                prompt = f'Extract the name from the following resume:\n\n{text}\n\nName:'
                response = openai.Completion.create(
                    engine='davinci',
                    prompt=prompt,
                    max_tokens=10,
                    n=1,
                    stop='\n'
                )
                name = response.choices[0].text.strip()


                prompt = f'Extract the name from the following resume:\n\n{text}\n\Phone:'
                response = openai.Completion.create(
                    engine='davinci',
                    prompt=prompt,
                    max_tokens=10,
                    n=1,
                    stop='\n'
                )
                phone = response.choices[0].text.strip()
                
                prompt = f'Extract the name from the following resume:\n\n{text}\n\cgpa:'
                response = openai.Completion.create(
                    engine='davinci',
                    prompt=prompt,
                    max_tokens=10,
                    n=1,
                    stop='\n'
                )
                cgpa = response.choices[0].text.strip()                

                prompt = f'Extract the name from the following resume:\n\n{text}\n\skills:'
                response = openai.Completion.create(
                    engine='davinci',
                    prompt=prompt,
                    max_tokens=10,
                    n=1,
                    stop='\n'
                )
                skills = response.choices[0].text.strip()

                prompt = f'Extract the name from the following resume:\n\n{text}\n\college:'
                response = openai.Completion.create(
                    engine='davinci',
                    prompt=prompt,
                    max_tokens=10,
                    n=1,
                    stop='\n'
                )
                college = response.choices[0].text.strip()


                data = [name, phone, cgpa, skills, college]
                csv_file.write(','.join(data) + '\n')

        print(f'Output written to {csv_path}')


def main():
    print(f'start 2')
    ResumeParser().process_resumes();
    
print(f'start 0')
main()
print(f'start ')