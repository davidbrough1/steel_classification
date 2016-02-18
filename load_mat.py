from scipy.io import loadmat

data_dict = loadmat('orientaiton_data.mat')
keys = sorted(data_dict.keys())[:-3]
print 'sample\t\tgimage size'
for k in keys:
    print k, '\t', data_dict[k].shape
