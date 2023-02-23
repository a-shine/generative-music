pitches = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]

# This could be used to give the melody generator a sense of key

class Key:

    def __init__(self, root) -> None:
        super().__init__()
        self.root = root

    def root(self):
        return self.root

    def fourth(self):
        return pitches[(pitches.index(self.root)+5) % 12]
    
    def fifth(self):
        return pitches[(pitches.index(self.root)+7) % 12]


class Major(Key):

    def second(self):
        return pitches[(pitches.index(self.root)+2) % 12]

    def third(self):
        return pitches[(pitches.index(self.root)+4) % 12]

    # fourth and fifth are perfect (shared across major and minor keys)

    def sixth(self):
        return pitches[(pitches.index(self.root)+9) % 12]

    def seventh(self):
        return pitches[(pitches.index(self.root)+11) % 12]

#is diminished/augmented relative to the major or minor key or entuirely independent?







# to give a sense of key the melody generator use the generated circle of fifths to know the specific pitch for each degree of the scale
class CircleOfFifths:
    
    def __init__(self) -> None:
        pass

# major/minor key




