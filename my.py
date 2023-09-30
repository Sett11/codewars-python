def unusual_lex_order(a):
    return sorted(a,key=lambda e:e[::-1])

print(unusual_lex_order(["nigeb", "ta", "eht", "gninnigeb"]))