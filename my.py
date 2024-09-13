from statistics import mean,median

def hand(n):
    h,n=divmod(n,3600)
    m,n=divmod(n,60)
    return '|'.join([str(int(h)).rjust(2,'0'),str(int(m)).rjust(2,'0'),str(int(n)).rjust(2,'0')])

def stat(s):
    if not s:
        return ''
    a=sorted([k[0]*3600+k[1]*60+k[2] for k in [[int(j) for j in i.split('|')] for i in s.split(', ')]])
    return f"Range: {hand(a[-1]-a[0])} Average: {hand(mean(a))} Median: {hand(median(a))}"

print(stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"))