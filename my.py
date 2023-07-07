def my_first_kata(a,b):
  return False if type(a)!=int and type(a)!=float or type(b)!=int and type(b)!=float else a%b+b%a
    
print(my_first_kata(20,2))