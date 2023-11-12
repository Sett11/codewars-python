def unscramble(s):
    return [i for i in word_list if sorted(i)==sorted(s)]