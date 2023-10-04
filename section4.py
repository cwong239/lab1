"""
Signature:  f2m double -> double

Header:     f2m(1) -> 0.3048
            f2m(10) - > 0.3048
            f2m("not a number") -> Enter a number please
            f2m(-15.2) -> 4.63296
            f2m(0.92137875) -> 0.280836243

Purpose:    Convert an amount of feet to an amount of meters
"""

def f2m(feet):
    try:
        return feet * 0.3048
    except:
        return "Enter a number please"



"""
Signature:  Note -> none
            getPitch -> double
            getDuration -> double

Purpose:    up a pitch by one octave
"""

class Note:
    def __init__(self, p, d):
        self.pitch = p
        self.duration = d

    def getPitch(self):
        return self.pitch
    def getDuration(self):
        return self.duration

"""
Signature:  up_one_octave note -> double

Header:     n1 = Note(10, 2)
            up_one_octave(n1) -> 20
            
            n2 = Note(0.12398, 2)
            up_one_octave(n2) -> 0.24796
            
            n3 = Note("Not a number", 2)
            up_one_octave(n3) -> Please enter a valid number
            
            n4 = Note(-1, 2)
            up_one_octave(n4) -> Please enter a valid number
            
            n5 = Note(1203, 2)
            up_one_octave(n5) -> 2406

Purpose:    up a pitch by one octave
"""

def up_one_octave(note):
    try:
        if note.getPitch()>0:
            return note.getPitch()*2
    except:
        return "Please enter a valid number"


n1 = Note(10, 2)
print(up_one_octave(n1))

n2 = Note(0.12398, 2)
print(up_one_octave(n2))

n3 = Note("Not a number", 2)
print(up_one_octave(n3))