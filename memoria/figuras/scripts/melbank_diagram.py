import matplotlib.pyplot as plt
from pyfilterbank import melbank

f1, f2 = 0, 8000

melmat, (melfreq, fftfreq) = melbank.compute_melmat(24, f1, f2, num_fft_bands=4097, sample_rate=16000)

fig, ax = plt.subplots(figsize=(10, 3))
ax.plot(fftfreq, melmat.T)

ax.set_ylabel('Amplitud')
ax.set_xlabel('Freqüència (Hz)', labelpad=0.0)
ax.set_xlim((f1, f2))
ax.set_ylim((0.005, 1))

plt.subplots_adjust(left=0.06, bottom=0.15, right=0.98, top=0.95)

plt.savefig("mel_filterbank.pdf", format="pdf", bbox_inches="tight", dpi=1200)
plt.show()
