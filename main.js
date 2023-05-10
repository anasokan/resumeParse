// This script for sample POC
const { Logger }=require('./logger');

const fs = require('fs');
const pdfParse = require('pdf-parse');
const docx = require('docx');
const regexp = require('regexp');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;

const resumesDir = 'C:/temp2/logs/resume';
const csvPath = './output.csv';



class ResumeParser {

    constructor() {
        this.test();
        logger.noise('ResumeParser constructor noise');
        logger.debug('ResumeParser constructor debug');
        logger.info('ResumeParser constructor info');
        logger.warn('ResumeParser constructor warn');
        logger.error('ResumeParser constructor error');
        this.processResumes();  
    }
    
    processResumes() {
        const csvWriter = createCsvWriter({
          path: csvPath,
          header: [
            { id: 'name', title: 'Name' },
            { id: 'phone', title: 'Phone' },
            { id: 'cgpa', title: 'CGPA/Marks' },
            { id: 'skills', title: 'Skills' },
            { id: 'college', title: 'College' }
          ]
        });

        fs.readdir(resumesDir, (err, files) => {
          if (err) {
            console.error(err);
            return;
          }

          const resumes = files.filter(file => /\.(pdf|docx)$/i.test(file));

          const data = resumes.map(file => {
            const ext = file.split('.').pop().toLowerCase();
            const filePath = `${resumesDir}/${file}`;

            let text = '';

            switch (ext) {
              case 'pdf':
                const pdfData = fs.readFileSync(filePath);
                text = pdfParse(pdfData).text;
                break;
              case 'docx':
                const docxData = fs.readFileSync(filePath);
                const doc = new docx.Document(docxData);
                text = doc.getText();
                break;
            }

            const nameMatch = text.match(/Name:(.*?)\n/);
            const name = nameMatch ? nameMatch[1].trim() : '';

            const phoneMatch = text.match(/Phone:(.*?)\n/);
            const phone = phoneMatch ? phoneMatch[1].trim() : '';

            const cgpaMatch = text.match(/CGPA:(.*?)\n/);
            const cgpa = cgpaMatch ? cgpaMatch[1].trim() : '';

            const skillsMatch = text.match(/Skills:(.*?)\n/);
            const skills = skillsMatch ? skillsMatch[1].trim() : '';

            const collegeMatch = text.match(/College:(.*?)\n/);
            const college = collegeMatch ? collegeMatch[1].trim() : '';

            return { name, phone, cgpa, skills, college };
          });

          csvWriter.writeRecords(data)
            .then(() => console.log(`Output written to ${csvPath}`))
            .catch(err => console.error(err));
        });
    }
    
    sleep(x) {
        return new Promise((resolve) => {  setTimeout(resolve, x);  });
    }

    async test() {

    }
}


function main(){
    new ResumeParser();
}
let logger=new Logger('poc',5);
main(); 