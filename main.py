# importing libraries
import os
import pydub


wrkDir = str(input("Enter the path of your playlist folder: "))

playlist = []

try:
    for entity in os.listdir(wrkDir):
        full_entity = os.path.join(wrkDir, entity)
        if os.path.isfile(full_entity):
            playlist.append(full_entity)
except (FileNotFoundError, IOError):
    print("Wrong file or file path")


for thing in playlist:
    print(thing)

for thing in playlist:
    file = AudioSegment.from_mp3(thing)
    file.export(thing, format="wav")
