def read_job_description(file_path):

    with open(file_path, "r") as file:

        jd_text = file.read()

    return jd_text



jd = read_job_description(
    "job_description/ml_engineer.txt"
)


print(jd)