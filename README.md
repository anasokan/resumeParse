# Node.js Resume Parser Tool
This is a Node.js tool that processes resumes in PDF and DOCX format to extract information such as name, phone number, CGPA/marks, skillset, and college name. The tool outputs the extracted information into a CSV file.

## Requirements
To run this tool, you need to have the following installed:

- Node.js (v12 or above)
- npm

## Installation
1. Clone this repository: git clone https://github.com/<username>/node-resume-parser
2. Change to the project directory: cd node-resume-parser
3. Install the required npm packages: npm install

## Usage
1. Place your resumes in PDF and/or DOCX format in a folder.
2. Update the resumesDir variable in index.js with the path to the folder where you placed the resumes.
3. Run the tool: node index.js
4. The tool will create a CSV file named output.csv in the project directory containing the extracted information from the resumes.

## Configuration
You can customize the headers of the CSV file by updating the header array in the createCsvWriter function call in the processResumes method of the ResumeParser class.

## Contributing
If you would like to contribute to this project, please follow these steps:

1. Fork this repository.
2. Create a branch: git checkout -b my-feature-branch.
3. Make your changes and commit them: git commit -m "my feature description".
4. Push to the original branch: git push origin my-feature-branch.
5. Create a pull request.

## License
This project is licensed under the MIT License.