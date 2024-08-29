# from math import log

# def li(x,n=100):
#     if x<2:
#         return float('nan')
#     step=(x-2)/n
#     integral=.0
#     for i in range(n):
#         t1,t2=2+i*step,2+(i+1)*step
#         if t1>0 and t2>0:
#             integral+=(1/log(t1)+1/log(t2))*step/2
#     return integral

# print(li(10000))

from re import compile

def change(s,p,v):
  a=s.splitlines()
  for i in range(len(a)):
    if 'Corporation' in a[i] or 'Level' in a[i]:
      a[i]=''
    elif a[i].startswith('Program'):
      a[i]=f'Program: {p}'
    elif a[i].startswith('Author'):
      a[i]='Author: g964'
    elif a[i].startswith('Date'):
      a[i]='Date: 2019-01-01'
    elif a[i].startswith('Version'):
      t=a[i].split()
      if compile(r'\A\d+\.\d+\Z').search(t[1]):
        if t[1]!='2.0':
          a[i]=f'Version: {v}'
      else:
        return 'ERROR: VERSION or PHONE'
    elif a[i].startswith('Phone'):
      if compile(r'\A\+1\-\d{3,3}\-\d{3,3}-\d{4,4}\Z').search(a[i].split()[1]):
        a[i]='Phone: +1-503-555-0090'
      else:
        return 'ERROR: VERSION or PHONE'
  return ' '.join(filter(bool,a))

print(change('Program title: Primes\nAuthor: Kern\nCorporation: Gold\nPhone: +1-503-555-0091\nDate: Tues April 9, 2005\nVersion: 6.7\nLevel: Alpha','Balance', '1.5.6'))