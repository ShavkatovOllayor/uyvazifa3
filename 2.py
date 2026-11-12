
from datetime import datetime

def bugungi_sana():
    return datetime.now().strftime("%Y-%m-%d")


def hozirgi_vaqt():
    return datetime.now().strftime("%H:%M:%S")


def yilni_aniqla(sana):
    sana_obj = datetime.strptime(sana, "%Y-%m-%d")
    return sana_obj.year
