import pandas as pd
import os

from email_sender import send_email
from matcher import calculate_match_score
from resume_parser import extract_text
from jd_reader import read_job_description
from resume_downloader import download_resume



# Read applicant CSV

data = pd.read_csv(
    "applicants.csv"
)



# Read Job Description

jd_text = read_job_description(
    "job_description/ml_engineer.txt"
)



# Store results

selected_candidates = []

rejected_candidates = []



# Process every applicant

for index, row in data.iterrows():

    name = row["Full Name"]
    email = row["Email"]
    resume_link = row["Resume"]


    print("\nChecking:", name)



    try:

        # Download resume from Google Drive

        resume_path = download_resume(
            resume_link,
            name
        )


        print(
            "Resume downloaded:",
            resume_path
        )



        # Extract resume text

        resume_text = extract_text(
            resume_path
        )



        # Generate AI score

        score, matched_skills = calculate_match_score(
            resume_text,
            jd_text
        )



        print(
            "Score:",
            round(score,2)
        )


        print(
            "Matched Skills:",
            matched_skills
        )



        # Selection process

        if score >= 70:


            print(
                "Selected:",
                name
            )


            # Send confirmation email

            send_email(
                email,
                name
            )


            selected_candidates.append(
                {
                    "Full Name": name,
                    "Email": email,
                    "Resume": resume_link,
                    "Score": round(score,2),
                    "Matched Skills": ", ".join(matched_skills),
                    "Status": "Selected",
                    "Mail Status": "Sent"
                }
            )



        else:


            print(
                "Rejected:",
                name
            )


            rejected_candidates.append(
                {
                    "Full Name": name,
                    "Email": email,
                    "Resume": resume_link,
                    "Score": round(score,2),
                    "Matched Skills": ", ".join(matched_skills),
                    "Status": "Rejected",
                    "Mail Status": "Not Sent"
                }
            )



    except Exception as e:

        print(
            "Error processing",
            name,
            ":",
            e
        )



# Convert results to DataFrame

selected_df = pd.DataFrame(
    selected_candidates
)


rejected_df = pd.DataFrame(
    rejected_candidates
)

# Create output folder

os.makedirs(
    "output",
    exist_ok=True
)


# Save Excel reports

selected_df.to_excel(
    "output/Selected_Candidates.xlsx",
    index=False
)


rejected_df.to_excel(
    "output/Rejected_Candidates.xlsx",
    index=False
)



print("\n======================")
print("Process Completed")
print("======================")

print("\nProcess Completed")
print("Excel files saved inside output folder")