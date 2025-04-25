from mido import Message, MidiFile, MidiTrack, second2tick, Parser, format_as_string
from PIL import Image
from random import randint, shuffle
import numpy as np

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

p = Parser()
values = []
notes = []

tonalities = {
    'major': [0, 2, 4, 5, 7, 9, 11, 12],
    'minor': [0, 2, 3, 5, 7, 8, 10, 12]
}

keys = {
    'c': 60,
    'c#': 61,
    'd': 62,
    'd#': 63,
    'e': 64,
    'f': 65,
    'f#': 66,
    'g': 67,
    'g#': 68,
    'a': 69,
    'a#': 70,
    'b': 71,
}


# If you want to have the midi file in a specific key 
def pitch_quantize(image, ext='.jpeg'): 
    key = input('What key? :')
    tonality = input('What? :')
    notesInKey = [i + keys[key] for i in tonalities[tonality]]
    im = Image.open(image+ext, 'r')
    pixel_val = list(im.getdata())
    pixel_val_flat = [x for sets in pixel_val for x in sets]
    conditionedPixels = [y for y in pixel_val_flat if y in notesInKey]
    newArray = list(conditionedPixels)
    shuffle(newArray)
    for x in newArray[:4000]:
        track.append(Message('note_on', note=int(x), velocity=int(randint(0, 127)), time=int(second2tick(1, 2, 3000))))
        track.append(Message('note_off', note=int(x), velocity=int(randint(0, 127)), time=100))
    mid.save(image + '.mid')

#If you want the midi file to be chromatic
def pitch_unquantize(image, ext='.jpg'):
    im = Image.open(image+ext, 'r')
    pixelVal = list(im.getdata())
    pixelValflat = [x for sets in pixelVal for x in sets]
    conditionedPixels = [y for y in pixelValflat if y < 127]
    for x in conditionedPixels[:4000]:
        track.append(Message('note_on', note=int(x), velocity=int(randint(0, 127)), time=int(second2tick(1, 2, 3000))))
        track.append(Message('note_off', note=int(x), velocity=int(randint(0, 127)), time=100))
    mid.save(image + '.mid')






























