"""
Usage example:
python3 fourier.py stt1.out/table.txt

"""

import sys
import numpy as np
import pandas as pd
#import csv
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt


def fourier(T, signal):

    t0 = T[1]
    SAMPLE_RATE = 1 / t0
    print("SAMPLE_RATE: {:.04f} GHz".format(SAMPLE_RATE))
    #DURATION = 1
    # число точек в normalized_tone
    #N = SAMPLE_RATE * DURATION
    N = len(signal)
    print("N = ", N)

    xf = fftfreq(N, 1 / SAMPLE_RATE)
    yf = fft(signal)
    yf = np.abs(yf) / N

    maxind = np.argmax(yf)
    print("Peak f = {:.4f} GHz".format(abs(xf[maxind])))

    #plt.plot(T, signal)
    #xf = xf[:N//2]
    #yf = yf[:N//2]
    #print(xf)
    #print(yf)
    plt.plot(xf, yf)
    # Here we go:
    plt.xlim(-0.3, 0.3)
    plt.ylim(-1, 1)
    plt.show()


def process_file(data_path):

    df = pd.read_csv(data_path, sep="\t")
    df.columns=['t','mx','my','mz']

    T = df.t.values * 1e9
    signal = df.mx.values
    #print(T, signal)
    plt.plot(T, signal)
    #plt.xlim(-0.3, 0.3)
    #plt.ylim(-1, 1)
    plt.show()

    fourier(T, signal)



if __name__ == "__main__":

    if len(sys.argv) > 1:
        data_path = sys.argv[1]
    else:
        data_path = "stt2.out/table.txt"

    process_file(data_path)


