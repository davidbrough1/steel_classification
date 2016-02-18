import pandas as pd
import numpy as np
from os import listdir
from scipy.io import savemat

dir_path = '/home/david/Downloads/EBSD data_DP Steel/'
file_names = sorted([i for i in listdir(dir_path) if i[-9:] == 'Pdata.txt'])
data_dict = {}
names = ['phi1', 'Phi', 'phi2', 'x', 'y',
         'IQ (image quality)', 'CI (Confidence Index)']
for f in file_names:
    print(f)
    df = pd.read_csv(dir_path + f, names=names, skiprows=9,
                     index_col=range(7, 14),
                     header=None, delim_whitespace=True)
    img_shape = (df['y'].values.max() + 1, df['x'].values.max() + 1, 3)
    img = np.zeros(img_shape)
    locs = (df['x'].values.astype(int), df['y'].values.astype(int))
    angles = df.values[:, :3]
    img[locs[1], locs[0]] = angles
    data_dict[f[:-10]] = img.copy()
savemat('orientaiton_data', data_dict)
