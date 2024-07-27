class JurassicWord(object):
    def __init__(self):
        self.dead_dino = "_C     C}>" 
        self.flowers = "iii     iii"
        self.leaves = "|||     |||"
        self.t_rex = "VvvvV"
        self.velociraptor = "vvvvv" 
        self.brachiosaurus = "uuuuu"
        self.triceratops = "uuVuu"
        
    def lunch_time(self,s):
        print(s)
        if s[:2]+' '*5+s[-3:]==self.dead_dino:
            if s[2:-3]==self.velociraptor:
                return 'A velociraptor is eating a dead dino.'
            if s[2:-3]==self.t_rex:
                return 'A T-Rex is eating a dead dino.'
            else:
                return 'Something is eating a dead dino.'
        if s[3:-3]==self.velociraptor or s[3:-3]==self.t_rex:
            if s[:3]+' '*5+s[-3:]==self.flowers:
                return 'Something is eating flowers.'
            if s[:3]+' '*5+s[-3:]==self.leaves:
                return 'Something is eating leaves.'
            else:
                if s[3:-3]==self.velociraptor:
                    return 'A velociraptor is eating something.'
                else:
                    return 'A T-Rex is eating something.'
        if s[3:-3]==self.brachiosaurus:
            t=s[:3]+' '*5+s[-3:]
            if t==self.flowers:
                return 'A brachiosaurus is eating flowers.'
            if t==self.leaves:
                return 'A brachiosaurus is eating leaves.'
            else:
                return 'A brachiosaurus is eating something.'
        if s[3:-3]==self.triceratops:
            if s[:3]+' '*5+s[-3:]==self.flowers:
                return 'A triceratops is eating flowers.'
            if s[:3]+' '*5+s[-3:]==self.leaves:
                return 'Something is eating leaves.'
            else:
                return 'A triceratops is eating something.'
        if s[:3]+' '*5+s[-3:]==self.flowers:
            return 'Something is eating flowers.'
        if s[:3]+' '*5+s[-3:]==self.leaves:
            return 'Something is eating leaves.'
        return 'Something is eating something.'

        
j=JurassicWord()
print(j.lunch_time('_CVvvvVC}>'))
print(j.lunch_time('vvvvvvvvvvv'))