import os
import touch

direct =os.getcwd()


#touch.touch("success.java")



def check(next,yourpath):
    if next == 'cd':
        return os.chdir(os.path.abspath(os.path.join(yourpath, os.pardir)))

    if next[:2] == 'cd' and len(next) > 2:
        if os.path.exists(next[3:]):
            return os.chdir(next[3:])

    if next == 'ls':
        ls = os.listdir()
        ls = list(set(ls))
        rls = []
        for el in ls:
            rls += ls
        rls = list(set(rls))
        for el in rls:
            if rls.index(el) != len(rls)-1:
                print(el,end = ' ; ')
            else:
                print(el)


    if next[:5] == 'touch' and len(next) > 5:
        try:
            touch.touch(next[6:])
        except:
            print("This File Could Not Be Made")

    if next[:3] == 'rmv' and len(next) > 3:
        if os.path.exists(next[4:]):
            os.remove(next[4:])

    return None

while True:
    direct = os.getcwd()
    print()
    next = input(direct+str(':~$ '))
    check(next,direct)
