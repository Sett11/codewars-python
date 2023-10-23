notes_dictionary = {
    440: "A",
    466.16: "A#",
    493.88: "B",
    523.25: "C",
    554.37: "C#", 
    587.33: "D", 
    622.25: "D#", 
    659.25: "E", 
    698.46: "F", 
    739.99: "F#", 
    783.99: "G", 
    830.61: "G#"}

def get_note(n):
    for i in notes_dictionary:
        if n%i==0 or i%n==0:
            return notes_dictionary[i]

print(get_note(1046.5))