def expression_out(e):
    a={"+" : "Plus",
"-": "Minus",
"*" : "Times",
"/" : "Divided By",
"**": "To The Power Of",
"=" : "Equals",
"!=": "Does Not Equal",}
    o={"+" : "Plus",
"-": "Minus",
"*" : "Times",
"/" : "Divided By",
"**": "To The Power Of",
"=" : "Equals",
"!=": "Does Not Equal",
'1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','0':'Zero','10':'Ten'}
    if(e.split()[1] not in a):return "That's not an operator!"
    return ' '.join(list(map(lambda e:o[e],e.split())))

print(expression_out('1 1 3'))