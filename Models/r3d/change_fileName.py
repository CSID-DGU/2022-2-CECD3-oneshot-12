import os




all_file = os.listdir('/home/plass-oneshot/jsw/3D-ResNets-PyTorch/prepared_dataset/export_v2/selfharm')



for file_dir_path in all_file:
    file_dir_path = './'+file_dir_path

    file_names = os.listdir(file_dir_path)

    new_name = 'image'
    for name in file_names:
        before_name = os.path.join(file_dir_path, name)
        after_name = f'{new_name}_'+name
        after_name = os.path.join(file_dir_path, after_name)
        os.rename(before_name, after_name)
  
