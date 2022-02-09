import numpy as np  # numpy
import matplotlib.pyplot as plt  # plots for visualizationpath
import os  # for path folders
import pathlib
import glob

import cv2   # computer vision or OpenCv
import torch # PyTorch DeepLearning
from torchvision import transforms, datasets # laod data and transform to tensor
from torch.utils.data import DataLoader # for batch_size data
from torchvision.utils import make_grid

import torch.nn as nn  # MOdel
from torch import optim  # optimizer
from torchsummary import summary 

from torch.autograd import Variable
import torch.nn.functional as F  
from PIL import Image 

train_transforms = transforms.Compose([transforms.Grayscale(num_output_channels=1),
                                       transforms.Resize((224,224)),
                                       transforms.RandomRotation(30),
                                       transforms.RandomHorizontalFlip(),
                                       transforms.ToTensor(),
                                       transforms.Normalize([0.5],
                                                            [0.5])
                                       ])
test_transforms = transforms.Compose([transforms.Grayscale(num_output_channels=1),
                                       transforms.Resize((224,224)),
                                       transforms.ToTensor(),
                                       transforms.Normalize([0.5],
                                                            [0.5])
                                       ])

path ='data/'
train_data = datasets.ImageFolder(path+'Train', transform=train_transforms)
test_data = datasets.ImageFolder(path+'Test', transform=test_transforms)

train_loader = DataLoader(train_data, batch_size=32, shuffle=True)
test_loader  = DataLoader(test_data, batch_size=32, shuffle=True)

images, labels = next(iter(test_loader))
print(images.shape)
print(len(labels))

image = Image.open(path+'Train/pushup/pushup1.jpg')
image_tensor = test_transforms(image).float()

# image_tensor =image_tensor.unsqueeze(0)
print(image_tensor.shape)
input = Variable(image_tensor)