import matplotlib.pyplot as plt
import emcee 


ndim = 8
filename = "tutorial.h5"
reader = emcee.backends.HDFBackend(filename)
samples = reader.get_chain()

labels=['xi0', 'eta0', 'theta', 'i', 'gamma', 'vmax', 'v0', 'rt']

fig, axes = plt.subplots(ndim, figsize=(10, 7), sharex=True)
for i in range(ndim):
    ax = axes[i]
    ax.plot(samples[:, :, i], "k", alpha=0.3)
    ax.set_xlim(0, len(samples))
    ax.set_ylabel(labels[i])
    ax.yaxis.set_label_coords(-0.1, 0.5)

axes[-1].set_xlabel("step number")
plt.savefig('burnin.pdf')
