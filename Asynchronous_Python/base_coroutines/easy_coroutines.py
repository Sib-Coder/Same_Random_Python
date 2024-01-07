def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner



def subgen():
    x = 'Ready to message'
    message = yield x
    print('Subgen received: ', message)

class BlablaEx(Exception):
    pass


@coroutine
def avarege():
    count = 0
    summ =0
    avarege = None
    while True:
        try:
            x = yield avarege
        except StopIteration:
            print("Done!")
        except BlablaEx:
            print("____________________________________EX_____________________________________")
        else:
            count+=1
            summ+=x
            avarege= round(summ /count,2)

#######################STOP ON 14:00 https://www.youtube.com/watch?v=5SyA3lsO_hQ