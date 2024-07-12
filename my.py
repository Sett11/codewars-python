from string import ascii_lowercase as a

def solve(s):
    return all(abs(a.index(s[i])-a.index(s[-i-1])) in [0,2] for i in range(len(s)//2))

print(solve('ceb'))
print(solve('kxbkwgyydkcbtjcosgikfdyhuuprubpwthgflucpyylbofvqxkkvqthmdnywpaunfihvupbwpruwfybdmgeuocltdaidyyewmbzm'))