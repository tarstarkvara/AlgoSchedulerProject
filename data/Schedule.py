from random import shuffle

from data.Day import Day


class Schedule(object):

    def __init__(self, daysCount, lessonsCount):
        self.days = []

        for i in range(daysCount):
            self.days.append(Day(lessonsCount))

    def addLesson(self, lesson, day, hour):
        self.days[day].addLesson(lesson, hour)
        lesson.decrement()

    def getFirstAvailableHour(self, lesson, shuffleDays, shuffleHours):
        newHours = [i for i in range(len(self.days))]
        if (shuffleDays):
            shuffle(newHours)

        for dayNumber in newHours:
            day = self.days[dayNumber]
            hour = day.getFirstAvailableHour(lesson, shuffleHours)
            if (hour != None):
                return dayNumber, hour

        return None, None
