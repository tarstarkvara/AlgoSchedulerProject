from random import shuffle

from data.Hour import Hour


class Day(object):

    def __init__(self, lessonsCount):
        self.hours = []

        for i in range(lessonsCount):
            self.hours.append(Hour())

    def canAddLesson(self, lesson, hour):
        return self.hours[hour].canAddLesson(lesson)

    def addLesson(self, lesson, hour):
        self.hours[hour].addLesson(lesson)

    def getAvailableHour(self, lesson, shuffleHours):
        newHours = [i for i in range(len(self.hours))]
        if (shuffleHours):
            shuffle(newHours)

        for hour in newHours:
            canAddLesson = self.canAddLesson(lesson, hour)
            if (canAddLesson):
                return hour

        return None