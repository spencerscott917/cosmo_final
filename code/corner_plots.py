import corner
import emcee
import matplotlib.pyplot as plt
import numpy as np
from model import *

# obj_name = fname.split('/')[-1][:-5] # extract object name from filename
# obj_name = 'id8'

filename = f"chains/chains_{obj_id}.h5"
reader = emcee.backends.HDFBackend(filename)
samples = reader.get_chain(discard=5000, flat=True)

labels=['xi0', 'eta0', 'theta', 'i', 'gamma', 'vmax', 'v0', 'rt']
ndim = 8

# rereading chains in order to set more sensible limits on samples for corner plots
lim_samples = reader.get_chain(discard=5000)
_d = {}
for yi in range(ndim):
    p50 = np.median(lim_samples[:,:,yi])
    print(p50)
    percent = 0.05
    if (yi <= 0) or (yi<4):
        _d[labels[yi]] = (p50-1,p50+1)
        # _d[labels[yi]] = (p50*(1-percent),p50*(1+percent))
    elif yi == 4:
        _d[labels[yi]] = (p50-.1,p50+.1)
        # _d[labels[yi]] = (p50*(1-percent),p50*(1+percent))
    elif yi < 7:
        _d[labels[yi]] = (p50-100,p50+100)
        # _d[labels[yi]] = (p50*(1-percent),p50*(1+percent))
    else:
        _d[labels[yi]] = (p50-1,p50+1)
        # _d[labels[yi]] = (p50*(1-percent),p50*(1+percent))
limits = [_d[labels[yi]] for yi in range(ndim)]


figure = corner.corner(samples, bins=75,
                                labels=labels,
                                quantiles=[0.16, 0.5, 0.84],
                                # range=limits,
                                show_titles=True)

figure.suptitle(obj_id)

figure.savefig(f'figs/corner_{obj_id}.pdf')