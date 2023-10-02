class Feet2Meters:
    def __init__(self):
        pass
    def f2m(self,feet):
        try:
            return feet * 0.3048
        except:
            return "Enter a number please"



class Note:
    def __init__(self, p, d):
        self.pitch = p
        self.duration = d

    def getPitch(self):
        return self.pitch
    def getDuration(self):
        return self.duration

def up_one_octave(self, note):
    return note.getPitch()*2

