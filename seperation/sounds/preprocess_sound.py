"""The script makes the sources to have same length,
as well as have the same sampling rate"""
from scipy.io import wavfile
import utilities as utl

# Read the .wav files as numpy arrays
rate1, data1 = wavfile.read("sss1.wav")
rate2, data2 = wavfile.read("sss2.wav")

# Plot the sounds as time series data
utl.plotSounds([data1, data2], ["1", "2"], rate1, "/Users/songxinhang/Desktop/Cocktail-Party-Problem-master/plots/original")

# Make both of the files to have same length as well as same sampling rate
minimum = min(data1.shape[0], data2.shape[0])

# Slicing the array for both the sources
data1 = data1[0:minimum]
data2 = data2[0:minimum]

# writing the array into to the wav file with sampling rate which is average of the two
wavfile.write("sss1.wav", (rate1 + rate2)/2, data1)
wavfile.write("sss2.wav", (rate1 + rate2)/2, data2)