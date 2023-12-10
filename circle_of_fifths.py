notes = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]

# This could be used to give the melody generator a sense of key

# Introduce the idea of an abstract key class with a scale method

class Key:

    def __init__(self, root) -> None:
        super().__init__()
        self.root = root

    def root(self):
        return self.root

    def fourth(self):
        return notes[(notes.index(self.root)+5) % 12]
    
    def fifth(self):
        return notes[(notes.index(self.root)+7) % 12]

    def scale(self):
        return [self.root, self.second(), self.third(), self.fourth(), self.fifth(), self.sixth(), self.seventh(), self.root]

    


class Major(Key):

    def second(self):
        return notes[(notes.index(self.root)+2) % 12]

    def third(self):
        return notes[(notes.index(self.root)+4) % 12]

    # fourth and fifth are perfect (shared across major and minor keys)

    def sixth(self):
        return notes[(notes.index(self.root)+9) % 12]

    def seventh(self):
        return notes[(notes.index(self.root)+11) % 12]

    

#is diminished/augmented relative to the major or minor key or entirely independent?







# to give a sense of key the melody generator use the generated circle of fifths to know the specific pitch for each degree of the scale
class CircleOfFifths:
    
    def __init__(self) -> None:
        pass

# major/minor key




