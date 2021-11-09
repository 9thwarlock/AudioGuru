import matplotlib.pyplot as plot
import numpy
from scipy.io import wavfile


def formSpecgram():
    samplingFrequency, sData = wavfile.read('/Users/akhilk/Documents/testDir/testSong2.wav')
    signalData = sData[:, 0]  # 0 denotes the usage of left stereo channel, 1 being right
    # numpy.savetxt("testSong1.csv", signalData, fmt='%1.3f' ,delimiter=",")
    plot.figure(figsize=(100, 10))
    plot.subplot(211)
    plot.title('Spectrogram of test song')

    plot.plot(signalData)
    plot.xlabel('Sample')
    plot.ylabel('Amplitude')

    plot.subplot(212)
    x = plot.specgram(signalData, Fs=samplingFrequency, sides='twosided')
    plot.xlabel('Time')
    plot.ylabel('Frequency')
    print(len(signalData))
    print(samplingFrequency)

    specData = numpy.array(x, dtype=object)

    # for weirdVal in specData:
    #    print(weirdVal)
    #    print("------")

    #plot.show()
