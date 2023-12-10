import random
from midiutil import MIDIFile

# Set the tempo and time signature
tempo = 120
time_signature = (4, 4)

# Set the number of tracks, the duration of the song, and the MIDI channel
num_tracks = 1
duration = 4  # in seconds
midi_channel = 0

# Set the range of notes to use
lowest_note = 48  # C3
highest_note = 84  # C6

# Set the possible durations (in beats) of the notes
possible_durations = [0.25, 0.5, 1, 2, 4]

# Create a MIDIFile object with the specified parameters
midi_file = MIDIFile(numTracks=num_tracks, file_format=1, ticks_per_quarternote=240, deinterleave=False)

# Add a track to the MIDIFile object
midi_file.addTrackName(track=0, time=0, trackName="Random Melody")
midi_file.addTempo(track=0, time=0, tempo=tempo)

# Generate a random melody by selecting notes and durations from the specified ranges
melody = []
current_time = 0
while current_time < duration * 240:
    # Select a random note and duration
    note = random.randint(lowest_note, highest_note)
    duration = random.choice(possible_durations)
    
    # Add the note to the melody
    melody.append((note, duration))
    
    # Add a rest between notes
    rest_duration = random.choice([0.25, 0.5, 1])
    current_time += int(duration * 240) + int(rest_duration * 240)

# Add the notes to the MIDI file
for i, (note, duration) in enumerate(melody):
    # Set the start time and duration of the note
    start_time = i * 240  # 1 beat = 240 ticks
    duration_ticks = int(duration * 240)

    # Set the velocity of the note (0-127)
    velocity = random.randint(80, 127)

    # Add the note to the MIDI file
    midi_file.addNote(track=0, channel=midi_channel, pitch=note, time=start_time, duration=duration_ticks, volume=velocity)

# Write the MIDI file to disk
with open("random_melody.mid", "wb") as output_file:
    midi_file.writeFile(output_file)
