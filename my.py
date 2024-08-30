def convert_lambda_to_def(s):
    a=s.split('=')
    f_head=f"def {a[0].strip()}({a[1].split(':')[0].replace('lambda','',1).strip()}):\n    return "
    return f_head+a[1].split(': ')[1]

print(convert_lambda_to_def("act = lambda h: h + ' ' + 'i'"))