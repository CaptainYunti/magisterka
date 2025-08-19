import torch
import numpy as np
import matplotlib.pyplot as plt
from torch import nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import copy

import my_models
import data_prep
import visualizer
from train_test import train, test

device = (
    "cuda"
    if torch.cuda.is_available()
    else "cpue"
)

print(f"Device: {device}")

BATCH = 2048
EPOCHS = 100

sr = 44100

max_track_number = 9





classes = ("other", "verse", "chorus", "other vocals")


first_model = my_models.ReluNet().to(device) # 1024, 1024, 128
second_model = my_models.Relu6Net().to(device) # 1024, 1024, 128
third_model = my_models.GeluNet().to(device) # 1024, 1024, 128

fourth_model = my_models.ReluBiggerNet().to(device) # 1024, 2048, 1024, 128
fifth_model = my_models.Relu6BiggerNet().to(device) # 1024, 2048, 1024, 128
sixth_model = my_models.GeluBiggerNet().to(device) # 1024, 2048, 1024, 128

seventh_model = my_models.ReluSmallerNet().to(device) # 128, 128, 64
eighth_model = my_models.Relu6SmallerNet().to(device) # 128, 128, 64
ninth_model = my_models.GeluSmallerNet().to(device) # 128, 128, 64

models = [first_model, second_model, third_model, fourth_model, fifth_model, sixth_model, seventh_model, eighth_model, ninth_model]
copy_models = copy.deepcopy(models)

loss = nn.CrossEntropyLoss()
# optimizers_sgd = [optim.SGD(model.parameters(), lr=0.0001, momentum=0.9) for model in models]
# optimizers_adam = [optim.Adam(model.parameters(), lr=1e-4) for model in models]


mlp_names = ["SGD-ReLU", "SGD-ReLU6", "SGD-GELU",
              "SGD-ReLU-Bigger", "SGD-ReLU6-Bigger", "SGD-GELU-Bigger",
              "SGD-ReLU-Smaller", "SGD-ReLU6-Smaller", "SGD-GELU-Smaller",
              "Adam-ReLU", "Adam-ReLU6", "Adam-GELU",
              "Adam-ReLU-Bigger", "Adam-ReLU6-Bigger", "Adam-GELU-Bigger",
              "Adam-ReLU-Smaller", "Adam-ReLU6-Smaller", "Adam-GELU-Smaller",
              "ReLU-untrained", "ReLU6-untrained", "GELU-untrained",
              "ReLU-Bigger-untrained", "ReLU6-Bigger-untrained", "GELU-Bigger-untrained",
              "ReLU-Smaller-untrained", "ReLU6-Smaller-untrained", "GELU-Smaller-untrained"]


for track_number in range(max_track_number+1):

    train_data, test_data = data_prep.get_data(track_number, normalize=True)

    train_loader = DataLoader(train_data, batch_size=BATCH, shuffle=False)
    test_loader = DataLoader(test_data, batch_size=BATCH, shuffle=False)

    models = copy.deepcopy(copy_models)
    optimizers_sgd = [optim.SGD(model.parameters(), lr=0.0001, momentum=0.9) for model in models]

    for model_index, model in enumerate(models):
        optimizer = optimizers_sgd[model_index]
        print(f"Model: {print(model)}\n\n")

        for epoch in range(EPOCHS):
            train(train_loader, model, loss, optimizer, epoch, device)

        test_result = test(test_loader, model, loss, 1, device)[2]

        print("Done!")

        data_prep.data_visualization(track_number, test_result, mlp_names[model_index])
        torch.save(model.state_dict(), f"./models/{mlp_names[model_index]}_{track_number}.pth")

    models = copy.deepcopy(copy_models)
    optimizers_adam = [optim.Adam(model.parameters(), lr=1e-4) for model in models]

    for model_index, model in enumerate(models):
        optimizer = optimizers_adam[model_index]
        print(f"Model: {print(model)}\n\n")

        for epoch in range(EPOCHS):
            train(train_loader, model, loss, optimizer, epoch, device)
        test_result = test(test_loader, model, loss, 1, device)[2]

        print("Done!")

        data_prep.data_visualization(track_number, test_result, mlp_names[model_index+18])
        torch.save(model.state_dict(), f"./models/{mlp_names[model_index+18]}_{track_number}.pth")


    models = copy.deepcopy(copy_models)

    for model_index, model in enumerate(models):

        print(f"Model: {print(model)}\n\n")
        test_result = test(test_loader, model, loss, 1, device)[2]

        print("Done!")

        data_prep.data_visualization(track_number, test_result, mlp_names[model_index+9])



# train_data, test_data = data_prep.get_data(0, normalize=True)
# test_loader = DataLoader(test_data, batch_size=BATCH, shuffle=False)
# model = my_models.ReluNet().to(device)
# model.load_state_dict(torch.load("./models/Adam-ReLU_0.pth", weights_only=True))
# test_result = test(test_loader, model, loss, 1, device)[2]
# data_prep.data_visualization(0, test_result, "Adam-test")




# for(indx, model) in enumerate(models):
#     print(f"Model: {print(model)}\n\n")
    
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

