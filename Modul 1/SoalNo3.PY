#No3 A
def jmlVokal(string):
    vok = 0
    x = "aiueoAIUEO"
    for car in string.lower():
        if car in x:
            vok += 1
    vokal = len(string)
    return(vokal,vok)

#No3 B
def jmlVokal2(string):
    vok = 0
    x = "aiueoAIUEO"
    for car in string.lower():
        if car not in x:
            vok += 1
    vokal = len(string)
    return(vokal,vok)
