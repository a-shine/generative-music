from midiutil import MIDIFile
from circle_of_fifths import Major

# degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number

# What is the range of midi note numbers?
# 0-127, where 60 is middle C

# Generate a random list of numbers that correspond to midi note numbers
import random

# Choose value from a random key

# Generate random rhythm for 4 bars of 4/4 time
import random

import random

def generate_rhythm():
    # Define the number of beats per bar and the number of bars
    beats_per_bar = 4
    num_bars = 2
    
    # Define the possible note durations
    durations = [2, 1, 0.5, 0.25]
    
    # Initialize an empty rhythm list
    rhythm = []
    
    # Generate a random rhythm for each bar
    for i in range(num_bars):
        # Initialize a list for the current bar
        bar = []
        
        # Generate notes for the current bar until the bar is full
        remaining_beats = beats_per_bar
        while remaining_beats > 0:
            # Choose a random note duration
            duration = random.choice(durations)
            
            # If the note duration fits within the remaining beats, add it to the bar
            if duration <= remaining_beats:
                bar.append(duration)
                remaining_beats -= duration
        
        # Add the current bar to the rhythm
        rhythm.extend(bar)
    
    return rhythm


# rhythm = generate_rhythm()
# print(rhythm)

# Convert notes to midi note numbers
def convert_to_midi(note: str):
    # note = string.upper(note)
    # note = note.lower()
    match note:
        case "C":
            return 60
        case "C#/Db":
            return 61
        case "D":
            return 62
        case "D#/Eb":
            return 63
        case "E":
            return 64
        case "F":
            return 65
        case "F#/Gb":
            return 66
        case "G":
            return 67
        case "G#/Ab":
            return 68
        case "A":
            return 69
        case "A#/Bb":
            return 70
        case "B":
            return 71 


c_maj = Major('D')

# TODO: Add the idea of modulating to a different key

def convert_note_list_to_midi(note_list: list):
    midi_list = []
    for note in note_list:
        midi_list.append(convert_to_midi(note))
    return midi_list

def random_note_list_in_key(key: Major):
    note_list = []
    for i in range(16):
        note_list.append(random.choice(key.scale()))
    return note_list

# print(random_note_list_in_key(c_maj))
degrees = convert_note_list_to_midi(random_note_list_in_key(c_maj))

print(degrees)

track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 110  # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

for i, degree in enumerate(degrees):
    MyMIDI.addNote(track, channel, degrees[i], time + i, duration, volume)


with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)