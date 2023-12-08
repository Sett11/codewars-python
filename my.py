def middle_permutation(s):
    n,s=len(s),sorted(s)
    return s.pop(n//2-1)+''.join(s[::-1]) if n%2==0 else s.pop(n//2)+middle_permutation(s)

print(middle_permutation('gbmaxjztldn'))