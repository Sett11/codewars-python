def is_matching(st, st1, st2): 
    return sorted(st.replace(' ','').lower())==sorted((st1+st2).replace(' ','').lower())