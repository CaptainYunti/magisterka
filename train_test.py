import torch
from torch import nn
from torch.utils.data import DataLoader
import visualizer


def train(dataloader: DataLoader, model: nn.Module, loss_fn, optimizer, epoch, device="cpu"):
    size = len(dataloader.dataset)
    model.train()
    for batch, (X,y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)

        pred = model(X)
        loss = loss_fn(pred, y)

        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        if batch % 1000 == 0:
            loss, current = loss.item(), (batch+1) * len(X)
            print(f"loss: {loss:>7f} [{current:>5d}/{size:>5d}]")

            # visualizer.writer.add_scalar(f"training loss {model.__class__.__name__}", loss, epoch * len(dataloader) + batch)
            # visualizer.writer.add_figure("Predictions vs. actuals", visualizer.plot_classes_preds(model, X, y),
            #                              global_step=epoch * len(dataloader) + batch)


def test(dataloader: DataLoader, model: nn.Module, loss_fn, epoch, device="cpu"):
    class_predictions = []
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()

    test_loss, correct = 0, 0

    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
            class_predictions = class_predictions + pred.argmax(1).tolist()

    test_loss /= num_batches
    correct /= size

    print(f"Test Error: \n Accuracy: {100*correct:>0.2f}%, AVG loss: {test_loss:>8f} \n")
    
    # visualizer.writer.add_scalar(f"test accuracy {model.__class__.__name__}", correct*100, epoch+1)

    return correct, test_loss, class_predictions

