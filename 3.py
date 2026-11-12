
def soz_qosh(lugat, soz, tarjima):
    lugat[soz] = tarjima


def soz_qidir(lugat, soz):
    return lugat.get(soz, "Bu so'z lug'atda mavjud emas!")


def lugatni_kor(lugat):
    for soz, tarjima in lugat.items():
        print(soz, "-", tarjima)
