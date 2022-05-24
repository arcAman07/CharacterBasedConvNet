import json
import torch
import torch.nn as nn

class largeCharacterLevelCNN(nn.Module):
  def __init__(self, args, number_of_classes):
    super(largeCharacterLevelCNN, self).__init__()

  # define conv layers

  self.dropout_input = nn.Dropout2D(args.dropout_input)

  self.conv1 = nn.Conv2d


