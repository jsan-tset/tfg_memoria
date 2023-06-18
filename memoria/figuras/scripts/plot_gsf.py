import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Dades
#data_pm = pd.read_csv('gsf_gmm_pm.csv')
#data_ub = pd.read_csv('gsf_gmm_ub.csv')
#data_pm = pd.read_csv('gsf_dnn_pm.csv')
#data_ub = pd.read_csv('gsf_dnn_ub.csv')
#data_pm = pd.read_csv('gsf_oldlm_small_pm.csv')
#data_ub = pd.read_csv('gsf_oldlm_small_ub.csv')
#data_pm = pd.read_csv('gsf_oldlm_big_pm.csv')
#data_ub = pd.read_csv('gsf_oldlm_big_ub.csv')
data_pm = pd.read_csv('gsf_newlm_small_pm.csv')
data_ub = pd.read_csv('gsf_newlm_small_ub.csv')
#data_pm = pd.read_csv('gsf_newlm_big_pm.csv')
#data_ub = pd.read_csv('gsf_newlm_big_ub.csv')
#data_pm = pd.read_csv('gsf_tlm_pm.csv')
#data_ub = pd.read_csv('gsf_tlm_ub.csv')
#data_pm = pd.read_csv('gsf_tlm_ngram_pm.csv')
#data_ub = pd.read_csv('gsf_tlm_ngram_ub.csv')


# Gràfica gmm; dnn; oldlm_big; newlm_small; newlm_big; tlm; tlm+ngram

plt.plot(data_pm['GSF'].to_numpy(), data_pm['WER'].to_numpy(), marker='o', label='PM', color='royalblue')
plt.plot(data_ub['GSF'].to_numpy(), data_ub['WER'].to_numpy(), marker='o', label='UB', color='tab:orange')

plt.text(9, 21.75, "PM", color='royalblue')
plt.text(8, 20.1, "UB", color='tab:orange')


# Gràfica sis curves oldlm_small
"""
plt.plot(data_pm['GSF'].to_numpy(), data_pm['WER09'].to_numpy(), marker='o', label='PM', color='royalblue')
plt.plot(data_pm['GSF'].to_numpy(), data_pm['WER10'].to_numpy(), marker='v', label='PM', color='tab:orange')
plt.plot(data_pm['GSF'].to_numpy(), data_pm['WER11'].to_numpy(), marker='s', label='PM', color='forestgreen')
plt.plot(data_ub['GSF'].to_numpy(), data_ub['WER09'].to_numpy(), marker='o', label='UB', color='royalblue')
plt.plot(data_ub['GSF'].to_numpy(), data_ub['WER10'].to_numpy(), marker='v', label='UB', color='tab:orange')
plt.plot(data_ub['GSF'].to_numpy(), data_ub['WER11'].to_numpy(), marker='s', label='UB', color='forestgreen')

plt.text(8, 22.4, "PM - PSF=0,9", color='royalblue')
plt.text(8, 22.2, "PM - PSF=1,0", color='tab:orange')
plt.text(8, 22.0, "PM - PSF=1,1", color='forestgreen')
plt.text(8, 20.8, "UB - PSF=0,9", color='royalblue')
plt.text(8, 20.6, "UB - PSF=1,0", color='tab:orange')
plt.text(8, 20.4, "UB - PSF=1,1", color='forestgreen')
"""




#plt.yticks(np.arange(17.5, 21.0, 0.5))
plt.xticks(np.arange(8, 13, 1))


plt.xlabel("GSF")
#plt.xlabel("LMHR") # cas del tranformer
plt.ylabel("WER")


#plt.legend()

plt.savefig("gsf_tlm_ngram.pdf", format="pdf", bbox_inches="tight", dpi=1200)

plt.show()
