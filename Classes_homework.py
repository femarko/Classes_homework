class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
    
    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        grade_total = []
        
        for value in (self.grades).values():
            grade_total += value
        return round(sum(grade_total) / len(grade_total), 1)

    def __gt__(self, some_object):
        if not isinstance(some_object, Student):
            print('Not a Student')
            return
        else:
            return self._average_grade() > some_object._average_grade()


    def __str__(self):
        separator = ', '
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_grade()}\nКурсы в процессе обучения: {separator.join(self.courses_in_progress)}\nЗавершенные курсы: {separator.join(self.finished_courses)}\n'

     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
            

class Lecturer(Mentor):
    def __init__(self, name, sirname):
        super().__init__(name, sirname)
        self.grades = {}

    def _average_grade(self):
        grade_total = []
        
        for value in (self.grades).values():
            grade_total += value
        return round(sum(grade_total) / len(grade_total), 1)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_grade()}\n'

    def __gt__(self, some_object):
        if not isinstance(some_object, Lecturer):
            print('Not a Lecturer')
            return
        else:
            return self._average_grade() > some_object._average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'


student_1 = Student('Ivan', 'Ivanov', 'male')
student_1.courses_in_progress += ['C#', 'C++', 'Java']
student_1.finished_courses += ['Python', 'JS', 'GIT']

student_2 = Student('Fedor', 'Fedorov', 'male')
student_2.courses_in_progress = ['C#', 'C++', 'Java']
student_2.finished_courses = ['Python', 'JS', 'GIT']

lecturer_1 = Lecturer('Alexey', 'Alexeev')
lecturer_1.courses_attached += ['C#', 'C++', 'Java']

lecturer_2 = Lecturer('Sergey', 'Sergeev')
lecturer_2.courses_attached += ['C#', 'C++', 'Java']

reviewer_1 = Reviewer('Petr', 'Petrov')
reviewer_1.courses_attached += ['C#', 'C++', 'Java']

reviewer_2 = Reviewer('Pavel', 'Pavlov')
reviewer_2.courses_attached += ['C#', 'C++', 'Java']

student_1.rate_lect(lecturer_1, 'C#', 10)
student_1.rate_lect(lecturer_1, 'C#', 9)
student_1.rate_lect(lecturer_1, 'C#', 10)
student_1.rate_lect(lecturer_1, 'C++', 10)
student_1.rate_lect(lecturer_1, 'C++', 9)
student_1.rate_lect(lecturer_1, 'C++', 9)
student_1.rate_lect(lecturer_1, 'Java', 10)
student_1.rate_lect(lecturer_1, 'Java', 10)
student_1.rate_lect(lecturer_1, 'Java', 9)
student_1.rate_lect(lecturer_2, 'C#', 10)
student_1.rate_lect(lecturer_2, 'C#', 9)
student_1.rate_lect(lecturer_2, 'C#', 10)
student_1.rate_lect(lecturer_2, 'C++', 10)
student_1.rate_lect(lecturer_2, 'C++', 9)
student_1.rate_lect(lecturer_2, 'C++', 9)
student_1.rate_lect(lecturer_2, 'Java', 10)
student_1.rate_lect(lecturer_2, 'Java', 10)
student_1.rate_lect(lecturer_2, 'Java', 9)

student_2.rate_lect(lecturer_1, 'C#', 10)
student_2.rate_lect(lecturer_1, 'C#', 10)
student_2.rate_lect(lecturer_1, 'C#', 7)
student_2.rate_lect(lecturer_1, 'C++', 5)
student_2.rate_lect(lecturer_1, 'C++', 8)
student_2.rate_lect(lecturer_1, 'C++', 10)
student_2.rate_lect(lecturer_1, 'Java', 10)
student_2.rate_lect(lecturer_1, 'Java', 10)
student_2.rate_lect(lecturer_1, 'Java', 5)
student_2.rate_lect(lecturer_2, 'C#', 7)
student_2.rate_lect(lecturer_2, 'C#', 10)
student_2.rate_lect(lecturer_2, 'C#', 9)
student_2.rate_lect(lecturer_2, 'C++', 8)
student_2.rate_lect(lecturer_2, 'C++', 10)
student_2.rate_lect(lecturer_2, 'C++', 6)
student_2.rate_lect(lecturer_2, 'Java', 10)
student_2.rate_lect(lecturer_2, 'Java', 9)
student_2.rate_lect(lecturer_2, 'Java', 9)

reviewer_1.rate_hw(student_1, 'C#', 10)
reviewer_1.rate_hw(student_1, 'C++', 9)
reviewer_1.rate_hw(student_1, 'Java', 10)
reviewer_1.rate_hw(student_2, 'C#', 3)
reviewer_1.rate_hw(student_2, 'C++', 2)
reviewer_1.rate_hw(student_2, 'Java', 1)

print(lecturer_1)
print(lecturer_2)
print(f'{lecturer_1 > lecturer_2}\n')
print(student_1)
print(student_2)
print(student_1 > student_2)


def average_course_hw_rate(students_list, course):
    total_grade = 0
    for student in students_list:
        for key, value  in student.grades.items():
            if key == course:
                total_grade += sum(student.grades[key])
    
    return round(total_grade / len(students_list), 2)

def average_course_lect_rate(lecturers_list, course):
    total_grade = 0
    for lecturer in lecturers_list:
        for key, value  in lecturer.grades.items():
            if key == course:
                total_grade += sum(lecturer.grades[key])
    
    return round(total_grade / len(lecturers_list), 2)

students_list = [student_1, student_2]
lecturers_list = [lecturer_1, lecturer_2]

print(average_course_hw_rate(students_list, 'C++'))
print()
print(average_course_lect_rate(lecturers_list, 'C++'))