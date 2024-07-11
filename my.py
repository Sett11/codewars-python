def obfuscate(s):
    return s.replace('.',' [dot] ').replace('@',' [at] ')

print(obfuscate('Code_warrior@foo.ac.uk'))