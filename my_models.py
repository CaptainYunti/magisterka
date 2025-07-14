import torch
import torch.nn as nn
import torch.nn.functional as F


class GeluNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.training_stack = nn.Sequential(
            nn.Linear(13,1024),
            nn.GELU(),
            nn.Linear(1024,1024),
            nn.GELU(),
            nn.Linear(1024,128),
            nn.GELU(),
            nn.Linear(128,4)
        )

    def forward(self, x):
        return self.training_stack(x)
    

class ReluNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.training_stack = nn.Sequential(
            nn.Linear(13,1024),
            nn.ReLU(),
            nn.Linear(1024,1024),
            nn.ReLU(),
            nn.Linear(1024,128),
            nn.ReLU(),
            nn.Linear(128,4)
        )

    def forward(self, x):
        return self.training_stack(x)
    

class Relu6Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.training_stack = nn.Sequential(
            nn.Linear(13,1024),
            nn.ReLU6(),
            nn.Linear(1024,1024),
            nn.ReLU6(),
            nn.Linear(1024,128),
            nn.ReLU6(),
            nn.Linear(128,4)
        )

    def forward(self, x):
        return self.training_stack(x)
    
    


class GeluBiggerNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.training_stack = nn.Sequential(
            nn.Linear(13,1024),
            nn.GELU(),
            nn.Linear(1024,2048),
            nn.GELU(),
            nn.Linear(2048,1024),
            nn.GELU(),
            nn.Linear(1024,128),
            nn.GELU(),
            nn.Linear(128,4)
        )

    def forward(self, x):
        return self.training_stack(x)
    

class ReluBiggerNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.training_stack = nn.Sequential(
            nn.Linear(13,1024),
            nn.ReLU(),
            nn.Linear(1024,2048),
            nn.ReLU(),
            nn.Linear(2048,1024),
            nn.ReLU(),
            nn.Linear(1024,128),
            nn.ReLU(),
            nn.Linear(128,4)
        )

    def forward(self, x):
        return self.training_stack(x)
    

class Relu6BiggerNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.training_stack = nn.Sequential(
            nn.Linear(13,1024),
            nn.ReLU6(),
            nn.Linear(1024,2048),
            nn.ReLU6(),
            nn.Linear(2048,1024),
            nn.ReLU6(),
            nn.Linear(1024,128),
            nn.ReLU6(),
            nn.Linear(128,4)
        )

    def forward(self, x):
        return self.training_stack(x)