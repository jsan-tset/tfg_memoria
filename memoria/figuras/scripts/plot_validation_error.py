import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Dades
data = pd.read_csv('validation_epoch.csv')

# Plot
plt.plot(data['EPOCH'].to_numpy(), data['ERR'].to_numpy(), marker='x', color='royalblue')

plt.xlabel("Època")
plt.ylabel("Error de validació (FER%)")
plt.xticks(np.arange(0, 28, 3))

#plt.legend()

plt.savefig("validation_error.pdf", format="pdf", bbox_inches="tight", dpi=1200)

plt.show()
