import torch
import torch.nn as nn
import torch.nn.functional as F

class ConvNet1(nn.Module):
    def __init__(self):
        super(ConvNet1, self).__init__()
        self.conv1 = nn.Conv1d(1, 16, 16)
        self.max_pool1 = nn.MaxPool1d(4,4)
        self.conv2 = nn.Conv1d(16, 32, 8)
        self.max_pool2 = nn.MaxPool1d(4,4)
        self.conv3 = nn.Conv1d(32, 64, 8)
        self.max_pool3 = nn.MaxPool1d(4,4)
        self.fc1 = nn.Linear(3904, 64)
        self.fc2 = nn.Linear(64, 1)
 
    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.max_pool1(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = self.max_pool2(x)
        x = self.conv3(x)
        x = F.relu(x)
        x = self.max_pool3(x)
        # resize
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        x = torch.sigmoid(x)
        return x
