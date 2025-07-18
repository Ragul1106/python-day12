def format_resume(data):
    lines = []
    
    lines.append(f"# {data['name']}\n")
    lines.append(f"**{data['title']}**\n")
    contact = data['contact']
    lines.append(f"- 📧 {contact['email']}  |  📞 {contact['phone']}  |  📍 {contact['location']}\n")

    lines.append("## 🧠 Summary")
    lines.append(data['summary'] + "\n")

    lines.append("## 🛠️ Skills")
    lines.append(", ".join(data['skills']) + "\n")

    lines.append("## 💼 Experience")
    for job in data['experience']:
        lines.append(f"**{job['role']}** at *{job['company']}* ({job['duration']})")
        for d in job['details']:
            lines.append(f"- {d}")
        lines.append("")

    lines.append("## 🎓 Education")
    for edu in data['education']:
        lines.append(f"- {edu['degree']}, {edu['institution']} ({edu['year']})")

    return "\n".join(lines)
