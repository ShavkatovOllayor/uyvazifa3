import random
import string

def parol_yarat(uzunlik):
    belgilar = string.ascii_letters + string.digits + string.punctuation
    parol = ""

    for i in range(uzunlik):
        parol += random.choice(belgilar)

    return parol


def parol_tekshir(parol):
    if len(parol) >= 8:
        return True
    else:
        return False
