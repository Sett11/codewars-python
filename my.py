def window(x,y,lst):
    return [k for k in [lst[i:i+x] for i in range(0,len(lst),y)] if len(k)==x]+([] if x else [[]])