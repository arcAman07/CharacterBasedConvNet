import json
import torch
import torch.nn as nn

class LargeCharacterConvnet(TextClassificationBase):
  def __init__(self):
    super(LargeCharacterConvnet, self).__init__()
    self.dropout_input = nn.Dropout2d(0.5)
    self.conv1 = nn.Sequential(
      nn.Conv1d(
        1014,
        1024,
        kernel_size = 7,
        padding = 0,
      ),
      nn.ReLU(),
      nn.MaxPool1d(3),
    )
    self.conv2 = nn.Sequential(
      nn.Conv1d(
        1024,
        1024,
        kernel_size = 7,
        padding = 0,
      ),
      nn.ReLU(),
      nn.MaxPool1d(3),
    )
    self.conv3 = nn.Sequential(
      nn.Conv1d(
        1024,
        1024,
        kernel_size = 3,
        padding = 0,
      ),
      nn.ReLU(),
    ),
    self.conv4 = nn.Sequential(
      nn.Conv1d(
        1024,
        1024,
        kernel_size = 3,
        padding = 0,
      ),
      nn.ReLU(),
    )
    self.conv5 = nn.Sequential(
      nn.Conv1d(
        1024,
        1024,
        kernel_size = 3,
        padding = 0,
      ),
      nn.ReLU(),
    )
    self.conv6 = nn.Sequential(
      nn.Conv1d(
        1024,
        1024,
        kernel_size = 3,
        padding = 0,
      ),
      nn.ReLU(),
      nn.MaxPool1d(3)
    )

    input_shape = (
            128,
            1014,
            70,
        )



