#!/usr/bin/env python3
from collections import defaultdict


def readlessondata(filename):
    lessondata = defaultdict(list)
    f = open(filename, 'r', encoding='utf-8')
    x = f.readline()
    x = f.readline()
    while len(x) > 0:
        data = x.strip().split('\t')
        lessondata[data[-2]] += (data[:-2] + data[-1:])
        x = f.readline()
    return lessondata
##struktuur tunniplaani väljundil (sonastike möll):
#                                  päev1: [tund1:[[klass,tund,opetaja],[klass,tund,opetaja],...],
#                                         tund2:[[klass,tund,opetaja],[klass,tund,opetaja],...],...],
#                                  päev2: [tund1:[[klass,tund,opetaja],[klass,tund,opetaja],...],
#                                         tund2:[[klass,tund,opetaja],[klass,tund,opetaja],...],...]

test_dict = {'päev1': {'1': [['10a','matemaatika', 'opetaja1'],['10b','matemaatika','opetaja2']],
                       '2': [['10a','bioloogia','bio1'],['10c','matemaatika','opetaja2']],
                       '3': [['10a', 'matemaaika', 'opetaja1'], ['10b', 'fyysika', 'fys1']]},
             'päev2': {'1': [['10a','matemaatika', 'opetaja1'],['10b','matemaatika','opetaja2']],
                       '2': [['10c','bioloogia','bio1'],['10c','matemaatika','opetaja2']],
                       '3': [['10c', 'matemaatika', 'opetaja1'], ['10b', 'fyysika', 'fys1']]}
            }

test_dict2 = {'päev1': {'1': [['10a','matemaatika', 'opetaja1'],['10b','matemaatika','opetaja2']],
                       '2': [['10a','bioloogia','bio1'],['10c','matemaatika','opetaja2']],
                       '3': [['10a', 'matemaatika', 'opetaja1'], ['10b', 'fyysika', 'fys1']]},
              'päev2': {'1': [['10a','matemaatika', 'opetaja1'],['10b','matemaatika','opetaja2']],
                       '2': [['10c','bioloogia','bio1'],['10c','matemaatika','opetaja2']],
                       '3': [['10c', 'matemaatika', 'opetaja1'], ['10b', 'fyysika', 'fys1']],
                       '4': [['10a','matemaatika', 'opetaja1'],['10b','matemaatika','opetaja2']],
                       '5': [['10c','bioloogia','bio1'],['10c','matemaatika','opetaja2']],
                       '6': [['10c', 'matemaatika', 'opetaja1'], ['10b', 'fyysika', 'fys1']]}
             }
def evaluate_result(schedule, optimal_lessons):
    score = 0
    teachers = defaultdict(defaultdict)
    classes = defaultdict(defaultdict)
    for i in schedule:
        for j in schedule[i]:
            for k in schedule[i][j]:
                teachers[k[2]] = defaultdict(defaultdict)
                classes[k[0]] = defaultdict(defaultdict)
    for i in schedule:
        for j in schedule[i]:
            for k in schedule[i][j]:
                try:
                    teachers[k[2]][i].append(int(j))
                except AttributeError:
                    teachers[k[2]][i] = [int(j)]
                try:
                    classes[k[0]][i].append(int(j))
                except AttributeError:
                    classes[k[0]][i] = [int(j)]
    for i in teachers:
        for j in teachers[i]:
            lessons = sorted(teachers[i][j])
            if len(lessons) > 1:
                for k in range(len(lessons)-1):
                    score += lessons[k+1] - lessons[k] - 1
            if max(lessons)>5:
                score += 5*(max(lessons)-5)
    for i in classes:
        for j in classes[i]:
            lessons = sorted(classes[i][j])
            if len(lessons) > 1:
                for k in range(len(lessons)-1):
                    score += (lessons[k+1] - lessons[k] - 1)*3
            if max(lessons)>5:
                score += 5*(max(lessons)-5)
    return score

print(readlessondata('Algo_Project_data.txt'))
print(evaluate_result(test_dict,5))
print(evaluate_result(test_dict2,5))