#!usr/bin/python3
# -*- coding: utf-8 -*-

from lingv import *

my = Mystem()

with open('test.txt','r', encoding="utf-8") as f:
    string = [line.rstrip(r'\S*[\w]') for line in f][1]

class HierarchyBuilder(object):
    # def __init__(self):
    #     self.analysis = analysis

    def build(self, analysis):
        pos = set(re.findall(r"^([A-Z]+).+", analysis[0]['gr']))
        if "S" in pos:
            return Существительное(analysis)
        if "A" in pos:
            return Прилагательное(analysis)
        if "NUM" in pos:
            return Числительное(analysis)
        if "V" in pos:
            return Глагол(analysis)
        if "ADV" in pos:
            return Наречие(analysis)
        if "PRO" in pos:
            return Местоимение(analysis)
        if "CONJ" in pos:
            return Союз(analysis)
        if "INTJ" in pos:
            return Междометие(analysis)
        if "PR" in pos:
            return Предлог(analysis)
        if "PART" in pos:
            return Частица(analysis)


hb = HierarchyBuilder()
for a in my.analyze(string):
    try:
        x = hb.build(a['analysis'])
        if x is not None:
            print(x, x.pos)
            if isinstance(x, Существительное):
                print(x.падеж, x.род, x.число)
            elif isinstance(x, Глагол):
                print(x.время, x.залог, x.лицо, x.наклонение)
    except KeyError:
        pass
