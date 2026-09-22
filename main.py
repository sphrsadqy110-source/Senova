import json



def load_tasks():
    with open("data/tasks.json", "r", encoding="utf-8") as file:
        return json.load(file)

def save_tasks(tasks):
    with open("data/tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

def add_subject(subject):
    tasks = load_tasks()
    for task in tasks:
        if task["subject"] == subject:
            print("Subject already exists!")
            return

    task = {
        "subject": subject,
        "day": 1,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"{subject} added!")

def show_tasks():
    tasks = load_tasks()
    print("\nCurrent Tasks:")
    for task in tasks:
        status = "✓" if task["completed"] else " "
        print(f"[{status}] {task["subject"]} - Day{task["day"]}")

def complete_task(subject):
    tasks = load_tasks()
    for task in tasks:
        if task["subject"] == subject:
            task["completed"] = True

            new_task ={
                "subject": subject,
                "day": task["day"] + 1,
                "completed": False
            }

            tasks.remove(task)
            tasks.append(new_task)
            save_tasks(tasks)
            return
    print("Subject NOT found!")

add_subject("Math")
add_subject("Circuits")
add_subject("Python")
show_tasks()
subject = input("which subject did you completed?")
complete_task(subject)
show_tasks()