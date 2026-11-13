import os
import gdown


def download_resume(url, name):

    os.makedirs(
        "resumes",
        exist_ok=True
    )


    file_path = f"resumes/{name}_resume.pdf"


    gdown.download(
        url,
        file_path,
        quiet=False
    )


    print(
        "Saved:",
        file_path
    )


    return file_path