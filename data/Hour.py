class Hour(object):

    def __init__(self):
        self.lessons = []
        self.busyTeachers = []

    def canAddLesson(self, checkLesson):
        for lesson in self.lessons:
            if (lesson.className == checkLesson.className):
                return False

        for teacher in checkLesson.teachers:
            if (not teacher in self.busyTeachers):
                checkLesson.setTeacher(teacher)
                self.busyTeachers.append(teacher)
                return True

        return False

    def addLesson(self, checkLesson):
        self.lessons.append(checkLesson)