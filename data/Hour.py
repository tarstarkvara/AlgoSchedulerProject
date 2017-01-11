from time import sleep


class Hour(object):

    def __init__(self):
        self.lessons = []

    def canAddLesson(self, checkLesson):
        busyTeachers = []
        for lesson in self.lessons:
            if (lesson.className == checkLesson.className):
                return False
            busyTeachers.append(lesson.teacher)

        for teacher in checkLesson.teachers:
            if (teacher not in busyTeachers):
                checkLesson.setTeacher(teacher)
                return True

        return False

    def addLesson(self, checkLesson):
        self.lessons.append(checkLesson)