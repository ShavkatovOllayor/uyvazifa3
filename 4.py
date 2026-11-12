
def baho_aniqla(ball):
    if 90 <= ball <= 100:
        return "A'lo"
    elif 70 <= ball < 90:
        return "Yaxshi"
    elif 50 <= ball < 70:
        return "Qoniqarli"
    elif 0 <= ball < 50:
        return "Qoniqarsiz"
    else:
        return "Noto'g'ri ball!"


def ortacha_hisobla(balllar):
    return sum(balllar) / len(balllar)


def eng_yaxshi_ball(balllar):
    return max(balllar)
