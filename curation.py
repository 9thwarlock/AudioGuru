import matplotlib.pyplot as plot
from scipy.io import wavfile
import csv

import initialization

# dataFile = open('sonicCompiler_lib/songData.csv')


for song in initialization.playlist:
    samplingFrequency, sData = wavfile.read(song)
    signalData = sData[:, 0]  # 0 denotes the usage of left stereo channel, 1 being right
    print(len(signalData))
    x = plot.specgram(signalData, Fs=samplingFrequency, sides='twosided')
    with open("songData.csv", 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Title", "Data", 'Frequency'])
        csvwriter.writerows([song, signalData, samplingFrequency])


