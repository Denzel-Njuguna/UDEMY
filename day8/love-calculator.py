search = ["true","love"]

def check1(name1,TRUE,LOVE):
    for each in name1:
        if each in search[0]:
            TRUE+=1
        if each in search[1]:
            LOVE+=1
    return TRUE,LOVE 
def check2(name2,TRUE,LOVE):
    for letter in name2:
        if letter in search[0]:
            TRUE+=1
        if letter in search[1]:
            LOVE+=1
    return TRUE,LOVE

def calculate_love_score(name1, name2):
    TRUE = 0
    LOVE = 0
    TRUE,LOVE = check1(name1,TRUE,LOVE)
    TRUE,LOVE = check2(name2,TRUE,LOVE)
    return ''.join([str(TRUE),str(LOVE)])
result = calculate_love_score(name1="lover",name2="lover")
print(result)