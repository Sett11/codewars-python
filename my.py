def gc_content(s):
    return round((s.count('C')+s.count('G'))/len(s)*100,2) if s else 0.0

print(gc_content('AAATTTCCCGGG'))