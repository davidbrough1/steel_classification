import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt
from pymks import MKSStructureAnalysis
from pymks.bases import GSHBasis
from pymks.tools import draw_components_scatter

data_dict = loadmat('orientaiton_data.mat')
keys = sorted(data_dict.keys())[:-3]
data_list = [data_dict[k] for k in keys]
shapes = [s.shape for s in data_list]
X = []
crop_size = (100, 100)  # (400, 1100)
for s, d in zip(shapes, data_list):
    x_0, x_1 = (s[0] - crop_size[0] - 1) / 2, - (s[0] - crop_size[0] - 1) / 2
    y_0, y_1 = (s[1] - crop_size[1] - 1) / 2, - (s[1] - crop_size[1] - 1) / 2
    X.append(d[x_0:x_1, y_0:y_1][None])
X = np.concatenate(X)
X_masks = np.sum(X, axis=-1) > 0
gsh_basis = GSHBasis(n_states=7)
anaylzer = MKSStructureAnalysis(basis=gsh_basis, n_components=3)
y = anaylzer.fit_transform(X, confidence_index=X_masks)
labels = [k[:-3] for k in keys[::-3]]
draw_components_scatter(np.array_split(y, 9), labels=labels)
