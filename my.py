# def solve(n): 
#     return list(map(int,str(n)))[::-1]

# print(solve(45))


def whac_a_mole(arr):
    a,c=sorted(sum(arr,[]),reverse=True),0
    def f(a):
        while a[-1]<1:
            a.pop()
            if not a:
                return
    while a:
        for _ in range(2):
            f(a)
            if not a:
                break
            a.pop()
            c+=1
            if not a:
                break
        a=[i-1 for i in a]
    return c


print(whac_a_mole([
            [1, 1, 2, 2],
            [3, 3, 4, 4],
            [4, 8, 8, 8]
        ]))
print(whac_a_mole([
            [6, 4, 1, 1],
            [4, 4, 4, 4],
            [1, 2, 3, 3]
        ]))