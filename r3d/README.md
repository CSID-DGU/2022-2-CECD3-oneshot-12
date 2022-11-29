# 3D ResNets for Action Recognition


## Requirements

* [PyTorch](http://pytorch.org/) (ver. 0.4+ required)

```bash
conda install pytorch torchvision cudatoolkit=10.1 -c soumith
```

* FFmpeg, FFprobe

* Python 3

## Preparation

### ActivityNet

* Download videos using [the official crawler](https://github.com/activitynet/ActivityNet/tree/master/Crawler).
* Convert from avi to jpg files using ```util_scripts/generate_video_jpgs.py```

```bash
python -m util_scripts.generate_video_jpgs mp4_video_dir_path jpg_video_dir_path activitynet
```

* Add fps infomartion into the json file ```util_scripts/add_fps_into_activitynet_json.py```

```bash
python -m util_scripts.add_fps_into_activitynet_json mp4_video_dir_path json_file_path
```

### Kinetics

* Download videos using [the official crawler](https://github.com/activitynet/ActivityNet/tree/master/Crawler/Kinetics).
  * Locate test set in ```video_directory/test```.
* Convert from avi to jpg files using ```util_scripts/generate_video_jpgs.py```

```bash
python -m util_scripts.generate_video_jpgs mp4_video_dir_path jpg_video_dir_path kinetics
```

* Generate annotation file in json format similar to ActivityNet using ```util_scripts/kinetics_json.py```
  * The CSV files (kinetics_{train, val, test}.csv) are included in the crawler.

```bash
python -m util_scripts.kinetics_json csv_dir_path 700 jpg_video_dir_path jpg dst_json_path
```

### UCF-101

* Convert from avi to jpg files using ```util_scripts/generate_video_jpgs.py```

```bash
python -m util_scripts.generate_video_jpgs avi_video_dir_path jpg_video_dir_path ucf101

nohup python -m util_scripts.generate_video_jpgs /home/plass-oneshot/jsw/video_gan/DVD-GAN/dataset/UCF101/videos_classified /home/plass-oneshot/jsw/3D-ResNets-PyTorch/prepared_dataset ucf101 &

```

* Generate annotation file in json format similar to ActivityNet using ```util_scripts/ucf101_json.py```
  * ```annotation_dir_path``` includes classInd.txt, trainlist0{1, 2, 3}.txt, testlist0{1, 2, 3}.txt

```bash
python -m util_scripts.ucf101_json annotation_dir_path jpg_video_dir_path dst_json_path

python -m util_scripts.ucf101_json /home/plass-oneshot/jsw/3D-ResNets-PyTorch/annotations/ucfTrainTestlist /home/plass-oneshot/jsw/3D-ResNets-PyTorch/prepared_dataset /home/plass-oneshot/jsw/3D-ResNets-PyTorch/dst_json

python -m util_scripts.ucf101_json2 /home/plass-oneshot/jsw/3D-ResNets-PyTorch/annotations/export_ann /home/plass-oneshot/jsw/3D-ResNets-PyTorch/prepared_dataset/export/ /home/plass-oneshot/jsw/3D-ResNets-PyTorch/
```

### HMDB-51

* Download videos and train/test splits [here](http://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database/).
* Convert from avi to jpg files using ```util_scripts/generate_video_jpgs.py```

```bash
python -m util_scripts.generate_video_jpgs avi_video_dir_path jpg_video_dir_path hmdb51
```

* Generate annotation file in json format similar to ActivityNet using ```util_scripts/hmdb51_json.py```
  * ```annotation_dir_path``` includes brush_hair_test_split1.txt, ...

```bash
python -m util_scripts.hmdb51_json annotation_dir_path jpg_video_dir_path dst_json_path

```

## Running the code

Assume the structure of data directories is the following:

```misc
~/
  data/
    kinetics_videos/
      jpg/
        .../ (directories of class names)
          .../ (directories of video names)
            ... (jpg files)
    results/
      save_100.pth
    kinetics.json
```

Confirm all options.

```bash
python main.py -h
```

Train ResNets-50 on the Kinetics-700 dataset (700 classes) with 4 CPU threads (for data loading).  
Batch size is 128.  
Save models at every 5 epochs.
All GPUs is used for the training.
If you want a part of GPUs, use ```CUDA_VISIBLE_DEVICES=...```.

```bash
python main.py --root_path ~/data --video_path kinetics_videos/jpg --annotation_path kinetics.json \
--result_path results --dataset kinetics --model resnet \
--model_depth 50 --n_classes 700 --batch_size 128 --n_threads 4 --checkpoint 5
```

Continue Training from epoch 101. (~/data/results/save_100.pth is loaded.)

```bash
python main.py --root_path ~/data --video_path kinetics_videos/jpg --annotation_path kinetics.json \
--result_path results --dataset kinetics --resume_path results/save_100.pth \
--model_depth 50 --n_classes 700 --batch_size 128 --n_threads 4 --checkpoint 5
```

Calculate top-5 class probabilities of each video using a trained model (~/data/results/save_200.pth.)  
Note that ```inference_batch_size``` should be small because actual batch size is calculated by ```inference_batch_size * (n_video_frames / inference_stride)```.

```bash
python main.py --root_path ~/data --video_path kinetics_videos/jpg --annotation_path kinetics.json \
--result_path results --dataset kinetics --resume_path results/save_200.pth \
--model_depth 50 --n_classes 700 --n_threads 4 --no_train --no_val --inference --output_topk 5 --inference_batch_size 1
```

Evaluate top-1 video accuracy of a recognition result (~/data/results/val.json).

```bash
python -m util_scripts.eval_accuracy ~/data/kinetics.json ~/data/results/val.json --subset val -k 1 --ignore
```

Fine-tune fc layers of a pretrained model (~/data/models/resnet-50-kinetics.pth) on UCF-101.

```bash
python main.py --root_path ~/data --video_path ucf101_videos/jpg --annotation_path ucf101_01.json \
--result_path results --dataset ucf101 --n_classes 101 --n_pretrain_classes 700 \
--pretrain_path models/resnet-50-kinetics.pth --ft_begin_module fc \
--model resnet --model_depth 50 --batch_size 128 --n_threads 4 --checkpoint 5


python main.py --video_path /home/plass-oneshot/jsw/3D-ResNets-PyTorch/prepared_dataset \ # jpg
  --annotation_path /home/plass-oneshot/jsw/3D-ResNets-PyTorch/dst_json/ucf101_01.json \ # json
  --result_path results \
  --dataset ucf101 \ # dataset
  --n_classes 101 \ # n_classes
  --n_pretrain_classes 700 \ 
  --pretrain_path /home/plass-oneshot/jsw/3D-ResNets-PyTorch/pth/r3d50_K_200ep.pth \
  --ft_begin_module fc \ # fc
  --model resnet --model_depth 50 --batch_size 128 --n_threads 4 --checkpoint 5


python main.py --video_path /home/plass-oneshot/jsw/3D-ResNets-PyTorch/prepared_dataset/ucf101 --annotation_path /home/plass-oneshot/jsw/3D-ResNets-PyTorch/dst_json/ucf101_01.json --result_path ./results/test/ \
  --dataset ucf101 --n_classes 101   --n_pretrain_classes 700 --pretrain_path /home/plass-oneshot/jsw/3D-ResNets-PyTorch/pth/r3d50_K_200ep.pth \
  --ft_begin_module fc   --model resnet --model_depth 50 --batch_size 128 --n_threads 4 --checkpoint 5


python main.py --video_path /home/plass-oneshot/jsw/3D-ResNets-PyTorch/prepared_dataset/export_v2 --annotation_path /home/plass-oneshot/jsw/3D-ResNets-PyTorch/export_01.json --result_path ./results/test \
  --dataset ucf101 --n_classes 2   --n_pretrain_classes 700 --pretrain_path /home/plass-oneshot/jsw/3D-ResNets-PyTorch/pth/r3d50_K_200ep.pth \
  --ft_begin_module fc   --model resnet --model_depth 50 --batch_size 128 --n_threads 4 --checkpoint 5 \
  --n_epochs 200


python main.py --video_path /home/plass-oneshot/jsw/3D-ResNets-PyTorch/prepared_dataset/export_v2 --annotation_path /home/plass-oneshot/jsw/3D-ResNets-PyTorch/export_01.json  --dataset ucf101 --n_classes 2  \
  --ft_begin_module fc  --batch_size 128 --n_threads 4 \
  --checkpoint 25 \
  --result_path ./results/resnet18/r3d34_K_200ep \
  --pretrain_path /home/plass-oneshot/jsw/3D-ResNets-PyTorch/pth/r3d34_K_200ep.pth \
--model resnet --model_depth 34 --n_pretrain_classes 700\
  --n_epochs 200


python main.py --video_path /home/plass-oneshot/jsw/3D-ResNets-PyTorch/prepared_dataset/export_v2 --annotation_path /home/plass-oneshot/jsw/3D-ResNets-PyTorch/export_01.json  --dataset ucf101 --n_classes 2  \
  --ft_begin_module fc  --batch_size 128 --n_threads 4 \
  --checkpoint 25 \
  --result_path ./results/aug \
  --pretrain_path /home/plass-oneshot/jsw/3D-ResNets-PyTorch/pth/r2p1d50_KM_200ep.pth \
  --model resnet2p1d --model_depth 50 --n_pretrain_classes 1039 \
  --n_epochs 200
```

python -m util_scripts.eval_accuracy ~/data/kinetics.json ~/data/results/val.json --subset val -k 1 --ignore


### pretrain
#### 50
r3d50_K_200ep.pth: --model resnet --model_depth 50 --n_pretrain_classes 700
r3d50_KM_200ep.pth: --model resnet --model_depth 50 --n_pretrain_classes 1039
r3d50_KMS_200ep.pth: --model resnet --model_depth 50 --n_pretrain_classes 1139
r3d50_KS_200ep.pth: --model resnet --model_depth 50 --n_pretrain_classes 800
r3d50_M_200ep.pth: --model resnet --model_depth 50 --n_pretrain_classes 339
r3d50_MS_200ep.pth: --model resnet --model_depth 50 --n_pretrain_classes 439
r3d50_S_200ep.pth: --model resnet --model_depth 50 --n_pretrain_classes 100

r3d18_K_200ep.pth: --model resnet --model_depth 18 --n_pretrain_classes 700
r3d18_KM_200ep.pth: --model resnet --model_depth 18 --n_pretrain_classes 1039

r3d34_K_200ep.pth: --model resnet --model_depth 34 --n_pretrain_classes 700
r3d34_KM_200ep.pth: --model resnet --model_depth 34 --n_pretrain_classes 1039

#### 101
r3d101_K_200ep.pth: --model resnet --model_depth 101 --n_pretrain_classes 700
r3d101_KM_200ep.pth: --model resnet --model_depth 101 --n_pretrain_classes 1039

#### 152
r3d152_K_200ep.pth: --model resnet --model_depth 152 --n_pretrain_classes 700
r3d152_KM_200ep.pth: --model resnet --model_depth 152 --n_pretrain_classes 1039

#### 200
r3d200_K_200ep.pth: --model resnet --model_depth 200 --n_pretrain_classes 700
r3d200_KM_200ep.pth: --model resnet --model_depth 200 --n_pretrain_classes 1039