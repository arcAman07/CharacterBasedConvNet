import json
import torch
import torch.nn as nn

class largeCharacterLevelCNN(nn.Module):
  def __init__(self, args, number_of_classes):
    super(largeCharacterLevelCNN, self).__init__()

  # define conv layers

