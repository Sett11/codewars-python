from itertools import groupby as g

slot=lambda s:{(5,):1000,(1,4):800,(2,3):500,(1,1,3):300,(1,2,2):200,(1,1,1,2):100}.get(tuple(sorted(len(list(j)) for _,j in g(s))),0)

print(slot('!!!!!'))
print(slot('!!!!?'))
print(slot('!!!??'))
print(slot('!!!?!'))
print(slot('??!!?'))
print(slot('?!??!'))