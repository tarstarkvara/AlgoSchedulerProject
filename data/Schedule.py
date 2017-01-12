from random import shuffle

from data.Day import Day


class Schedule(object):

    def __init__(self, daysCount, lessonsCount):
        self.days = []

        for i in range(daysCount):
            self.days.append(Day(lessonsCount))

    def addLesson(self, lesson, day, hour):
        lesson.decrement()
        self.days[day].addLesson(lesson, hour)

    def getAvailableHour(self, lesson, shuffleDays, shuffleHours):
        newDays = [i for i in range(len(self.days))]
        if (shuffleDays):
            shuffle(newDays)

        for dayNumber in newDays:
            day = self.days[dayNumber]
            hour = day.getAvailableHour(lesson, shuffleHours)
            if (hour != None):
                return dayNumber, hour

        return None, None
