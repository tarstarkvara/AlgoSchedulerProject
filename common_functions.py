#!/usr/bin/env python3
from collections import defaultdict
from random import shuffle
from math import exp
import random

def readlessondata(filename):
    lessondata = defaultdict(list)
    f = open(filename, 'r', encoding='utf-8')
    x = f.readline()
    x = f.readline()
    while len(x) > 0:
        data = x.strip().split('\t')
        lessondata[data[-2]] += (data[:-2] + data[-1:])
        x = f.readline()
    f.close()
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

reference = {'day1': {1: [['10a','fyysika', 'oks'], ['10b','matemaatika','timak'], ['10c', 'bioloogia','kaarna'],['10d', 'geograafia','seevri'], ['10e', 'kunst', 'beier'], ['11a','matemaatika','hüva'],['11b','B_keel_vene_pr_saksa', '(Matto,Roots,L_Titova,O_Titova)'],['11c','B_keel_vene_pr_saksa,A_keel_inglise', '(Matto,Roots,O_Titova);Hunt'],['11d','B_keel_vene_pr_saksa','(Matto,Roots,L_Titova,O_Titova)'],['11e','matemaatika','orav'],['12a','kirjandus','pluum'],['12b','fyysika','reemann'],['12c','keemia','paabo'],['12d','fyysika','paaver'],['12e','ajalugu','punga']],
                       2: [['10a','geograafia', 'seevri'],['10b', 'B_keel_vene_pr_saksa,A_keel_inglise', '(O_Titova,Niitvägi,Matto);roostoja'], ['10c', 'B_keel_vene_pr_saksa,A_keel_inglise', '(O_Titova,Niitvägi,Matto);ojaveer'], ['10d','B_keel_vene_pr_saksa,A_keel_inglise', '(L_Titova,Niitvägi,Matto);rootsi'], ['10e', 'kirjandus', 'pluum'], ['11a','fyysika','reemann'],['11b','matemaatika','hüva'],['11c','matemaatika','timak'],['11d','kunst','beier'],['11e','muusika','keerberg'],['12a','fyysika','oks'],['12b','bioloogia','kaarna'],['12c','ajalugu','punga'],['12d','matemaatika','orav'],['12e','fyysika','paaver']],
                       3: [['10a','mat_fys_pr', 'timak,reemann'],['10b', 'informaatika,B_keel_vene_pr_saksa', 'mägi;L_Titova'], ['10c', 'muusika', 'keerberg'], ['10d', 'C_keel_prantsuse_saksa', 'Niitvägi,Matto'], ['10e', 'geograafia', 'seevri'], ['11a','A_keel_inglise', '(Hunt,Köhler,Ojaveer,Roostoja)'],['11b','keemia','paabo'],['11c','kirjandus','pluum'],['11d','bioloogia','kaarna'],['11e','A_keel_inglise', '(Hunt,Köhler,Ojaveer,Roostoja)'],['12a','matemaatika','hüva'],['12b','ajalugu','punga'],['12c','filosoofia','pettai'],['12d','usundiõpetus','schihalejev'],['12e','matemaatika','orav']],
					   4: [['10a','mat_fys_pr', 'timak,reemann'],['10b', 'informaatika,A_keel_inglise', 'mägi;(köhler,hildebrandt,hunt)'], ['10c', 'B_keel_vene_pr_saksa,A_keel_inglise', 'L_Titova;(köhler,hildebrandt,hunt)'], ['10d', 'B_keel_vene_pr_saksa,A_keel_inglise', 'O_Titova;(köhler,hildebrandt,hunt)'], ['10e', 'inimeseõpetus', 'saar'], ['11a','keemia','paabo'],['11b','ajalugu','pettai'],['11c','bioloogia','ustav'],['11d','muusika','keerberg'],['11e','fyysika','paaver'],['12a','matemaatika','hüva'],['12c','matemaatika','orav'],['12d','bioloogia','kaarna'],['12e','usundiõpetus','schihalejev']]},
             'day2': {1: [['10a','muusika', 'keerberg'], ['10b', 'geograafia', 'seevri'], ['10c', 'keemia', 'paabo'], ['10d', 'matemaatika','kiisel'], ['10e', 'kunst', 'beier'], ['11a','matemaatika','hüva'],['11b','ajalugu','pettai'],['11c','kehaline','saarva,poom'],['11d','bioloogia','kaarna'],['11e','kirjandus','soodla'],['12a','kirjandus','pluum'],['12b','fyysika','reemann'],['12c','fyysika','oks'],['12d','ühiskonnaõpetus','ristikivi'],['12e','filosoofia','paaver']],
                       2: [['10a','geograafia', 'seevri'],['10b', 'B_keel_vene_pr_saksa,A_keel_inglise', '(O_Titova,Niitvägi,Matto);roostoja'], ['10c',  'B_keel_vene_pr_saksa,A_keel_inglise', '(O_Titova,Niitvägi,Matto);ojaveer'], ['10d', 'B_keel_vene_pr_saksa,A_keel_inglise', '(L_Titova,Niitvägi,Matto);rootsi'], ['10e', 'matemaatika', 'kiisel'], ['11a','kirjandus','soodla'],['11b','mat_fys_pr','reemann,hüva'],['11c','ajalugu','pettai'],['11d','kunst','beier'],['11e','fyysika','paaver'],['12a','ühiskonnaõpetus','ristikivi'],['12b','kirjandus','piirimäe'],['12c','keemia','paabo'],['12d','bioloogia','kaarna'],['12e','kirjandus','pluum']],
                       3: [['10a','fyysika', 'oks'], ['10b', 'kehaline', 'saarva,poom'], ['10c', 'kirjandus', 'lummo,tepp'], ['10d', 'eesti keel', 'piirimäe'], ['10e', 'ajalugu', 'pettai'], ['11a','fyysika','reemann'],['11b','A_keel_inglise', '(Hildebrandt,Ojaveer,Roostoja),Rootsi'],['11c','B_keel_vene_pr_saksa,A_keel_inglise', '(Hildebrandt,Ojaveer,Roostoja);L_Titova'],['11d','A_keel_inglise', '(Hildebrandt,Ojaveer,Roostoja),Köhler'],['11e','B_keel_vene,informaatika', 'O_Titova;Mägi'],['12a','matemaatika', 'hüva'],['12b','matemaatika','kiisel'],['12c','kirjandus','soodla'],['12d','fyysika','paaver'],['12e','muusika','keerberg']],
					   4: [['10a','kirjandus', 'lummo,tepp'], ['10b', 'informaatika,A_keel_inglise', 'mägi;(köhler,hildebrandt,hunt)'], ['10c', 'B_keel_vene_pr_saksa,A_keel_inglise', 'L_Titova;(köhler,hildebrandt,hunt)'], ['10d', 'B_keel_vene_pr_saksa,A_keel_inglise', 'O_Titova;(köhler,hildebrandt,hunt)'], ['10e', 'geograafia', 'seevri'], ['11a','keemia','paabo'],['11b','mat_fys_pr','reemann,hüva'],['11c','bioloogia','ustav'],['11d','muusika','keerberg'],['11e','bioloogia','kaarna'],['12a','ajalugu','punga'],['12b','mat_fys_pr','kiisel,oks'],['12c','filosoofia','pettai'],['12d','kehaline','saarva,poom'],['12e','fyysika','paaver']],
					   5: [['10a','kehaline', 'saarva,poom'], ['10b', 'kirjandus', 'piirimäe'], ['10c', 'muusika', 'keerberg'], ['10d', 'geograafia', 'seevri'], ['10e', 'inimeseõpetus', 'saar'], ['11a','A_keel_inglise', '(Hunt,Köhler,Ojaveer,Roostoja)'],['11b','keemia','paabo'],['11d','kirjandus','mandri,tepp'],['11e','A_keel_inglise', '(Hunt,Köhler,Ojaveer,Roostoja)'],['12a','mat_fys_pr', 'oks,hüva'],['12d','kirjandus','soodla'],['12e','ajalugu','punga']]},
			 'day3': {1: [['10a','fyysika', 'oks'],['10b',  'B_keel_vene_pr_saksa,A_keel_inglise', '(O_Titova,Niitvägi,Matto);roostoja'], ['10c', 'B_keel_vene_pr_saksa,A_keel_inglise', '(O_Titova,Niitvägi,Matto);ojaveer'], ['10d','B_keel_vene_pr_saksa,A_keel_inglise', '(L_Titova,Niitvägi,Matto);rootsi'], ['10e', 'kirjandus','pluum'], ['11a','kehaline', 'saarva,poom'],['11b','keemia','paabo'],['11c','matemaatika','timak'],['11d','kirjandus','mandri,tepp'],['11e','kirjandus','soodla'],['12a','ajalugu','punga'],['12b','matemaatika','kiisel'],['12c','matemaatika','orav'],['12d','usundiõpetus','schihalejev'],['12e','fyysika','paaver']],
                       2: [['10a','A_keel_inglise', 'köhler,(hildebrandt,hunt,ojaveer)'], ['10b', 'kirjandus', 'piirimäe'], ['10c', 'keemia', 'paabo'], ['10d', 'C_keel_prantsuse_saksa', 'Niitvägi,Matto'],['10e', 'A_keel_inglise', 'köhler,(hildebrandt,hunt,ojaveer)'], ['11a','kirjandus', 'soodla'],['11b','kirjandus','mandri,tepp'],['11c','kirjandus','pluum'],['11d','matemaatika','timak'],['11e','matemaatika','orav'],['12a','fyysika', 'oks'],['12b','kehaline','saarva,poom'],['12c','ajalugu','punga'],['12d','fyysika','paaver'],['12e','usundiõpetus','schihalejev']],
                       3: [['10a','kirjandus', 'lummo,tepp'], ['10b','matemaatika','timak'], ['10c', 'matemaatika','kiisel'], ['10d', 'eesti keel', 'piirimäe'], ['10e', 'geograafia', 'seevri'], ['11a','keemia', 'paabo'],['11b','A_keel_inglise', '(Hildebrandt,Ojaveer,Roostoja),Rootsi'],['11c','B_keel_vene_pr_saksa,A_keel_inglise', '(Hildebrandt,Ojaveer,Roostoja);L_Titova'],['11d','A_keel_inglise', '(Hildebrandt,Ojaveer,Roostoja),Köhler'],['11e','B_keel_vene,informaatika', 'O_Titova;Mägi'],['12a','ühiskonnaõpetus', 'ristikivi'],['12b','ajalugu','punga'],['12c','fyysika','oks'],['12d','filosoofia','paaver'],['12e','kirjandus','pluum']],
					   4: [['10a','matemaatika', 'timak'], ['10b', 'geograafia', 'seevri'], ['10c', 'kirjandus','lummo,tepp'], ['10d', 'matemaatika', 'kiisel'], ['10e', 'kehaline', 'saarva,poom'], ['11a','joonestamine_matemaatika', 'lepiste,mägi'],['11b','B_keel_vene_pr_saksa', '(Matto,Roots,L_Titova,O_Titova)'],['11c','B_keel_vene_pr_saksa,A_keel_inglise', '(Matto,Roots,O_Titova);Hunt'],['11d','B_keel_vene_pr_saksa','(Matto,Roots,L_Titova,O_Titova)'],['11e','fyysika','paaver'],['12b','kirjandus','piirimäe'],['12c','keemia','paabo'],['12d','ühiskonnaõpetus','ristikivi'],['12e','ajalugu','punga']]},
		     'day4': {1: [['10a','matemaatika', 'timak'],['10b', 'informaatika,B_keel_vene_pr_saksa', 'mägi;L_Titova'], ['10c', 'keemia','paabo'], ['10d', 'muusika', 'keerberg'], ['10e', 'matemaatika', 'kiisel'], ['11a','fyysika','reemann'],['11b','matemaatika','hüva'],['11c','ajalugu','pettai'],['11d','kirjandus','mandri,tepp'],['11e','matemaatika','orav'],['12a','ajalugu','punga'],['12b','bioloogia','kaarna'],['12c','kehaline','saarva,poom'],['12d','usundiõpetus','schihalejev'],['12e','kirjandus','pluum']],
                       2: [['10a','geograafia', 'seevri'], ['10b', 'informaatika,A_keel_inglise', 'mägi;(köhler,hildebrandt,hunt)'], ['10c',  'B_keel_vene_pr_saksa,A_keel_inglise', 'L_Titova;(köhler,hildebrandt,hunt)'], ['10d', 'B_keel_vene_pr_saksa,A_keel_inglise', 'O_Titova;(köhler,hildebrandt,hunt)'], ['10e', 'ajalugu','pettai'], ['11a','mat_fys_pr', 'reemann,hüva'],['11b','kirjandus','mandri,tepp'],['11c','kirjandus','pluum'],['11d','matemaatika','timak'],['11e','bioloogia','kaarna'],['12a','kehaline','saarva,poom'],['12b','matemaatika','kiisel'],['12c','kirjandus','soodla'],['12d','matemaatika','orav'],['12e','usundiõpetus','schihalejev']],
                       3: [['10a','A_keel_inglise', 'köhler,(hildebrandt,hunt,ojaveer)'],  ['10b', 'geograafia', 'seevri'], ['10c', 'matemaatika','kiisel'],['10d', 'C_keel_prantsuse_saksa', 'Niitvägi,Matto'], ['10e', 'A_keel_inglise', 'köhler,(hildebrandt,hunt,ojaveer)'], ['11a','mat_fys_pr', 'reemann,hüva'],['11b','ajalugu','pettai'],['11c','matemaatika','timak'],['11d','kehaline','saarva,poom'],['11e','B_keel_vene,informaatika', 'O_Titova;Mägi'],['12a','kirjandus','pluum'],['12b','ajalugu','punga'],['12c','matemaatika','orav'],['12d','bioloogia','kaarna'],['12e','muusika','keerberg']],
					   4: [['10a','muusika', 'keerberg'], ['10b', 'mat_fys_pr','timak,reemann'], ['10c', 'bioloogia','kaarna'], ['10d', 'geograafia', 'seevri'], ['10e', 'kirjandus','pluum'], ['11a','joonestamine_informaatika','lepiste,mägi'],['11b','B_keel_vene_pr_saksa', '(Matto,Roots,L_Titova,O_Titova)'],['11c','B_keel_vene_pr_saksa,A_keel_inglise', '(Matto,Roots,O_Titova);Hunt'],['11d','B_keel_vene_pr_saksa','(Matto,Roots,L_Titova,O_Titova)'],['11e','kehaline','saarva,poom'],['12a','matemaatika','hüva'],['12b','matemaatika','kiisel'],['12c','ajalugu','punga'],['12d','kirjandus','soodla'],['12e','matemaatika','orav']]},
			 'day5': {1: [['10a','muusika', 'keerberg'],['10b','informaatika,B_keel_vene_pr_saksa', 'mägi;L_Titova'], ['10c', 'kehaline','saarva,poom'], ['10d', 'matemaatika', 'kiisel'], ['10e', 'kunst','beier'], ['11a','A_keel_inglise', '(Hunt,Köhler,Ojaveer,Roostoja)'],['11b','matemaatika','hüva'],['11c','ajalugu','pettai'],['11d','matemaatika','timak'],['11e','A_keel_inglise', '(Hunt,Köhler,Ojaveer,Roostoja)'],['12a','fyysika','oks'],['12b','bioloogia','kaarna'],['12c','kirjandus','soodla'],['12d','matemaatika','orav'],['12e','filosoofia','paaver']],
                       2: [['10a','kirjandus', 'lummo,tepp'], ['10b', 'mat_fys_pr','timak,reemann'], ['10c', 'bioloogia','kaarna'], ['10d', 'kehaline', 'saarva,poom'], ['10e', 'matemaatika','kiisel'], ['11a','matemaatika','hüva'],['11b','A_keel_inglise', '(Hildebrandt,Ojaveer,Roostoja),Rootsi'],['11c','B_keel_vene_pr_saksa,A_keel_inglise', '(Hildebrandt,Ojaveer,Roostoja);L_Titova'],['11d','A_keel_inglise', '(Hildebrandt,Ojaveer,Roostoja),Köhler'],['11e','muusika','keerberg'],['12a','ühiskonnaõpetus','ristikivi'],['12b','kirjandus','piirimäe'],['12c','fyysika','oks'],['12d','kirjandus','soodla'],['12e','matemaatika','orav']],
                       3: [['10a','A_keel_inglise', 'köhler,(hildebrandt,hunt,ojaveer)'],['10b','matemaatika','timak'], ['10c', 'matemaatika','kiisel'], ['10d', 'eesti keel', 'piirimäe'], ['10e','A_keel_inglise', 'köhler,(hildebrandt,hunt,ojaveer)'], ['11a','kirjandus','soodla'],['11b','kehaline','saarva,poom'],['11c','bioloogia','ustav'],['11d','kunst','beier'],['11e','bioloogia','kaarna'],['12a','mat_fys_pr','oks,hüva'],['12b','fyysika','reemann'],['12c','filosoofia','pettai'],['12d','filosoofia','paaver'],['12e','muusika','keerberg']],
					   4: [['10a','matemaatika', 'timak'], ['10b', 'kirjandus','piirimäe'],['10c', 'kirjandus','lummo,tepp'],['10d', 'muusika', 'keerberg'],['10e', 'ajalugu', 'pettai'], ['11a','joonestamine_informaatika','lepiste,mägi'],['11b','kirjandus','mandri,tepp'],['11d','bioloogia','kaarna'],['11e','kirjandus','soodla'],['12b','mat_fys_pr','kiisel,oks'],['12c','matemaatika','orav'],['12d','ühiskonnaõpetus','ristikivi'],['12e','kehaline','saarva,poom']]}
                  }

def evaluate_result(schedule, optimal_lessons):
    score = 0
    teachers = defaultdict(defaultdict)
    classes = defaultdict(defaultdict)
    for i in schedule:
        for j in schedule[i]:
            for k in schedule[i][j]:
                #print(k)
                sep_teachers = k[2].split(';')
                for x in sep_teachers:
                    for y in x.split(','):
                        teachers[y.lower().strip('()')] = defaultdict(defaultdict)
                classes[k[0]] = defaultdict(defaultdict)
    for i in schedule:
        for j in schedule[i]:
            for k in schedule[i][j]:
                #try:
                sep_teachers = k[2].split(';')
                for x in sep_teachers:
                    for y in x.split(','):
                        try:
                            teachers[y.lower().strip('()')][i].append(int(j))
                        except AttributeError:
                            teachers[y.lower().strip('()')][i] = [int(j)]
                try:
                    classes[k[0]][i].append(int(j))
                except AttributeError:
                    classes[k[0]][i] = [int(j)]
    for i in teachers:
        for j in teachers[i]:
            lessons = sorted(teachers[i][j])
            if len(lessons) > 1:
                for k in range(len(lessons)-1):
                    if lessons[k+1] != lessons[k]:
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

def simulated_anneal(greedy_output,max_lesson, start_T=1.0, alfa=0.9):
    old_cost = evaluate_result(greedy_output,max_lesson)
    T = start_T
    T_min = 0.01
    alpha = alfa
    while T > T_min:
        i = 1
        #print('iter')
        while i <= 100:
            ####choose whichever is currently needed
            #new_solution = permute_whole_slot(greedy_output)
            new_solution = permutewithinteacher(greedy_output)
            #new_solution = permutewithinteacher_nomissingclass(greedy_output)
            new_cost = evaluate_result(new_solution,max_lesson)
            #print(new_cost)
            #print(old_cost)
            ap = acceptprob(old_cost, new_cost, T)
            #print(ap)
            if ap > random.random():
            #    print("test")
                greedy_output = new_solution
                old_cost = new_cost
            i += 1
            #print("iteration")
        T *= alpha
    return greedy_output, old_cost

def permute_whole_slot(anneal_intermed):
    ##take one whole slot and change with another -- confilcts impossible, easiest solution
    firstday = 'dum1'
    secondday = 'dum1'
    firstslot = 'slot1'
    secondslot = 'slot1'
    while firstday == secondday and firstslot == secondslot:
        firstday = 'day' + str(random.randint(1,len(anneal_intermed)))
        firstslot = random.randint(1, len(anneal_intermed[firstday]))
        secondday = 'day' + str(random.randint(1, len(anneal_intermed)))
        secondslot = random.randint(1, len(anneal_intermed[secondday]))
        anneal_intermed[firstday][firstslot],anneal_intermed[secondday][secondslot] = \
            anneal_intermed[secondday][secondslot],anneal_intermed[firstday][firstslot]
    return anneal_intermed

def define_slot(anneal_intermed):
    firstday = 'dum1'
    secondday = 'dum1'
    firstslot = 'slot1'
    secondslot = 'slot1'
    while firstday == secondday and firstslot == secondslot:
        firstday = 'day' + str(random.randint(1, len(anneal_intermed)))
        firstslot = random.randint(1, len(anneal_intermed[firstday]))
        secondday = 'day' + str(random.randint(1, len(anneal_intermed)))
        secondslot = random.randint(1, len(anneal_intermed[secondday]))
    return firstday,firstslot,secondday,secondslot

def permutewithinteacher(anneal_intermed):
    candidates = []
    counter = 0
    emptyslot = False
    while len(candidates) == 0:
        if counter == 30:
            counter = 0
        if counter == 0:
            firstday,firstslot,secondday,secondslot = define_slot(anneal_intermed)
            class_present = True
        try:
            n = random.randint(1, len(anneal_intermed[firstday][firstslot]))
            first_teachers = anneal_intermed[firstday][firstslot][n - 1][2].replace(';', ',').lower().strip('()').split(',')
            first_classes = anneal_intermed[firstday][firstslot][n - 1][0]
            addable = True
            class_present = False
            for i in anneal_intermed[secondday][secondslot]:
                if i[0] == first_classes:
                    class_present = True
                    candidates.append(i)
                for j in i[2].replace(';', ',').lower().strip('()').split(','):
                    if j in first_teachers:
                        addable = False
                if not addable:
                    candidates = []
                    break
            for k in candidates:
                for i in anneal_intermed[firstday][firstslot]:
                        for j in i[2].replace(';', ',').lower().strip('()').split(','):
                            if j in k[2].replace(';', ',').lower().strip('()').split(','):
                                try:
                                    candidates.remove(k)
                                except ValueError:
                                    pass
            if not class_present:
                for i in anneal_intermed[secondday][secondslot]:
                    candidates.append(i)
                    for j in i[2].replace(';', ',').lower().strip('()').split(','):
                        if j in first_teachers:
                            addable = False
                    if not addable:
                        candidates = []
                        break
        except ValueError:
            n = random.randint(1, len(anneal_intermed[secondday][secondslot]))
            candidates = [anneal_intermed[secondday][secondslot][n-1]]
            emptyslot = True
    if emptyslot:
        candidate = random.sample(candidates, 1)
        indeks = anneal_intermed[secondday][secondslot].index(candidate[0])
        anneal_intermed[firstday][firstslot] = candidate[0]
        try:
            anneal_intermed[secondday][secondslot] = anneal_intermed[secondday][secondslot][:indeks] + \
                                                     anneal_intermed[secondday][secondslot][indeks+1:]
        except IndexError:
            anneal_intermed[secondday][secondslot] = anneal_intermed[secondday][secondslot][:indeks]
    elif not class_present:
        anneal_intermed[secondday][secondslot] += [anneal_intermed[firstday][firstslot][n - 1]]
        try:
            anneal_intermed[firstday][firstslot] = anneal_intermed[firstday][firstslot][:n - 1] + \
                                               anneal_intermed[firstday][firstslot][n:]
        except IndexError:
            anneal_intermed[firstday][firstslot] = anneal_intermed[firstday][firstslot][:n - 1]
    else:
        candidate = random.sample(candidates,1)
        indeks = anneal_intermed[secondday][secondslot].index(candidate[0])
        anneal_intermed[firstday][firstslot][n - 1], anneal_intermed[secondday][secondslot][indeks] = \
            anneal_intermed[secondday][secondslot][indeks], anneal_intermed[firstday][firstslot][n - 1]
    return anneal_intermed

def permutewithinteacher_nomissingclass(anneal_intermed):
    candidates = []
    counter = 0
    emptyslot = False
    while len(candidates) == 0:
        if counter == 30:
            counter = 0
        if counter == 0:
            firstday,firstslot,secondday,secondslot = define_slot(anneal_intermed)
        try:
            n = random.randint(1, len(anneal_intermed[firstday][firstslot]))
            first_teachers = anneal_intermed[firstday][firstslot][n - 1][2].replace(';', ',').lower().strip('()').split(',')
            first_classes = anneal_intermed[firstday][firstslot][n - 1][0]
            addable = True
            for i in anneal_intermed[secondday][secondslot]:
                if i[0] == first_classes:
                    candidates.append(i)
                for j in i[2].replace(';', ',').lower().strip('()').split(','):
                    if j in first_teachers:
                        addable = False
                if not addable:
                    candidates = []
                    break
            for k in candidates:
                for i in anneal_intermed[firstday][firstslot]:
                        for j in i[2].replace(';', ',').lower().strip('()').split(','):
                            if j in k[2].replace(';', ',').lower().strip('()').split(','):
                                try:
                                    candidates.remove(k)
                                except ValueError:
                                    pass
        except ValueError:
            n = random.randint(1, len(anneal_intermed[secondday][secondslot]))
            candidates = [anneal_intermed[secondday][secondslot][n-1]]
            emptyslot = True
    if emptyslot:
        candidate = random.sample(candidates, 1)
        indeks = anneal_intermed[secondday][secondslot].index(candidate[0])
        anneal_intermed[firstday][firstslot] = candidate[0]
        try:
            anneal_intermed[secondday][secondslot] = anneal_intermed[secondday][secondslot][:indeks] + \
                                                     anneal_intermed[secondday][secondslot][indeks+1:]
        except IndexError:
            anneal_intermed[secondday][secondslot] = anneal_intermed[secondday][secondslot][:indeks]
    else:
        candidate = random.sample(candidates,1)
        indeks = anneal_intermed[secondday][secondslot].index(candidate[0])
        anneal_intermed[firstday][firstslot][n - 1], anneal_intermed[secondday][secondslot][indeks] = \
            anneal_intermed[secondday][secondslot][indeks], anneal_intermed[firstday][firstslot][n - 1]
    return anneal_intermed

def acceptprob(old_cost, new_cost, T):
    if new_cost < old_cost:
        probability = 1
    else:
        probability = exp(-(new_cost-old_cost)/T)
    return probability


def greedy(lessondata,max_days,max_hours):
    cnt = 0
    innerc = 0
    lessonplan = {}
    random_lesson_keys = list(lessondata.keys())
    shuffle(random_lesson_keys)
    for i in range(max_days):
        lessonplan['day' + str(i+1)] = {}
        max_lessons = []
        for j in range(max_hours):
            lessonplan['day' + str(i+1)][j+1] = []
            for k in random_lesson_keys:
                cnt += 1
                if int(lessondata[k][3]) > 0:
                    toadd = [lessondata[k][0],lessondata[k][1],lessondata[k][2]]
                    addable = True
                    if not [lessondata[k][0],lessondata[k][1]] in max_lessons:
                        for l in lessonplan['day' + str(i+1)][j+1]:
                            innerc += 1
                            #print(l)
                            for a in lessondata[k][0].split(','):
                                #print(a)
                                if a in l[0]:
                                    addable = False
                                    #print('did not fit')
                                    break
                            if addable == False:
                                break
                            for a in lessondata[k][2].strip('()').split(','):
                                if a in l[2]:
                                    addable = False
                                    break
                            if not addable:
                                break
                        if addable:
                            lessonplan['day' + str(i+1)][j+1].append(toadd)
                            max_lessons.append([toadd[0],toadd[1]])
                            lessondata[k][3] = str(int(lessondata[k][3]) - 1)
    for i in range(max_days):
        for j in range(max_hours):
            for k in random_lesson_keys:
                if int(lessondata[k][3]) > 0:
                    toadd = [lessondata[k][0],lessondata[k][1],lessondata[k][2]]
                    addable = True
                    for l in lessonplan['day' + str(i+1)][j+1]:
                        for a in lessondata[k][0].split(','):
                            #print(a)
                            if a in l[0]:
                                addable = False
                                break
                        if not addable:
                            break
                        for a in lessondata[k][2].strip('()').split(','):
                            if a in l[2]:
                                addable = False
                                break
                        if not addable:
                            break
                    if addable:
                        lessonplan['day' + str(i+1)][j+1].append(toadd)
                        lessondata[k][3] = str(int(lessondata[k][3]) - 1)
    test_result = []
    for i in lessondata:
        #print(i)
        #print(lessondata[i])
        if int(lessondata[i][3]) > 0:
            test_result.append(lessondata[i])
    return (lessonplan,test_result)

#print(evaluate_result(reference, 5))
bilbo = []
minimum = 100000


def output_data(output_file, outer_reps, start_reps, inner_reps, annealing_start_T, annealing_factor, optimal_lessons, max_hours):
    dta = []
    print("start")
    for m in range(outer_reps):
        print("Starting-loop")
        minim = 100000
        cur_best, cur_fail = greedy(readlessondata("Algo_Project_data_changed.txt"), 5, max_hours)
        for i in range(start_reps):
            cur, cur_fail = greedy(readlessondata("Algo_Project_data_changed.txt"), 5, max_hours)
            tmp_min = evaluate_result(cur, optimal_lessons)
            if tmp_min < minim and len(cur_fail) == 0:
                minim = tmp_min
                cur_best, cur_fail = cur, cur_fail
        start_min = minim

        for j in range(inner_reps):
            tmp_ref, tmp_new_val = simulated_anneal(cur_best, max_hours, annealing_start_T, annealing_factor)
            if tmp_new_val < minim:
                cur_best, tmp_fail = tmp_ref, cur_fail
                minim = tmp_new_val
        print(str(m) + str(minim))
        dta.append([start_min, minim])

    with open(output_file, "a") as f:
        f.write("----------\n")
        f.write("Parameters are: start_reps:%d, annealing_start_T:%d, annealing_factor:%0.2f \n"
                % (start_reps, annealing_start_T, annealing_factor))
        f.write("Results: %s\n" % str(dta))


for i in range(1000):
    a, ta = greedy(readlessondata("Algo_Project_data_changed.txt"), 5, 5)
    bilbo.append(a)
    #print(evaluate_result(a,5))
    tmp_min = evaluate_result(a, 5)
    if tmp_min < minimum and len(ta) == 0:
        minimum = tmp_min
        minimal = a
        print(minimum)

#print(minimal)
#print(minimum)
#print(minimal)
print(minimum)
#print(evaluate_result(reference,5))
#print(simulated_anneal(reference,5)[1])
#print(evaluate_result(minimal,5))
#print(simulated_anneal(minimal, 5)[1])
#print(minimum)

#output_data(output_file="data.txt", outer_reps=2, start_reps=200, inner_reps=4, annealing_start_T=1.0,
#            annealing_factor=0.85, optimal_lessons=5, max_hours=5)
"""
output_data(output_file="data.txt", outer_reps=3, start_reps=200, inner_reps=4, annealing_start_T=10.0,
            annealing_factor=0.9, optimal_lessons=5, max_hours=5)

output_data(output_file="data.txt", outer_reps=3, start_reps=200, inner_reps=4, annealing_start_T=7.0,
            annealing_factor=0.9, optimal_lessons=5, max_hours=5)

output_data(output_file="data.txt", outer_reps=3, start_reps=200, inner_reps=4, annealing_start_T=5.0,
            annealing_factor=0.9, optimal_lessons=5, max_hours=5)

output_data(output_file="data.txt", outer_reps=3, start_reps=200, inner_reps=4, annealing_start_T=3.0,
            annealing_factor=0.9, optimal_lessons=5, max_hours=5)

output_data(output_file="data.txt", outer_reps=3, start_reps=200, inner_reps=4, annealing_start_T=1.0,
            annealing_factor=0.9, optimal_lessons=5, max_hours=5)

output_data(output_file="data.txt", outer_reps=3, start_reps=200, inner_reps=4, annealing_start_T=0.8,
            annealing_factor=0.9, optimal_lessons=5, max_hours=5)

"""