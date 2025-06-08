

DATA_FILE = "data.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def list_tasks(tasks):
    if not tasks:
        print("هیچ کاری وجود ندارد.")
    else:
        print("\nلیست کارها:")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['title']} [{status}]")
    print()

def add_task(tasks):
    title = input("عنوان کار جدید را وارد کن: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("کار اضافه شد.\n")

def mark_done(tasks):
    list_tasks(tasks)
    try:
        number = int(input("شماره کاری که انجام شده را وارد کن: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            save_tasks(tasks)
            print("با موفقیت علامت‌گذاری شد.\n")
        else:
            print("شماره نامعتبر.\n")
    except ValueError:
        print("ورودی باید عدد باشد.\n")

def delete_task(tasks):
    list_tasks(tasks)
    try:
        number = int(input("شماره کاری که می‌خواهی حذف کنی را وارد کن: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"«{removed['title']}» حذف شد.\n")
        else:
            print("شماره نامعتبر.\n")
    except ValueError:
        print("ورودی باید عدد باشد.\n")

def main():
    tasks = load_tasks()
    while True:
        print("=== مدیر لیست کارها ===")
        print("1. نمایش کارها")
        print("2. افزودن کار جدید")
        print("3. علامت‌گذاری انجام‌شده")
        print("4. حذف کار")
        print("5. خروج")

        choice = input("انتخاب شما: ")

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("خروج از برنامه. موفق باشی! 👋")
            break
        else:
            print("گزینه نامعتبر است.\n")

if __name__ == "__main__":
    main()


    # update featureTodo 
