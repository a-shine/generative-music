import mido
import random
import sys
from collections import namedtuple


def generate_melody(scale, rhythm):
    """Generates a melody based on the given scale and rhythm.

    The melody is generated by randomly selecting notes from the scale and placing them in the given rhythm.

    Parameters:
      scale: The scale to use for the melody.
      rhythm: The rhythm to use for the melody.

    Returns:
      A list of notes.
    """
    notes = []
    # Populates the initial melody space with rests and note placeholders
    for note in rhythm:
        if note == 'rest':
            notes.append('rest')
        else:
            notes.append(note)

    for note in scale:
        if note == 'rest':
            notes.append('rest')
        else:
            notes.append(note)
    return notes


# MIDIEvent = namedtuple("MIDIEvent", "event_type", "note", "duration", "velocity", "channel", "program_number", "pitch_bend_value", "aftertouch_value", "control_change")
# MIDIEvent = namedtuple("MIDIEvent", ["event_type", "note", "duration", "velocity", "channel", "program_number", "pitch_bend_value", "aftertouch_value", "control_change"])


def generate_melody():
    """Generates a simple random melody."""

    # Generate a random sequence of notes.
    notes = [random.randint(0, 127) for _ in range(16)]

    # Generate a sequence of durations for the notes.
    durations = [random.randint(0, 127) for _ in range(16)]

    # Write the MIDI events to a file.
    with open("melody.mid", "wb") as f:
        f.write(b"".join(mido.Message(type="note_on", note=note, duration=duration)
                for note, duration in zip(notes, durations)))