import numpy as np
import torch
import torchvision
import torchvision.transforms as transforms
from torchvision.models import vgg11, VGG11_Weights, resnet50, resnet18, efficientnet_b3, efficientnet_b2
from torch.optim import AdamW
from torch.nn import CrossEntropyLoss
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import torch.nn as nn
from customdataset import CustomDataset
from tqdm import tqdm
from torchvision.models import efficientnet_b0
def save_metrics(train_loss, val_loss, train_acc, val_acc):
    # 리스트를 numpy 배열로 변환
    train_losses = np.array(train_loss)
    val_losses = np.array(val_loss)
    train_accs = np.array(train_acc)
    val_accs = np.array(val_acc)

    # 각 epoch 별로 파일을 열어 데이터 추가
    with open(f'train_losses_epoch.txt', 'a') as f:
        np.savetxt(f, train_losses)
    with open(f'val_losses_epoch.txt', 'a') as f:
        np.savetxt(f, val_losses)
    with open(f'train_accs_epoch.txt', 'a') as f:
        np.savetxt(f, train_accs)
    with open(f'val_accs_epoch.txt', 'a') as f:
        np.savetxt(f, val_accs)
def train(model, train_loader, val_loader, epochs, DEVICE, optimizer, criterion) :
    best_val_acc = 0.0
    train_losses = []
    val_losses = []
    train_accs = []
    val_accs = []
    print("Train...")
    for epoch in range(epochs) :
        train_loss = 0.0
        val_loss = 0.0
        val_acc = 0.0
        train_acc = 0.0

        model.train()

        # tqdm
        train_loader_iter = tqdm(train_loader,
                                 desc=f"Epoch {epoch +1}/{epochs}", leave=False)

        for i, (data, target) in enumerate(train_loader_iter) :
            data = data.to(DEVICE)
            target = target.to(DEVICE)

            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()

            train_loss += loss.item()

            # acc
            _, pred = torch.max(output, 1)
            train_acc += (pred == target).sum().item()

            # print the loss
            if i % 10 == 9 :
               train_loader_iter.set_postfix({"Loss" : loss.item()})

        train_loss /= len(train_loader)
        train_acc = train_acc / len(train_loader.dataset)

        # eval
        model.eval()
        with torch.no_grad() :
            for data, target in val_loader :
                data = data.to(DEVICE)
                target = target.to(DEVICE)

                outputs = model(data)
                pred = outputs.argmax(dim=1, keepdim=True)
                val_acc += pred.eq(target.view_as(pred)).sum().item()
                val_loss += criterion(outputs, target).item()

        val_loss /= len(val_loader)
        val_acc = val_acc / len(val_loader.dataset)
        save_metrics(train_losses, val_losses, train_accs, val_accs)

        train_losses.append(train_loss)
        train_accs.append(train_acc)
        val_losses.append(val_loss)
        val_accs.append(val_acc)

        if val_acc > best_val_acc :
            torch.save(model.state_dict(), 'bestefficient0.pt')
            best_val_acc = val_acc



    return model, train_losses, val_losses, train_accs, val_accs

# Train Loss : 0.4077, Train Acc : 0.8465,
def main() :
    DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = efficientnet_b2(pretrained=True)
    model.classifier[1] = nn.Linear(in_features=1408, out_features=74)
    model.to(DEVICE)

    train_transform = transforms.Compose([
        transforms.Resize((300,300)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
        ),
    ])

    val_transform = transforms.Compose([
        transforms.Resize((300,300)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
        ),
    ])

    # dataset
    train_dataset = CustomDataset("../data/train_images/", transform=train_transform)
    val_dataset = CustomDataset("../data/val_images/", transform=val_transform)

    # dataloader
    train_loader = DataLoader(train_dataset, batch_size=54, num_workers=4,
                              pin_memory=True, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=54, num_workers=4,
                            pin_memory=True, shuffle=False)

    epochs = 100
    criterion = CrossEntropyLoss().to(DEVICE)
    optimizer = AdamW(model.parameters(), lr=0.001)

    train(model, train_loader, val_loader, epochs, DEVICE, optimizer, criterion)

if __name__ == "__main__" :
    main()