from resume.input import load_resume_data
from resume.template import format_resume
from resume.export import export_resume

def main():
    path = "data/sample.json"
    data = load_resume_data(path)
    content = format_resume(data)

    export_resume(content, filename="ragul_resume", format="md")

if __name__ == "__main__":
    main()
