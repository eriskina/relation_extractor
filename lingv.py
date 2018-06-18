from pymystem3 import Mystem
import re
import sys

m = Mystem()
EMPTY = set()

class Cлово():
    def __init__(self, analysis):
        try:
            # {'text': 'мне', 'analysis': [{'gr': 'SPRO,ед,1-л=(пр|дат)', 'lex': 'я'}]}
            self.word = analysis[0]['lex']
            self.analysis = analysis[0]['gr']
            self.type = set(re.findall(r"^([A-Z]+).+", self.analysis))
            try:
                self.падеж = Падеж(set([x for x in re.findall(r".*((им,)|(род,)|(дат,)|(вин,)|(твор,)|(пр,)|(парт,)|(местн,)|(зват,)).*", self.analysis)[0] if x ]))
            except IndexError:
                self.падеж = None
            #print (re.findall(r".*((деепр)|(инф)|(прич)|(изъяв)|(пов)).*", self.analysis), self.analysis)
            try:
                self.наклонение = Наклонение(set([x for x in re.findall(r".*((деепр)|(инф)|(прич)|(изъяв)|(пов)).*", self.analysis)[0] if x ]))
            except IndexError:
                self.наклонение = None
            try:
                self.залог = Залог(set([x for x in re.findall(r".*((действ)|(страд)).*", self.analysis)[0] if x ]))
            except IndexError:
                self.залог = None
            #print (66666, re.findall(r".*((им,)|(род,)|(дат,)|(вин,)|(твор,)|(пр,)|(парт,)|(местн,)|(зват,)).*", self.analysis))
            print()
        except (IndexError, KeyError):
            print(analysis)
            raise KeyError

    def __eq__(self, obj):
        #print(obj.__class__, self.__class__, 111111111111, file = sys.stderr)
        if self.__class__ in [Существительное,Прилагательное,Глагол,Наречие,Местоимение,Междометие,Союз,Частица,Числительное,Предлог,Падеж,Наклонение,Залог]:
            #print(111111111111, file = sys.stderr)
            return (self.type & obj.type) != EMPTY
        else:
            return False

    def __repr__(self):
        return "%s %s %s %s" % (self.word, self.падеж, self.наклонение, self.залог)

class Существительное(Cлово):
    def __init__(self):
        self.type = {'S'}

class Прилагательное(Cлово):
    def __init__(self):
        self.type = {'A'}

class Глагол(Cлово):
    def __init__(self):
        self.type = {'V'}

class Наречие(Cлово):
    def __init__(self):
        self.type = {'ADV'}

class Местоимение(Cлово):
    def __init__(self):
        self.type = {'ADVPRO','APRO','SPRO'}

class Числительное(Cлово):
    def __init__(self):
        self.type = {'ANUM','NUM'}

class Союз(Cлово):
    def __init__(self):
        self.type = {'CONJ'}

class Междометие(Cлово):
    def __init__(self):
        self.type = {'INTJ'}

class Предлог(Cлово):
    def __init__(self):
        self.type = {'PR'}

class Частица(Cлово):
    def __init__(self):
        self.type = {'PART'}

class Падеж():
    def __init__(self, x):
        self.type = x

    def __repr__(self):
        return str(self.type)

class Именительный(Падеж):
    def __init__(self):
        self.падеж = {'им,'}

class Родительный(Падеж):
    def __init__(self):
        self.падеж = {'род,'}

class Дательный(Падеж):
    def __init__(self):
        self.падеж = {'дат,'}

class Винительный(Падеж):
    def __init__(self):
        self.падеж = {'вин,'}

class Творительный(Падеж):
    def __init__(self):
        self.падеж = {'твор,'}

class Предложный(Падеж):
    def __init__(self):
        self.падеж = {'пр,'}

class Партитив(Падеж):
    def __init__(self):
        self.падеж = {'парт,'}

class Местный(Падеж):
    def __init__(self):
        self.падеж = {'местн,'}

class Звательный(Падеж):
    def __init__(self):
        self.падеж = {'зват,'}

class Наклонение():
    def __init__(self, x):
        self.type = x

    def __repr__(self):
        return str(self.type)

class Деепричастие(Наклонение):
    def __init__(self):
        self.наклонение = {'деепр'}

class Инфинитив(Наклонение):
    def __init__(self):
        self.наклонение = {'инф'}

class Причастие(Наклонение):
    def __init__(self):
        self.наклонение = {'прич'}

class Изъявительное(Наклонение):
    def __init__(self):
        self.наклонение = {'изъяв'}

class Повелительное(Наклонение):
    def __init__(self):
        self.наклонение = {'пов'}

class Залог():
    def __init__(self, x):
        self.type = x

    def __repr__(self):
        return str(self.type)

class Действительный(Залог):
    def __init__(self):
        self.залог = {'действ'}

class Страдательный(Залог):
    def __init__(self):
        self.залог = {'страд'}
