import json

class TodoApp:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=4)
    
    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ کار '{task}' اضافه شد.")
    
    def show_tasks(self):
        print("📋 لیست کارها:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")
    
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"❌ کار '{removed}' حذف شد.")
        else:
            print("شماره کار نامعتبر است.")

# تست برنامه
app = TodoApp()
app.add_task("مطالعه پایتون پیشرفته")
app.add_task("تمرین Machine Learning")
app.show_tasks()
app.remove_task(0)
app.show_tasks()
