o={'039':'Golden Telecom','050':'MTS','063':'Life:)','066':'MTS','068':'Beeline','093':'Life:)','095':'MTS','096':'Kyivstar','097':'Kyivstar','098':'Kyivstar','099':'MTS','067':'Kyivstar'}

def detect_operator(s):
    s=s[slice(1,4)]
    return o[s] if s in o else 'no info'

print(detect_operator('80111551111'))