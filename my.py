def pillow(s):
    return any(s[1][k]=='B' for k in [i for i,j in enumerate(s[0]) if j=='n'])

print(pillow(['yF[CeAAiNihWEmKxJc/NRMVn', 'rMeIa\\KAfbjuLiTnAQxNw[XB']))