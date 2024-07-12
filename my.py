trigrams=lambda s:' '.join(s[i:i+3].replace(' ','_') for i in range(len(s)-2))


print(trigrams('the quick red'))