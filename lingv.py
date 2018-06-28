#!usr/bin/python3
# -*- coding: utf-8 -*-

from pymystem3 import Mystem
import re
import sys

# m = Mystem()
EMPTY = set()

class Cлово():  # Word / Lexeme
    def __init__(self, analysis):
        try:
            # {'text': 'мне', 'analysis': [{'gr': 'SPRO,ед,1-л=(пр|дат)', 'lex': 'я'}]}
            self.lemma = analysis[0]['lex']
            self.analysis = analysis[0]['gr']
            self.pos = set(re.findall(r"^([A-Z]+).+", self.analysis))
        except (IndexError, KeyError):
            print(analysis)
            raise KeyError

    def __eq__(self, obj):
        if self.__class__ in [Существительное,Прилагательное,Числительное,Глагол,Наречие,Местоимение,Междометие,Союз,Частица,Предлог]:
            return (self.pos & obj.type) != EMPTY
        else:
            return False

    def __repr__(self):
        return "%s" % (self.lemma)

class Имя(Cлово):  # Noun / Nomen
    def __init__(self, analysis):
        super(Имя, self).__init__(analysis)
        try:
            self.падеж = set([x for x in re.findall(r".*((им,)|(род,)|(дат,)|(вин,)|(твор,)|(пр,)|(парт,)|(местн,)|(зват,)).*", self.analysis)[0] if x ])  # Case
        except IndexError:
            self.падеж = None
        try:
            self.род = set([x for x in re.findall(r".*((муж)|(жен)|(сред)).*", self.analysis)[0] if x ])  # Gender
        except IndexError:
            self.род = None
        try:
            self.число = set([x for x in re.findall(r".*((ед)|(мн)).*", self.analysis)[0] if x ])  # Number
        except IndexError:
            self.число = None

class Существительное(Имя):  # Substantive
    def __init__(self, analysis):
        super(Существительное, self).__init__(analysis)
        self.pos = {'S'}

class Прилагательное(Имя): # Adjective
    def __init__(self, analysis):
        super(Прилагательное, self).__init__(analysis)
        self.pos = {'A'}

class Числительное(Имя):  # Numeral
    def __init__(self, analysis):
        super(Числительное, self).__init__(analysis)
        self.pos = {'ANUM','NUM'}

class Глагол(Cлово):  # Verb
    def __init__(self, analysis):
        super(Глагол, self).__init__(analysis)
        self.pos = {'V'}
        try:
            self.наклонение = set([x for x in re.findall(r".*((деепр)|(инф)|(прич)|(изъяв)|(пов)).*", self.analysis)[0] if x ])  # Mode / Mood
            # деепричастие, причастие и инфинитив в наклонение? с т.з. лингвистики это грубая ошибка. 
            # в доках майстема эта группа граммем называется "репрезентация и наклонение", мб лучше поставить везде репрезентацию 
        except IndexError:
            self.наклонение = None
        try:
            self.залог = set([x for x in re.findall(r".*((действ)|(страд)).*", self.analysis)[0] if x ])  # Voice / Diathesis
        except IndexError:
            self.залог = None
        try:
            self.время = set([x for x in re.findall(r".*((наст)|(непрош)|(прош)).*", self.analysis)[0] if x ])  # Tense
        except IndexError:
            self.время = None
        try:
            self.лицо = set([x for x in re.findall(r".*((1-л)|(2-л)|(3-л)).*", self.analysis)[0] if x ])  # Person
        except IndexError:
            self.лицо = None

class Наречие(Cлово):  # Adverb
    def __init__(self, analysis):
        super(Наречие, self).__init__(analysis)
        self.pos = {'ADV'}

class Местоимение(Cлово):  # Pronoun
    def __init__(self, analysis):
        super(Местоимение, self).__init__(analysis)
        self.pos = {'ADVPRO','APRO','SPRO'}
        # на подумать: если майстем разделяет местоимения (сущ, прил, наречные), можно в теории отнаследовать еще 3 класса
        # лично мне кажется это пока избыточным, правда

class Союз(Cлово):  # Conjunction
    def __init__(self, analysis):
        super(Союз, self).__init__(analysis)
        self.pos = {'CONJ'}

class Междометие(Cлово):  # Interjection
    def __init__(self, analysis):
        super(Междометие, self).__init__(analysis)
        self.pos = {'INTJ'}

class Предлог(Cлово):  # Preposition
    def __init__(self, analysis):
        super(Предлог, self).__init__(analysis)
        self.pos = {'PR'}

class Частица(Cлово):  # Particle
    def __init__(self, analysis):
        super(Частица, self).__init__(analysis)
        self.pos = {'PART'}

# class Падеж():
#     def __init__(self, x):
#         self.type = x

#     def __repr__(self):
#         return str(self.type)

# class Именительный(Падеж):
#     def __init__(self):
#         self.падеж = {'им,'}

# class Родительный(Падеж):
#     def __init__(self):
#         self.падеж = {'род,'}

# class Дательный(Падеж):
#     def __init__(self):
#         self.падеж = {'дат,'}

# class Винительный(Падеж):
#     def __init__(self):
#         self.падеж = {'вин,'}

# class Творительный(Падеж):
#     def __init__(self):
#         self.падеж = {'твор,'}

# class Предложный(Падеж):
#     def __init__(self):
#         self.падеж = {'пр,'}

# class Партитив(Падеж):
#     def __init__(self):
#         self.падеж = {'парт,'}

# class Местный(Падеж):
#     def __init__(self):
#         self.падеж = {'местн,'}

# class Звательный(Падеж):
#     def __init__(self):
#         self.падеж = {'зват,'}

# class Наклонение():
#     def __init__(self, x):
#         self.type = x

#     def __repr__(self):
#         return str(self.type)

# class Деепричастие(Наклонение):
#     def __init__(self):
#         self.наклонение = {'деепр'}

# class Инфинитив(Наклонение):
#     def __init__(self):
#         self.наклонение = {'инф'}

# class Причастие(Наклонение):
#     def __init__(self):
#         self.наклонение = {'прич'}

# class Изъявительное(Наклонение):
#     def __init__(self):
#         self.наклонение = {'изъяв'}

# class Повелительное(Наклонение):
#     def __init__(self):
#         self.наклонение = {'пов'}

# class Залог():
#     def __init__(self, x):
#         self.type = x

#     def __repr__(self):
#         return str(self.type)

# class Действительный(Залог):
#     def __init__(self):
#         self.залог = {'действ'}

# class Страдательный(Залог):
#     def __init__(self):
#         self.залог = {'страд'}
