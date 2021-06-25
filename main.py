# importing libraries
import os
import pydub


wrkDir = str(input("Enter the path of your playlist folder: "))

playlist = []

for entity in os.listdir(wrkDir):
    full_entity = os.path.join(wrkDir, entity)
    if os.path.isfile(full_entity):
        playlist.append(full_entity)


for thing in playlist:
    print(thing)

for thing in playlist:
    file = AudioSegment.from_mp3(thing)
    file.export(thing, format="wav")