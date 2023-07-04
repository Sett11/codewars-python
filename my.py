def difference_in_ages(a):
    b,c=min(a),max(a)
    return (b,c,c-b)

print(difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88]))