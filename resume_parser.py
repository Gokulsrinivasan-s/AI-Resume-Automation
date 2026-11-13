from pypdf import PdfReader
import os


def extract_text(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text



resume_folder = "resumes"


for file in os.listdir(resume_folder):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(
            resume_folder,
            file
        )

        resume_text = extract_text(pdf_path)


        print("\n----------------")
        print(file)
        print("----------------")

        print(resume_text)