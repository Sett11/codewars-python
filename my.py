f=lambda x:x*2

def process_array(a,f):
    return list(map(f,a))

print(process_array([4, 8, 2, 7, 5],f))