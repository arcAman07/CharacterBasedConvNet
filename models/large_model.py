import json
import torch
import torch.nn as nn

class LargeCharacterConvnet(TextClassificationBase):
  def __init__(self):
    super(LargeCharacterConvnet, self).__init__()
    self.dropout_input = nn.Dropout2d(0.5)

    # Defining the convolutional layers

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

    self.output_dimension = self._get_conv_output(input_shape)

    # Define the fully connected layers

    self.fc1 = nn.Sequential(
      nn.Linear(self.output_dimension, 2048),
      nn.ReLU(),
      nn.Dropout(0.5),
      
    )
    self.fc2 = nn.Sequential(nn.Linear(2048,2048), nn.ReLU(), nn.Dropout(0.5))

    self.fc3 = nn.Linear(2048, 2)

    # initialize weights

    self._create_weights()



  # utility private functions
  def _create_weights(self, mean=0.0, std=0.05):
    for module in self.modules():
      if isinstance(module, nn.Conv1d) or isinstance(module, nn.Linear):
        module.weight.data.normal_(mean, std)

  def _get_conv_output(self, shape):
    x = torch.rand(shape)
    x = x.transpose(1, 2)
    x = self.conv1(x)
    x = self.conv2(x)
    x = self.conv3(x)
    x = self.conv4(x)
    x = self.conv5(x)
    x = self.conv6(x)
    x = x.view(x.size(0), -1)
    output_dimension = x.size(1)
    return output_dimension
  # forward

  def forward(self, x):
    x = self.dropout_input(x)
    x = x.transpose(1, 2)
    x = self.conv1(x)
    x = self.conv2(x)
    x = self.conv3(x)
    x = self.conv4(x)
    x = self.conv5(x)
    x = self.conv6(x)
    x = x.view(x.size(0), -1)
    x = self.fc1(x)
    x = self.fc2(x)
    x = self.fc3(x)
    return x



