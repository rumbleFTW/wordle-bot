def corrPosFilter(dB: list, info: dict):                                                #correct position filter
    if len(info) == 0:
        return dB
    res = list()
    if len(info) == 0:
       res = dB
    for item in dB:
        legal = True
        for letter in info:
            if(item[info[letter]] != letter):
                legal = False    
        if legal:
            res.append(item)
    return res

def wrongPosFilter(dB: list, info: dict):                                               #wrong position filter
    res = []
    for item in dB:
        legal = True
        for letter in info:
            if item[info[letter]] == letter:
                legal = False
                break
        if legal:
            res.append(item)
    return res

def absFilter(dB: list, info: list):                                                    #absent filter
    res = []
    for item in dB:
        flag = True
        for letter in info:
            if letter in item:
                flag = False
                break
        if flag:
            res.append(item)
    return res

def presFilter(dB:list, info:list):                                                     #present filter
    res = []
    for item in dB:
        flag = True
        for letter in info:
            if letter not in item:
                flag = False
                break
        if flag:
            res.append(item)
    return res