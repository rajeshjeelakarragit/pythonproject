# Generalized approach for N courses
courses = {
    "Math": {"Alice", "Bob", "Charlie", "Diana"},
    "Science": {"Bob", "Diana", "Edward", "Fiona"},
    "History": {"Alice", "Charlie", "Fiona", "George"},
}

# Get all sets of students
all_courses = list(courses.values())

# Students in all courses
students_in_all = set.intersection(*all_courses)
print("Students in all courses:", students_in_all)

# Students in at least one course
all_students = set.union(*all_courses)
print("All unique students:", all_students)

# Students in at least two courses
students_in_two_or_more = set()
for i in range(len(all_courses)):
    for j in range(i + 1, len(all_courses)):
        students_in_two_or_more |= all_courses[i] & all_courses[j]
print("Students in at least two courses:", students_in_two_or_more)


"""

"""