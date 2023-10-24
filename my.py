words=[
["like", "a", "tweet", "what", "for", "world", "whale", "one", "last", "sun"],
["ocean", "beauty", "tweet", "monster", "yellow", "return", "despair", "flower", "return", "contrast"],
["romantic", "curious", "banana", "jealousy", "tactlessly", "remorseful", "follower", "elephant", "however", "instagram"],
["salmonella", "consequently", "irregular", "intelligence", "vegetable", "ordinary", "alternative", "watermelon", "controversial", "marijuana"],
["lackadaisical", "serendipity", "colonoscopy", "dramatically", "parsimonius", "imagination", "electricity", "diabolical", "deforestation", "abomination"],
["extraterrestrial", "onomatopoeia", "responsibility", "revolutionary", "generalisation", "enthusiastically", "biodiversity", "veterinarian", "characteristically", "indefatigable"],
["oversimplification", "individuality", "decriminalisation", "compartmentalisation", "anaesthesiologist", "industrialisation", "buckminsterfullerene", "irresponsibility", "autobiographical", "utilitarianism"]]

def haiku_wizard(a):
    return '\n'.join([' '.join([words[int(str(j)[0])-1][int(str(j)[1])] for j in i]) for i in a])


print(haiku_wizard([[10, 11, 23, 16], [50, 12, 14], [15, 40]]))