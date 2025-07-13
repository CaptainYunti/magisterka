import torch
import numpy as np
import matplotlib.pyplot as plt
from torch import nn
import torch.optim as optim

import my_models
import data_prep

import visualizer
from train_test import train, test

device = (
    "cuda"
    if torch.cuda.is_available()
    else "cpue"
)


BATCH = 1
EPOCHS = 1

#train_loader = 
#test_loader


classes = ("other", "verse", "chorus", "other vocals")

print(f"Device: {device}")


first_model = my_models.FirstNet().to(device) # 1024, 1024, 128, GELU

models = [first_model]

loss = nn.CrossEntropyLoss()
optimizers = [optim.SGD(model.parameters(), lr=0.01, momentum=0.9) for model in models]

for(indx, model) in enumerate(models):
    print(f"Model: {print(model)}\n\n")
    
    # cross-validation
    # train 9 songs
    # test 1 song
    # some wykresy i tabele


# for indx, model in enumerate(models):
#     print(f"Model: {print(model)}\n\n")
#     for t in range(EPOCHS):
#         print(f"Epoch {t+1}\n------------------------------------")
#         train(train_loader, model, loss, optimizers[indx], t, device)
#         test(test_loader, model, loss, t, device)
#         print("Done!\n\n")


# torch.save(model_big.state_dict(), "./models/model_big_SGD.pth")