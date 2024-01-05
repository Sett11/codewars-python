class Automaton(object):
    def __init__(self):
        self.q=['q1','q2','q3']
        self.c=0

    def read_commands(self,a):
        for i in range(len(a)):
            if (a[i]=='1' and self.q[self.c%3]=='q1') or (a[i]=='0' and self.q[self.c%3]=='q2'):
                self.c+=1
                continue
            if self.q[self.c%3]=='q3':
                self.c-=1
        return self.q[self.c%3]=='q2'
        
my_automaton = Automaton()

print(my_automaton.read_commands(["1", "0", "0", "1"]))