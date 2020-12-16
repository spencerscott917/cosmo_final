import corner
import emcee
import matplotlib.pyplot as plt


filename = 'tutorial.h5'
reader = emcee.backends.HDFBackend(filename)
samples = reader.get_chain(discard=1500, flat=True)

labels=['xi0', 'eta0', 'theta', 'i', 'gamma', 'vmax', 'v0', 'rt']

corner.corner(samples, labels=labels)
plt.savefig('corner.pdf')