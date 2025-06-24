def countdown(n):
    v, t = n < 0, abs(n)
    s = t / 1000
    h = s // 3600
    rs = s % 3600
    m = rs // 60
    sec = rs % 60
    return f"{'-' if v else '+'}{str(int(h)).rjust(2,'0')}:{str(int(m)).rjust(2, '0')}:{str(int(sec)).rjust(2,'0')}"

print(countdown(-154800000))
print(countdown(61000))