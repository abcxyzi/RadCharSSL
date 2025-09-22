#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RadCharSSL Data Loader
MLSP 2025 - "Few-Shot Radar Signal Recognition through Self-Supervised Learning and Radio Frequency Domain Adaptation"
This script selectively loads RadChar data for pre-training, fine-tuning and evaluation
Created on August 31, 2025
@author: Zi Huang
"""

import h5py
import torch 
import numpy as np
from torch.utils.data import Dataset

class RadCharDataset(Dataset):
    def __init__(self, file_path: str):
        self.file_path = file_path
        with h5py.File(self.file_path, 'r') as file:
            self.data = file['iq'][:]
            self.labels = file['labels'][:]
        file.close()
    
    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        frame = {
            'iq_real': torch.tensor(np.real(self.data[idx]), dtype=torch.float32),   # Real signal part only
            'iq_imag': torch.tensor(np.imag(self.data[idx]), dtype=torch.float32),   # Imaginary signal part only
            'iq_cplx': torch.tensor(self.data[idx], dtype=torch.cfloat),             # Complex signal
            'label': torch.tensor(self.labels[idx], dtype=torch.float32),            # Radar parameters   
            'label_class': torch.tensor(self.labels[idx][1], dtype=torch.int64),     # Class label
            'snr': torch.tensor(self.labels[idx][-1], dtype=torch.float32),          # SNR value
        }
        return frame

class RadCharDataModule():
    def __init__(self, data_path: str):
        # Path to .h5 data file location
        self.data_path = data_path

    def loadPretrainingSet(self):
        """For pre-training without labels"""
        return RadCharDataset(self.data_path + "RadChar-SSL.h5")

    def loadFinetuningSet(self, fewshot: int):
        """For few-shot fine-tuning"""
        if fewshot == 1:
            # NOTE: Download .h5 file from https://www.kaggle.com/datasets/abcxyzi/radcharssl-mlsp-2025
            return RadCharDataset(self.data_path + "RadChar-1shot.h5")
        elif fewshot == 5:
            # NOTE: Download .h5 file from https://www.kaggle.com/datasets/abcxyzi/radcharssl-mlsp-2025
            return RadCharDataset(self.data_path + "RadChar-5shot.h5")
        elif fewshot == 10:
            # NOTE: Download .h5 file from https://www.kaggle.com/datasets/abcxyzi/radcharssl-mlsp-2025
            return RadCharDataset(self.data_path + "RadChar-10shot.h5")
        else:
            raise ValueError("Argument fewshot must be one of [1, 5, 10]")

    def loadEvaluationSet(self):
        """For evaluation of fine-tuned models"""
        # NOTE: Download .h5 file from https://www.kaggle.com/datasets/abcxyzi/radcharssl-mlsp-2025
        return RadCharDataset(self.data_path + "RadChar-testset.h5")
    
if __name__ == "__main__":    
    # NOTE: Change the path as required
    RadCharSSL = RadCharDataModule(data_path="./radcharssl/") 
    
    # For pre-training
    ds_pretrain = RadCharSSL.loadPretrainingSet()
    
    # For few-shot fine-tuning
    ds_finetune_1shot = RadCharSSL.loadFinetuningSet(fewshot=1)
    ds_finetune_5shot = RadCharSSL.loadFinetuningSet(fewshot=5)
    ds_finetune_10shot = RadCharSSL.loadFinetuningSet(fewshot=10)

    # Inspect test set
    ds_eval = RadCharSSL.loadEvaluationSet()

    # Example usage, to access the I/Q data and class label of the k-th index
    ds = ds_eval
    for k in range(10):
        print("Frame:", k)
        print("Available keys:", ds[k].keys())
        print("Complex I/Q data (shape):", ds[k]["iq_cplx"].shape)
        print("Corresponding class label:", ds[k]["label_class"])
        print("Corresponding SNR label:", ds[k]["snr"], "\n")