def array_packing(a):
    return int(''.join([bin(i)[2:].rjust(8,'0') for i in a][::-1]),2)

print(array_packing([24, 85, 0]))


# from sys import maxsize
# from itertools import permutations

# def tsp(graph, s):
# 	vertex = []
# 	for i in range(len(graph)):
# 		if i != s:
# 			vertex.append(i)
# 	min_cost = maxsize
# 	next_permutation=permutations(vertex)
# 	r,q=[],[]
# 	for i in next_permutation:
# 		current_cost = 0
# 		k = s
# 		for j in i:
# 			current_cost += graph[k][j]
# 			k = j
# 		current_cost += graph[k][s]
# 		min_cost = min(min_cost, current_cost)
# 	return r

# print(tsp([
#             [0,343,482,294,452,406,118,68],
#             [343,0,3,129,115,165,45,15],
#             [482,3,0,397,148,488,335,79],
#             [294,129,397,0,32,135,318,310],
#             [452,115,148,32,0,467,70,303],
#             [406,165,488,135,467,0,83,63],
#             [118,45,335,318,70,83,0,421],
#             [68,15,79,310,303,63,421,0]     
#         ],0))