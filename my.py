def sort_reindeer(a):
    return sorted(a,key=lambda x:x.split(' ')[1])

print(sort_reindeer([
  "Dasher Tonoyan", 
  "Dancer Moore", 
  "Prancer Chua", 
  "Vixen Hall", 
  "Comet Karavani",        
  "Cupid Foroutan", 
  "Donder Jonker", 
  "Blitzen Claus"
]))