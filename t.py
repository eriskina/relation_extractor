from pymystem3 import Mystem

my = Mystem()

rez = my.analyze("Вся информация о любой вычислимой проблеме может быть представлена с использованием только 0 и 1. Теперь рассмотрим еще один метод выделения - через ключевое поле. Этот метод лучше подходит, если у вас реализована сортировка.")

rels = []
ob1 = ''
ob2 = ''
rel = ''
for token in rez:
    try:
        if token['analysis'][0]['gr'].split(',')[0] == 'V':
            # print(token['analysis'][0]['lex'])
            rel += "%s " % token['analysis'][0]['lex']
        elif token['analysis'][0]['gr'].split(',')[0] == 'S':
            ob1 += "%s " % token['analysis'][0]['lex']
        else:
            ob2 += "%s " % token['analysis'][0]['lex']
    except:
        pass

    print(token)
    if token['text'].strip() == '.':
        if strad:
            rels += [{'rel':rel.strip(), 'sub':ob2.strip(), 'ob':ob1.strip()}]
        else:
            rels += [{'rel':rel.strip(), 'sub':ob1.strip(), 'ob':ob2.strip()}]
        rel = ''
        sub = ''
        ob = ''
print(rels)



#for lex in token:
    #try:
        #if lex  == ' ':
                #if token['text'][0](',')['analysis'][0]['lex'].split(',')[0] == ' ':
                    #print(token['analysis'][0]['lex'])
    #except:
        #pass
