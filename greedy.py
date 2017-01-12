from collections import defaultdict

from data.Lesson import Lesson
from data.Schedule import Schedule


def readData(filename):
    lessons = []
    f = open(filename, 'r', encoding='utf-8')
    x = f.readline()
    x = f.readline()
    while len(x) > 0:
        data = x.strip().split('\t')
        for i in range(int(data[3])):
            lesson = Lesson(data)
            lessons.append(lesson)
        x = f.readline()
    f.close()
    return lessons


def evaluate_result(schedule):
    score = 0
    teachers = defaultdict(defaultdict)
    classes = defaultdict(defaultdict)
    days = schedule.days
    for day in days:
        for hour in day.hours:
            for lesson in hour.lessons:
                teachers[lesson.teacher] = defaultdict(defaultdict)
                classes[lesson.className] = defaultdict(defaultdict)
    dayCount = 0
    for day in days:
        hourCount = 0
        for hour in day.hours:
            for lesson in hour.lessons:
                try:
                    teachers[lesson.teacher][dayCount].append(hourCount)
                except AttributeError:
                    teachers[lesson.teacher][dayCount] = [hourCount]
                try:
                    classes[lesson.className][dayCount].append(hourCount)
                except AttributeError:
                    classes[lesson.className][dayCount] = [hourCount]
            hourCount += 1
        dayCount += 1
    for day in teachers:
        for hour in teachers[day]:
            lessons = sorted(teachers[day][hour])
            if len(lessons) > 1:
                for lesson in range(len(lessons) - 1):
                    if lessons[lesson + 1] != lessons[lesson]:
                        score += lessons[lesson + 1] - lessons[lesson] - 1
            if max(lessons) > 5:
                score += 5 * (max(lessons) - 5)
    for day in classes:
        for hour in classes[day]:
            lessons = sorted(classes[day][hour])
            if len(lessons) > 1:
                for lesson in range(len(lessons) - 1):
                    score += (lessons[lesson + 1] - lessons[lesson] - 1) * 3
            if max(lessons) > 5:
                score += 5 * (max(lessons) - 5)
    return score


def greedy(shuffleDays, shuffleHours):
    lessons = readData("Algo_Project_data.txt")
    schedule = Schedule(5, 5)

    for lesson in lessons:
        day, hour = schedule.getAvailableHour(lesson, shuffleDays, shuffleHours)
        if (day != None):
            schedule.addLesson(lesson, day, hour)

    return schedule


def greedyTeacher(shuffleDays, shuffleHours):
    lessons = readData("Algo_Project_data.txt")
    schedule = Schedule(5, 5)

    # Get all teachers
    teachers = []
    for lesson in lessons:
        for teacher in lesson.teachers:
            if (teacher not in teachers):
                teachers.append(teacher)

    # Schedule teacher by teacher
    for teacher in teachers:
        for lesson in lessons:
            if (lesson.times > 0 and teacher in lesson.teachers):
                day, hour = schedule.getAvailableHour(lesson, shuffleDays, shuffleHours)
                if (day != None):
                    schedule.addLesson(lesson, day, hour)

    subjects = []
    for lesson in lessons:
        if (lesson.name not in subjects):
            subjects.append(lesson.name)

    return schedule


def greedySubject(shuffleDays, shuffleHours):
    lessons = readData("Algo_Project_data.txt")
    schedule = Schedule(5, 5)

    # Get all subjects
    subjects = []
    for lesson in lessons:
        if (lesson.name not in subjects):
            subjects.append(lesson.name)

    # Schedule subject by subject
    for subject in subjects:
        for lesson in lessons:
            if (lesson.times > 0 and subject == lesson.name):
                day, hour = schedule.getAvailableHour(lesson, shuffleDays, shuffleHours)
                if (day != None):
                    schedule.addLesson(lesson, day, hour)

    return schedule


def isValid(schedule):
    faults = 0
    for day in schedule.days:
        for hour in day.hours:
            busyTeachers = []
            for lesson in hour.lessons:
                if (lesson.teacher in busyTeachers):
                    faults += 1
                busyTeachers.append(lesson.teacher)
    return faults == 0


def printResult(schedule):
    score = evaluate_result(schedule)
    # print("Score: " + str(score))
    # print(isValid(schedule))
    return score


def runTests(tests):

    greedyFF = 0
    greedyTF = 0
    greedyFT = 0
    greedyTT = 0

    greedyTeacherFF = 0
    greedyTeacherTF = 0
    greedyTeacherFT = 0
    greedyTeacherTT = 0

    greedySubjectFF = 0
    greedySubjectTF = 0
    greedySubjectFT = 0
    greedySubjectTT = 0

    for i in range(tests):

        # No shuffle
        greedyFF += printResult(greedy(False, False))
        greedyTeacherFF += printResult(greedyTeacher(False, False))
        greedySubjectFF += printResult(greedySubject(False, False))

        # Shuffle days
        greedyTF += printResult(greedy(True, False))
        greedyTeacherTF += printResult(greedyTeacher(True, False))
        greedySubjectTF += printResult(greedySubject(True, False))

        # Shuffle hours
        greedyFT += printResult(greedy(False, True))
        greedyTeacherFT += printResult(greedyTeacher(False, True))
        greedySubjectFT += printResult(greedySubject(False, True))

        # Shuffle days and hours
        greedyTT += printResult(greedy(True, True))
        greedyTeacherTT += printResult(greedyTeacher(True, True))
        greedySubjectTT += printResult(greedySubject(True, True))

    print("GreedyFF: " + str(greedyFF / tests))
    print("GreedyTF: " + str(greedyTF / tests))
    print("GreedyFT: " + str(greedyFT / tests))
    print("GreedyTT: " + str(greedyTT / tests))

    print("GreedyTeacherFF: " + str(greedyTeacherFF / tests))
    print("GreedyTeacherTF: " + str(greedyTeacherTF / tests))
    print("GreedyTeacherFT: " + str(greedyTeacherFT / tests))
    print("GreedyTeacherTT: " + str(greedyTeacherTT / tests))

    print("GreedySubjectFF: " + str(greedySubjectFF / tests))
    print("GreedySubjectTF: " + str(greedySubjectTF / tests))
    print("GreedySubjectFT: " + str(greedySubjectFT / tests))
    print("GreedySubjectTT: " + str(greedySubjectTT / tests))


runTests(1000)
