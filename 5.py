
import random

def son_yarat(minimum, maksimum):
    return random.randint(minimum, maksimum)


def tekshir(taxmin, sirli_son):
    if taxmin == sirli_son:
        return "To'g'ri topdingiz!"
    elif taxmin < sirli_son:
        return "Kattaroq son kiriting!"
    else:
        return "Kichikroq son kiriting!"
