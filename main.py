# importing libraries
import os
import pydub
import sksound
import csv
import shutil
from pydub import AudioSegment
import pandas as pd

storageDir = 'sonicCompiler_lib'
playlist = []
ingestionComplete = False

# --------------Initialization--------------------------
while True:
    usrInput = str(input("Enter the path of your playlist folder: "))
    if os.path.exists(usrInput):
        usrDir = input
        break
    else:
        print('file or directory does not exist, try again')

# create application directory and data csv
if not os.path.exists(storageDir):
    os.makedirs(storageDir)

if not os.path.exists(storageDir + '/songData.csv'):
    songDataCSV = pd.DataFrame(list())
    songDataCSV.to_csv(storageDir + '/songData.csv')

# Copies user's files to the application dir
for file in os.listdir(usrDir):
    oldFile = usrDir + '/' + file
    newFile = storageDir + '/' + file
    shutil.copyfile(oldFile, newFile)

# Appends the paths of the files in storageDir to playlist for conversion process
for entity in os.listdir(storageDir):
    full_entity = os.path.join(storageDir, entity)
    if os.path.isfile(full_entity):
        playlist.append(full_entity)  # adds song paths to playlist

# check for proper song ingestion
for thing in playlist:  
    print(thing)

# -----------Song File Conversion-------------------------
for thing in playlist:  # convert mp3 to wav for data ingestion
    file = AudioSegment.from_mp3(thing)
    file.export(thing, format="wav")
