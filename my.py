from re import sub,IGNORECASE

def remove_bmw(s):
    try:return sub(r'[bmw]','',s,flags=IGNORECASE)
    except:raise(TypeError("This program only works for text."))

print(remove_bmw("bmwvolvoBMW"))
print(remove_bmw(0))