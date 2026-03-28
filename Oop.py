class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

    def rate_lecture(self, lecturer, course, grade): #оценка лекторам, ставят студенты
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.course_grades:
                lecturer.course_grades[course] += [grade]
            else:
                lecturer.course_grades[course] = [grade]
        else:
            return "Ошибка"

    def rate_hw_aver(self):
        grades_count = 0
        grades_sum =  0
        for grade in self.grades:
            grades_count += len(self.grades[grade])
            grades_sum += sum(self.grades[grade])
        if grades_count > 0:
            return grades_sum / grades_count
        else:
            return 0

    def __eq__(self, other):
        if not isinstance(other,Student):
            return NotImplemented
        return self.rate_hw_aver() == other.rate_hw_aver()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.rate_hw_aver() > other.rate_hw_aver()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.rate_hw_aver() < other.rate_hw_aver()

    def __str__(self):
        rate_st_aver = self.rate_hw_aver()
        return f"Имя: {self.name}\n" f"Фамилия: {self.surname}\n" f"Средняя оценка за лекции: {round(rate_st_aver)}\n"f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"f"Завершенные курсы: {', '.join(self.finished_courses)}\n"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturer_list = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grades = {}
        Lecturer.lecturer_list.append(self)

    def add_rate(self):
        grades_count = 0
        grades_sum =  0
        for grade in self.course_grades:
            grades_count += len(self.course_grades[grade])
            grades_sum += sum(self.course_grades[grade])
        if grades_count > 0:
            return grades_sum / grades_count
        else:
            return 0

    def __eq__(self, other):
        if not isinstance(other,Lecturer):
            return NotImplemented
        return self.add_rate() == other.add_rate()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.add_rate() > other.add_rate()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.add_rate() < other.add_rate()

    def __str__(self):
        mean_grade = self.add_rate()
        return f"Имя: {self.name}\n" f"Фамилия: {self.surname}\n" f"Средняя оценка за лекции: {round(mean_grade, 1)}\n"


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\n" f"Фамилия: {self.surname}\n"


student1 = Student("Роза", "Азора", 'Ж')
student1.courses_in_progress += ["Python", "Git"]
student1.finished_courses += ["Введение в программирование"]

student2 = Student("Маруся", "Климова", "Ж")
student2.courses_in_progress += ["Python", "Git"]
student2.finished_courses += ["Введение в программирование"]
students_list = [student1, student2]

lecturer1 = Lecturer("Ольга", "Леонова")
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Иван', 'Добренький')
lecturer2.courses_attached += ["Python"]
lecturer_list = [lecturer1, lecturer2]

reviewer1 = Reviewer("Фёдор", "Добров")
reviewer1.courses_attached += ['Python']

reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 10)

reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 7)

student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer1, 'Python', 8)

student1.rate_lecture(lecturer2, 'Python', 10)
student1.rate_lecture(lecturer2, 'Python', 9)
student1.rate_lecture(lecturer2, 'Python', 10)

print(reviewer1)
print(lecturer1)
print(lecturer2)
print(student1)
print(student2)

def grade_stud_all(students_list, course):
    all_stud_grade = 0
    quantity_stud = 0
    for cadet in students_list:
        if course in cadet.grades.keys():
            stud_score = 0
            for grades in cadet.grades[course]:
                stud_score += grades
            all_stud_grade = stud_score / len(cadet.grades[course])
            stud_score += all_stud_grade
            quantity_stud += 1
    if all_stud_grade == 0:
        return 0
    else:
        return round(all_stud_grade / quantity_stud, 1)

def grades_lecturers(lecturer_list, course):
    average_rating = 0
    lec = 0
    for lecturer in lecturer_list:
        if course in lecturer.course_grades.keys():
            lecturer_average_rates = 0
            for rate in lecturer.course_grades[course]:
                lecturer_average_rates += rate
            overall_lecturer_average_rates = lecturer_average_rates / len(lecturer.course_grades[course])
            average_rating += overall_lecturer_average_rates
            lec += 1
    if average_rating == 0:
        return 0
    else:
        return round(average_rating / lec, 1)


if student1 < student2:
    print(f"Средняя оценка за домашние задания {student1.name} {student1.surname} меньше средней оценки {student2.name} {student2.surname}\n")
elif student1 > student2:
    print(f"Средняя оценка за домашние задания {student1.name} {student1.surname} больше средней оценки {student2.name} {student2.surname}\n")
else:
    print(f"Средняя оценка за домашние задания {student1.name} {student1.surname} равна средней оценке {student2.name} {student2.surname}\n")


if lecturer1 < lecturer2:
    print(f"Средняя оценка за лекции {lecturer1.name} {lecturer1.surname} меньше средней оценки {lecturer2.name} {lecturer2.surname}\n")
elif lecturer1 > lecturer2:
    print(f"Средняя оценка за лекции {lecturer1.name} {lecturer1.surname} больше средней оценки {lecturer2.name} {lecturer2.surname}\n")
else:
    print(f"Средняя оценка за лекции {lecturer1.name} {lecturer1.surname} равна средней оценке {lecturer2.name} {lecturer2.surname}\n")


print(f"Средняя оценка студентов за курс 'Python': {grade_stud_all(students_list, "Python")}\n")

print(f"Средняя оценка лекторов за курс 'Python': {grades_lecturers(lecturer_list, "Python")}\n")
