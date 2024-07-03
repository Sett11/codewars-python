def max_sum(a,r): 
    return max(sum(a[i:j+1]) for i,j in r)

print(max_sum([1,-2,3,4,-5,-4,3,2,1], [[1,4],[2,5]]))