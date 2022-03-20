"""
Usage example:
python3 fourier.py stt1.out/table.txt

"""

import os
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

    #plt.plot(T, signal)
    #xf = xf[:N//2]
    #yf = yf[:N//2]
    return xf, yf


def process_file(data_path, outdir):

    df = pd.read_csv(data_path, sep="\t")
    df.columns=['t','mx','my','mz']

    T = df.t.values * 1e9
    signal = df.mx.values
    #print(T, signal)
    plt.plot(T, signal)
    #plt.xlim(-0.3, 0.3)
    #plt.ylim(-1, 1)
    plt.savefig(os.path.join(outdir, 'signal.png'))
    plt.show()

    xf, yf = fourier(T, signal)
    maxind = np.argmax(yf)
    peak = abs(xf[maxind])
    print("Peak f = {:.6f} GHz".format(peak))

    #print(xf)
    print("len(yf):", len(yf))
    plt.plot(xf, yf)
    # Here we go:
    #plt.xlim(-0.3, 0.3)
    #plt.xlim(-1, 1)
    #plt.ylim(0, 1)
    plt.xlim(0, 1)
    plt.ylim(0, 0.5)
    plt.savefig(os.path.join(outdir, 'spectrum.png'))
    plt.show()

    with open(os.path.join(outdir, 'result.txt'), "wt") as fp:
        fp.write("{:.6f} GHz\n".format(peak))

if __name__ == "__main__":

    if len(sys.argv) > 1:
        data_path = sys.argv[1]
    else:
        data_path = "stt2.out/table.txt"

    process_file(data_path, outdir="stt2.out")


