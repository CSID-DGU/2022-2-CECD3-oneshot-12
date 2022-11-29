import os
from sklearn.model_selection import train_test_split

#normal/normal51.avi 1
#selfharm/normal51.avi 0
# normal/normal51.avi 
# selfharm/normal51.avi 

datas_normal_path = '/home/plass-oneshot/jsw/3D-ResNets-PyTorch/prepared_dataset/export/normal/'
datas_selfharm_path = '/home/plass-oneshot/jsw/3D-ResNets-PyTorch/prepared_dataset/export/selfharm/'

# normal
# datas_normal_list = [name for name in os.listdir(datas_path)]

datas_normal_list = [name for name in os.listdir(datas_normal_path)]
datas_selfharm_list = [name for name in os.listdir(datas_selfharm_path)]

train_normal, val_normal = train_test_split(datas_normal_list, test_size=0.2, random_state=42)
train_selfharm, val_selfharm = train_test_split(datas_selfharm_list, test_size=0.2, random_state=42)

# trainlist01.txt
# train_normal, train_selfharm
# normal/normal51.avi 1


trainlist_normal_list = [ 'normal/'+name+' 1'  for name in train_normal]
trainlist_selfharm_list = [ 'selfharm/'+name+' 2'  for name in train_selfharm]

f = open('/home/plass-oneshot/jsw/3D-ResNets-PyTorch/test/trainlist01.txt', 'a')
for name in trainlist_normal_list:
    f.write(name+'\n')
f.close()

f = open('/home/plass-oneshot/jsw/3D-ResNets-PyTorch/test/trainlist01.txt', 'a')
for name in trainlist_selfharm_list:
    f.write(name+'\n')
f.close()


# testlist01.txt
# val_normal, val_selfharm
# normal/normal51.avi 
vallist_normal_list = [ 'normal/'+name  for name in val_normal]
vallist_selfharm_list = [ 'selfharm/'+name  for name in val_selfharm]

f = open('/home/plass-oneshot/jsw/3D-ResNets-PyTorch/test/testlist01.txt', 'a')
for name in vallist_normal_list:
    f.write(name+'\n')
f.close()

f = open('/home/plass-oneshot/jsw/3D-ResNets-PyTorch/test/testlist01.txt', 'a')
for name in vallist_selfharm_list:
    f.write(name+'\n')
f.close()



print('finished')