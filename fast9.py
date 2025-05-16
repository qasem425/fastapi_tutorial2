from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # يسمح بالوصول من أي مصدرز قم بتقييد هذا في الإنتاج
    allow_credentials=True, # نقوم بزيارت هذا الموقع render.com
    allow_methods=["*"],
    allow_headers=["*"],
)
class Student(BaseModel):
    id : int
    name :str
    grade : int
students =[
    Student(id=1,name="karim ali",grade=5),
    Student(id=2,name="qasem kder",grade=3),
]
@app.get("/students/")
def read_students():
    return students
@app.post("/students/")
def create_student(New_Student: Student):
    students.append(New_Student)
    return New_Student
@app.put("/students/{student_id}")
def update_student(student_id: int, update_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = update_student
            return update_student
    return {"error":"Student not found"}
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id ==student_id:
            del students[index]
            return {"message": "Student Deleted"}
    return {"error":"Student not found"}

