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

def greedy(days, hours, shuffleDays, shuffleHours):
    lessons = readData("Algo_Project_data.txt")
    schedule = Schedule(days, hours)

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
    return faults == 0

# No shuffle
schedule = greedy(5, 5, False, False)
print(evaluate_result(schedule))
print(isValid(schedule))

# Shuffle days
schedule = greedy(5, 5, True, False)
print(evaluate_result(schedule))
print(isValid(schedule))

# Shuffle hours
schedule = greedy(5, 5, False, True)
print(evaluate_result(schedule))
print(isValid(schedule))

# Shuffle days and hours
schedule = greedy(5, 5, True, True)
print(evaluate_result(schedule))
print(isValid(schedule))