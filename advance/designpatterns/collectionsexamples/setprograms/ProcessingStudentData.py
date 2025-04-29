# Data: Students in different courses
math_students = {"Alice", "Bob", "Charlie", "Diana"}
science_students = {"Bob", "Diana", "Edward", "Fiona"}
history_students = {"Alice", "Charlie", "Fiona", "George"}

# 1. Students enrolled in all courses (Intersection)
students_in_all_courses = math_students & science_students & history_students
#students_in_all_courses = math_students & science_students
print("Students in all courses:", students_in_all_courses)

# 2. Students enrolled in only one course (Exclusive Members)


students_in_one_course = (
    (math_students - (science_students | history_students)) |
    (science_students - (math_students | history_students)) |
    (history_students - (math_students | science_students))
)
print("Students in only one course:", students_in_one_course)

# 3. Students enrolled in at least two courses (Common Members)
students_in_two_or_more_courses = (
    (math_students & science_students) |
    (science_students & history_students) |
    (math_students & history_students)
)
print("Students in at least two courses:", students_in_two_or_more_courses)

# 4. List all unique students (Union)
all_students = math_students | science_students | history_students
print("All unique students:", all_students)


"""

You have data about students who are enrolled in various courses. Perform the following tasks:

Find students who are enrolled in all courses.
Find students who are enrolled in only one course.
Identify students enrolled in at least two courses.
List all unique students across all courses.

Students in all courses: set()
Students in only one course: {'Edward', 'George'}
Students in at least two courses: {'Diana', 'Alice', 'Fiona', 'Bob', 'Charlie'}
All unique students: {'Diana', 'Fiona', 'Bob', 'Charlie', 'Edward', 'Alice', 'George'}



"""
