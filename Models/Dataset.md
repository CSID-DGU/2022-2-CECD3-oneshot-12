
## dataset
유치장 내 유치인 이상행위 데이터

### Supported Skeleton Datasets
[GitHub - kennymckormick/pyskl: A toolbox for skeleton-based action recognition.](https://github.com/kennymckormick/pyskl)
* NTURGB+D (CVPR 2016):  [NTU RGB+D: A large scale dataset for 3D human activity analysis](https://openaccess.thecvf.com/content_cvpr_2016/papers/Shahroudy_NTU_RGBD_A_CVPR_2016_paper.pdf) 
* NTURGB+D 120 (TPAMI 2019):  [Ntu rgb+ d 120: A large-scale benchmark for 3d human activity understanding](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8713892) 
* Kinetics 400 (CVPR 2017):  [Quo vadis, action recognition? a new model and the kinetics dataset](https://openaccess.thecvf.com/content_cvpr_2017/papers/Carreira_Quo_Vadis_Action_CVPR_2017_paper.pdf) 
* UCF101 (ArXiv 2012):  [UCF101: A dataset of 101 human actions classes from videos in the wild](https://arxiv.org/pdf/1212.0402.pdf) 
* HMDB51 (ICCV 2021):  [HMDB: a large video database for human motion recognition](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6126543) 
* FineGYM (CVPR 2020):  [Finegym: A hierarchical video dataset for fine-grained action understanding](https://openaccess.thecvf.com/content_CVPR_2020/papers/Shao_FineGym_A_Hierarchical_Video_Dataset_for_Fine-Grained_Action_Understanding_CVPR_2020_paper.pdf) 
* Diving48 (ECCV 2018):  [Resound: Towards action recognition without representation bias](https://openaccess.thecvf.com/content_ECCV_2018/papers/Yingwei_Li_RESOUND_Towards_Action_ECCV_2018_paper.pdf) 

### OpenDataset about Action Recognition
[Action Recognition | Papers With Code](https://paperswithcode.com/task/action-recognition-in-videos)

* Kinetics
[Kinetics](https://www.deepmind.com/open-source/kinetics)

* Action Recognition on NTU RGB+D
> **NTU RGB+D** is a large-scale dataset for RGB-D human action recognition. It involves 56,880 samples of 60 action classes collected from 40 subjects. The actions can be generally divided into three categories: 40 daily actions (e.g., drinking, eating, reading), nine health-related actions (e.g., sneezing, staggering, falling down), and 11 mutual actions (e.g., punching, kicking, hugging). These actions take place under 17 different scene conditions corresponding to 17 video sequences (i.e., S001–S017). The actions were captured using three cameras with different horizontal imaging viewpoints, namely, −45∘,0∘, and +45∘. Multi-modality information is provided for action characterization, including depth maps, 3D skeleton joint position, RGB frames, and infrared sequences. The performance evaluation is performed by a cross-subject test that split the 40 subjects into training and test groups, and by a cross-view test that employed one camera (+45∘) for testing, and the other two cameras for training.
sota: 97%, PoseC3D
[NTU RGB+D Benchmark (Action Recognition) | Papers With Code](https://paperswithcode.com/sota/action-recognition-in-videos-on-ntu-rgbd)


* something-something v2
> The 20BN-SOMETHING-SOMETHING V2 dataset is a large collection of labeled video clips that show humans performing pre-defined basic actions with everyday objects. The dataset was created by a large number of crowd workers. It allows machine learning models to develop fine-grained understanding of basic actions that occur in the physical world. It contains 220,847 videos, with 168,913 in the training set, 24,777 in the validation set and 27,157 in the test set. There are 174 labels.
sota : 75%, VideoMAE
특징: 비디오 영상 데이터, there’s an object annotation in addition to the video label.
[Something-Something V2 Benchmark (Action Recognition) | Papers With Code](https://paperswithcode.com/sota/action-recognition-in-videos-on-something)

* UCF101
> **UCF101** dataset is an extension of UCF50 and consists of 13,320 video clips, which are classified into 101 categories. These 101 categories can be classified into 5 types (Body motion, Human-human interactions, Human-object interactions, Playing musical instruments and Sports). The total length of these video clips is over 27 hours. All the videos are collected from YouTube and have a fixed frame rate of 25 FPS with the resolution of 320 × 240.
sota: 98%, SMART
특징: 
[UCF101 Benchmark (Action Recognition) | Papers With Code](https://paperswithcode.com/sota/action-recognition-in-videos-on-ucf101)

* HMDB-51
> The **HMDB51** dataset is a large collection of realistic videos from various sources, including movies and web videos. The dataset is composed of 6,849 video clips from 51 action categories (such as “jump”, “kiss” and “laugh”), with each category containing at least 101 clips. The original evaluation scheme uses three different training/testing splits. In each split, each action class has 70 clips for training and 30 clips for testing. The average accuracy over these three splits is used to measure the final performance.
sota: 87%, DEEP-HAL with ODF+SDF
특징:
[HMDB-51 Benchmark (Action Recognition) | Papers With Code](https://paperswithcode.com/sota/action-recognition-in-videos-on-hmdb-51)

* Something-Something V1 (20BN-Something-Something Dataset V1)
> The 20BN-SOMETHING-SOMETHING dataset is a large collection of labeled video clips that show humans performing pre-defined basic actions with everyday objects. The dataset was created by a large number of crowd workers. It allows machine learning models to develop fine-grained understanding of basic actions that occur in the physical world. It contains 108,499 videos, with 86,017 in the training set, 11,522 in the validation set and 10,960 in the test set. There are 174 labels.
> ⚠️ Attention: This is the outdated V1 of the dataset. V2 is available  [here](https://paperswithcode.com/dataset/something-something-v2).
sota: 60%, Uniformer-B
특징:
[Something-Something V1 Benchmark (Action Recognition) | Papers With Code](https://paperswithcode.com/sota/action-recognition-in-videos-on-something-1)

* Action Recognition on EPIC-KITCHENS-100
> 
sota: 53% , M&M
특징: 상당히 방대한 범위의 데이터인듯
[EPIC-KITCHENS-100 Benchmark (Action Recognition) | Papers With Code](https://paperswithcode.com/sota/action-recognition-on-epic-kitchens-100)

* Action Recognition on AVA v2.2
> 
sota: 39MAP, VideoMAE
[AVA v2.2 Benchmark (Action Recognition) | Papers With Code](https://paperswithcode.com/sota/action-recognition-on-ava-v2-2)

* Action Recognition on ActivityNet
> 
sota: 94MAP, NSNet
[ActivityNet Benchmark (Action Recognition) | Papers With Code](https://paperswithcode.com/sota/action-recognition-in-videos-on-activitynet)

* Action Recognition on Jester
sota: 98VAL
[Jester Benchmark (Action Recognition) | Papers With Code](https://paperswithcode.com/sota/action-recognition-in-videos-on-jester)

