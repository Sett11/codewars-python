def letter_pattern(a):
    return ''.join('*' if len(set(i))>1 else i[0] for i in zip(*a))

print(letter_pattern(['war', 'rad', 'dad']))