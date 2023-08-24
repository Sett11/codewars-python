import re


def is_valid_HK_phone_number(s):
    s = s.split(' ')
    return True if s[0].isdigit() and len(s[0]) == 4 and s[-1].isdigit() and len(s[-1]) == 4 and len(s) == 2 else False


def has_valid_HK_phone_number(s):
    s = re.sub(r'[^\d ]', ' ', s).split(' ')
    for i in range(len(s)):
        if i == len(s)-1:
            return False
        if s[i].isdigit() and len(s[i][:4]) == 4 and s[i+1].isdigit() and len(s[i+1][:4]) == 4:
            return True
    return False


print(is_valid_HK_phone_number("1234 5678"))
print(is_valid_HK_phone_number("1234  5678"))
print(is_valid_HK_phone_number("123f 5678"))
print(is_valid_HK_phone_number("123 5678"))
print(has_valid_HK_phone_number("Hello, my phone number is 1234 5678"))
print(has_valid_HK_phone_number("ceanjgz1z3114 825d9j/6yh"))
print(has_valid_HK_phone_number("skldfjs287389274329dklfj84239029043820942904823480924293042904820482409209438dslfdjs9345 8234sdklfjsdkfjskl28394723987jsfss2343242kldjf23423423SDLKFJSLKsdklf"))
