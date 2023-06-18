import matplotlib.pyplot as plt
import numpy as np
from math import exp, sin, pi
import wave, sys
 
def visualize(path: str):
   
    # reading the audio file
    raw = wave.open(path)
     
    # -1 indicates all frames
    signal = raw.readframes(-1)
    signal = np.frombuffer(signal, dtype ="int16")
   
    sign_len = len(signal)
    signal_hmm = []
    for i in range(sign_len):
        signal_hmm.append( signal[i]*sin(i/sign_len*pi) )

    f_rate = raw.getframerate()
 
    time = np.linspace(
        0, # start
        len(signal) / f_rate,
        num = len(signal)
    )
 
    plt.figure(1)
    plt.xlabel("T (s)")
    plt.ylabel("Amplitud")
    plt.plot(time, signal)
    #plt.plot(time, signal_hmm)
    
    plt.subplots_adjust(left=0.15, bottom=0.14, right=0.98, top=0.98)

    #plt.savefig("finestres_hamm.pdf", format="pdf", bbox_inches="tight", dpi=1200)
    plt.show()
 
 
if __name__ == "__main__":
   
    path = sys.argv[1]
 
    visualize(path)
