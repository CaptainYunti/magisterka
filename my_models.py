import torch
import torch.nn as nn
import torch.nn.functional as F


class FirstNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.training_stack == nn.Sequential(
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