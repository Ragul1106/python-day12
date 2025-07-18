def choose_priority():
    print("Priority Levels: low / medium / high")
    p = input("Enter priority: ").lower()
    return p if p in ("low", "medium", "high") else "low"
