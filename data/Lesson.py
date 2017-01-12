class Lesson(object):

    def __init__(self, data):
        self.className = data[0]
        self.name = data[1]

        self.teachers = []
        for teacher in data[2].replace("(", "").replace(")", "").lower().split(","):
            self.teachers.append(teacher)

        self.times = 1
        self.groups = data[4]

    def isAvailable(self):
        return self.times > 0

    def decrement(self):
        self.times -= 1

    def setTeacher(self, teacher):
        self.teacher = teacher