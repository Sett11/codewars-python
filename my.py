def mobile_keyboard(s):
    a=['1','2abc','3def','4ghi','5jkl','6mno','7pqrs','8tuv','9wxyz','*','0','#']
    return sum([j.index(i)+1 for i in s for j in a if i in j])

print(mobile_keyboard('codewars'))