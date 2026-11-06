import json

class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
    
    def info(self):
        return f"{self.name} ({self.age} ساله) - رشته: {self.major}"

class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_students()
    
    def load_students(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Student(**s) for s in data]
        except FileNotFoundError:
            return []
    
    def save_students(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([s.__dict__ for s in self.students], f, ensure_ascii=False, indent=4)
    
    def add_student(self, student):
        self.students.append(student)
        self.save_students()
        print(f"✅ دانشجو '{student.name}' اضافه شد.")
    
    def show_students(self):
        print("📋 لیست دانشجویان:")
        for s in self.students:
            print(s.info())
    
    def search_student(self, name):
        results = [s for s in self.students if name.lower() in s.name.lower()]
        if results:
            print("🔍 نتایج جستجو:")
            for s in results:
                print(s.info())
        else:
            print("❌ دانشجویی با این نام یافت نشد.")

# تست برنامه
manager = StudentManager()
manager.add_student(Student("Samiullah", 25, "Computer Science"))
manager.add_student(Student("Asma", 22, "Software Engineering"))
manager.show_students()
manager.search_student("Asma")
