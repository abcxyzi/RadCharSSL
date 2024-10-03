# Self-Supervised Radar Signal Recognition

This repo contains radar datasets accompanying the paper "Radar Signal Recognition through Self-Supervised Learning and Domain Adaptation", submitted to the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP 2025). 

We will release a preview of our paper soon. Stay tuned for updates.

## Overview

Four datasets were considered in our paper:

1. **RadioML** - this contains telecommunications signals only.
2. **DeepRadar** - this contains radar signals only.
3. **RadarComm** - this contains a mixture of telecommunications and radar signals.
4. **RadChar** (ours) - this contains radar signals only.

RadChar contains several variants used to support self-supervised pre-training, few-shot fine-tuning, and model evaluation:

- RadChar-SSL - this is used for pre-training only.
- RadChar-nShot - this is used for few-shot fine-tuning only, where n = 1, 5, 10.
- RadChar-Eval - this is used for evaluation only.

Note, RadChar dataset variants were derived from our [previous work](https://github.com/abcxyzi/RadChar).

## RadioML (Comm Data)

RadioML 2018.01A (**RadioML**) is a dataset created by [DeepSig Inc](https://www.deepsig.ai/). This dataset was introduced in [Over-the-Air Deep Learning Based Radio Signal Classification](https://ieeexplore.ieee.org/document/8267032), published in the 2017 IEEE Journal of Selected Topics in Signal Processing.

RadioML contains the following characteristics:
- 24 classes
- 26 SNR levels (-20 to 30 dB with a 2 dB resolution)
- 1,024 I/Q samples per frame
- 1 μs in temporal resolution 

RadioML is provided as a single file `GOLD_XYZ_OSC.0001_1024.hdf5` (21.45 GB), it can be downloaded from: https://www.kaggle.com/datasets/pinxau1000/radioml2018

10% of RadioML were used for self-supervised pre-training in our paper.

## DeepRadar (Radar Data)

**DeepRadar** is a dataset created by the [Radar and Microwave Group](http://www.gmr.ssr.upm.es:8080/?language=EN). This dataset was introduced in [LSTM Framework for Classification of Radar and Communications Signals](https://ieeexplore.ieee.org/document/10149618), published in the 2023 IEEE Radar Conference (RadarConf23).

DeepRadar contains the following characteristics:
- 23 classes
- 17 SNR levels (-12 to 20 dB with a 2 dB resolution)
- 1,024 I/Q samples per frame
- 0.01 μs in temporal resolution

DeepRadar is provided in three parts (train, validation, and test). The individual `.mat` files can be downloaded from: https://www.kaggle.com/datasets/pinxau1000/radioml2018

The training set `X_train.mat` was used for self-supervised pre-training in our paper

## RadarComm (Comm & Radar Data)

**RadarComm** is a dataset created by [ANDRO Computational Solutions](https://www.androcs.com/wp/). This dataset was introduced in [Multi-task Learning Approach for Automatic Modulation and Wireless Signal Classification](https://ieeexplore.ieee.org/document/9500447), published in the 2021 IEEE International Conference on Communications (ICC).

RadarComm contains the following characteristics:
- 6 modulation classes and 8 signal classes (each frame is dual-annotated with a modulation class and a signal class)
- 17 SNR levels (-12 to 20 dB with a 2 dB resolution)
- 128 I/Q samples per frame
- 0.1 μs in temporal resolution

RadarComm contains several dataset variants provided in `.zip` files. They can be downloaded from: https://www.kaggle.com/datasets/pinxau1000/radioml2018

The RadarComm dataset with dynamic channel effects `RadComDynamic.zip` was used for self-supervised pre-training in our paper. Note, we use only the modulation class labels for few-shot fine-tuning. 

## RadChar (Radar Data)

**RadChar** is our own dataset. This was introduced in [Multi-Task Learning For Radar Signal Characterisation](https://ieeexplore.ieee.org/document/10193318), published in the 2023 IEEE International Conference on Acoustics, Speech, and Signal Processing Workshops (ICASSPW).

RadChar contains the following characteristics:
- 5 classes
- 41 SNR levels (-20 to 20 dB with a 1 dB resolution)
- 512 I/Q samples per frame
- 0.3 μs in temporal resolution

RadChar contains several sizes provided in `.h5` files. The baseline dataset is RadChar-Baseline which is given by `RadChar-Baseline.h5`. It can be downloaded from: https://github.com/abcxyzi/RadChar

We introduce several RadChar variants to support self-supervised pre-training, few-shot fine-tuning, and model evaluation in our paper, these include:

- RadChar-SSL - this is used for pre-training only
- RadChar-nShot - this is used for few-shot fine-tuning only, where n = 1, 5, 10
- RadChar-Eval - this is used for evaluation only

RadChar-SSL is a new dataset. RadChar-nShot and RadChar-Eval were created from a random 90-10 train-test split of RadChar-Baseline, respectively.

### RadChar-Eval 

RadChar-Eval is created from the 10% split of RadChar-Baseline. This is used as the evaluation dataset (i.e., test-set) in our paper.

RadChar-Eval can be downloaded from: `download link will be made available soon`

### RadChar-nShot 

RadChar-nShot contains three small-scale datasets used for few-shot fine-tuning. These datasets were created from the 90% split of RadChar-Baseline.

RadChar-nShot can be downloaded from: 
- 1-shot: `download link will be made available soon`
- 5-shot: `download link will be made available soon`
- 10-shot: `download link will be made available soon`

### RadChar-SSL

RadChar-SSL is a new synthetic RadChar-like dataset generated for self-supervised pre-training only. This dataset does not contain class annotations.

RadChar-SSL contains 500,000 frames, with the same characteristics as RadChar-Baseline:
- 5 classes
- 41 SNR levels (-20 to 20 dB with a 1 dB resolution)
- 512 I/Q samples per frame
- 0.3 μs in temporal resolution

## Citation

Please cite our conference paper if you find it helpful for your research. Cheers.

We will release a preview of our paper soon. Stay tuned for updates.