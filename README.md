# AudioGuru
developed by Akhil Kammela


## What exactly is AudioGuru?
AudioGuru is a Python based application that learns about a user's music taste, and helps predict which of the user's playlists a newly discovered song should be added to.

From a technical view, AudioGuru forms spectrograms with WAV files provided by a user, and utilizes said spectrograms to train a set of classifiers to detect where new songs should be placed amongst a user's library of playlists.

&nbsp;

## How does AudioGuru work?


### Essential Packages/Dependencies
> Currently AudioGuru utilizes
> - [Scikit-sound](http://work.thaslwanter.at/sksound/html/)
> - [Pydub](https://github.com/jiaaro/pydub)
> - [Pandas](https://pandas.pydata.org/)
> - [Matplotlib](https://matplotlib.org/)
> - [SciPy](https://scipy.org/)
> - [Scikit-Learn](https://scikit-learn.org/stable/)

&nbsp;
### Features
> - AG interacts with song spectrograms and consolidates nearly 10 million data points **per song**
> 
> - Trains classifiers with spectrogram data to build a recommendation system (*in progress*)

&nbsp;

### Technical Basis
> **How will AG be able to use spectrograms to detect which playlist a song should be placed in ?**
> 
> As detailed in a [research paper](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.706.160&rep=rep1&type=pdf) from Institute of Systems and Computer Engineering of Porto, features extracted from the spectrograms of songs can be used to train a group of SVM classifiers tasked with performing automatic music genre classification. While the research group trained an ensemble of classifiers for genre detection, the results of their research can still be applied to AudioGuru. With the way that AudioGuru is structured, AG effectively treats user playlists as psuedo-genres. AG trains the classifiers around these psuedo-genres, so when given a song to classify under a pseudo-genre, AG's classification of the song serves as a recommendation of which playlist the song should be placed in. The paper found that the use of an ensemble of classifiers has an 86% success rate in genre detection. While AudioGuru won't be utilizing the same set of SVM classifiers, the aim is to reach a similar rate of success.
>
> TLDR: Research shows that training classifiers with spectrogram data allows for a high success rate in song genre classification. Given the structure of AudioGuru, building classifiers around the spectrograms of WAV files will allow for AudioGuru to give successful recommendations.

&nbsp;

### AudioGuru's functionality is comprised of 5 key processes
> - 1: Ingestion
> - 2: Curation 
> - 3: Analytics
> - 4: Knowledge System
> - 5: Decision Support

&nbsp;

## Key Processes
### Ingestion:
> - The Ingestion step of AG begins with the initialization of application files/folders where data is to be stored and managed.
> - AG prompts the user to input a playlist by providing a path to the folder where the playlist songs are stored.
> - AG prepares the songs by converting any .mp3 files to .WAV.

 ###  Curation:
 > - AG iterates through the playlist, forming spectrograms from the previously stored .WAV files.
 > - Data from the spectrograms are derived as numpy arrays, then stored in a CSV file. 
 > - AG performs preprocessing by applying variance scaling on the data stores in the CSV file.

 ###  Analytics: *in progress*
 > - The SVM Classifiers are trained with preprocessed data.
 > - Models formed from the classifiers are stored for use in the knowledge system.


 ###  Knowledge System: *in progress*
 > - The efficacy of the created models are tested, efficacy is displayed to the user



 ###  Decision Support: *in progress*
 > - AG prompts the user to input songs
 > - Stored models are used to determine the classification of the newly provided songs
 > - AG displays its recommendation to the user.



