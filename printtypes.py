student_info = {
   "name": "Alice",
   "age": 21,
   "major": "Computer Science"
}

name = student_info["name"]


grad_year = student_info.get("graduation_year", "2023")
print(grad_year)