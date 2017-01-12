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
        for i in range(lesson.times):
            day, hour = schedule.getFirstAvailableHour(lesson, shuffleDays, shuffleHours)
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
    print("Faults: " + str(faults))
    return faults == 0

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
                for i in range(lesson.times):
                    day, hour = schedule.getFirstAvailableHour(lesson, shuffleDays, shuffleHours)
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

    # Schedule teacher by teacher
    for subject in subjects:
        for lesson in lessons:
            if (lesson.times > 0 and subject == lesson.name):
                for i in range(lesson.times):
                    day, hour = schedule.getFirstAvailableHour(lesson, shuffleDays, shuffleHours)
                    if (day != None):
                        schedule.addLesson(lesson, day, hour)

    return schedule

def printInfo(schedule):
    print(evaluate_result(schedule))
    print(isValid(schedule))

def runTests():

    # No shuffle
    printInfo(greedy(False, False))
    printInfo(greedyTeacher(False, False))
    printInfo(greedySubject(False, False))

    # Shuffle days
    printInfo(greedy(True, False))
    printInfo(greedyTeacher(True, False))
    printInfo(greedySubject(True, False))

    # Shuffle hours
    printInfo(greedy(False, True))
    printInfo(greedyTeacher(False, True))
    printInfo(greedySubject(False, True))

    # Shuffle days and hours
    printInfo(greedy(True, True))
    printInfo(greedyTeacher(True, True))
    printInfo(greedySubject(True, True))

runTests()
