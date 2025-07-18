import os

def export_resume(content, filename="resume", format="txt"):
    ext = "md" if format == "md" else "txt"
    path = f"{filename}.{ext}"
    
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
    
    print(f"✅ Resume saved to {path}")
