from lingv import *

my = Mystem()

with open('test.txt','r') as f:
    str = [line.rstrip(r'\S*[\w]') for line in f][0]

for a in my.analyze(str):
    try:
        x = Cлово(a['analysis'])
        for y in [Существительное, Глагол, Прилагательное, Наречие]:
            if x == y():
                print(x)
    except KeyError:
        pass
