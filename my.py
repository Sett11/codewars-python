def small_word_helper(s):
    return ' '.join(i.upper() if len(i)<4 else ''.join(j if j.lower() not in 'aouie' else '' for  j in i) for i in s.split())

print(small_word_helper("The quick brown fox jumps over the lazy dog"))
print(small_word_helper("I'm just a small word from a small word family"))