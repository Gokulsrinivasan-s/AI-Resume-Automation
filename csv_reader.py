import pandas as pd


data = pd.read_csv("applicants.csv")


for index, row in data.iterrows():

    name = row["Full Name"]
    email = row["Email"]
    resume_link = row["Resume"]

    print(name)
    print(email)
    print(resume_link)
