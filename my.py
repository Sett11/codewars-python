def leader_b(user, user_score, your_score):
    if user_score<your_score:
        return 'Winning!'
    if user_score==your_score:
        return "Only need one!"
    a,b=divmod(user_score-your_score,3)
    return "To beat {}'s score, I must complete {} Beta kata and {} 8kyu kata.{}".format(user,a,b,' Dammit!' if a+b>1000 else '')

print(leader_b('g964', 36097, 20000))