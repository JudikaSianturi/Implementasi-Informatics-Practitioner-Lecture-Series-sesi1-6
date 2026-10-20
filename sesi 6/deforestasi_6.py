"""Studi kasus klasifikasi citra satelit untuk penyebab deforestasi.
Jalankan di Google Colab setelah dataset disusun per kelas di /content/dataset.
"""
import torch
import torch.nn as nn
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader, random_split
from sklearn.metrics import classification_report

torch.manual_seed(42)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
DATA_DIR = "/content/dataset"
BATCH_SIZE = 16
EPOCHS = 5

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

dataset = datasets.ImageFolder(root=DATA_DIR, transform=transform)
print("Jumlah citra:", len(dataset))
print("Kelas:", dataset.classes)
if len(dataset) < 10 or len(dataset.classes) < 2:
    raise ValueError("Dataset perlu minimal 10 citra dan 2 kelas. Periksa folder dataset.")

train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size
train_data, test_data = random_split(dataset, [train_size, test_size], generator=torch.Generator().manual_seed(42))
train_loader = DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True)
test_loader = DataLoader(test_data, batch_size=BATCH_SIZE, shuffle=False)

# ResNet18 menggunakan bobot pralatih; internet mungkin diperlukan saat pertama kali.
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
model.fc = nn.Linear(model.fc.in_features, len(dataset.classes))
model = model.to(device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)

for epoch in range(EPOCHS):
    model.train()
    total_loss = 0.0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch + 1}/{EPOCHS} - Loss: {total_loss / max(1, len(train_loader)):.4f}")

model.eval()
y_true, y_pred = [], []
with torch.no_grad():
    for images, labels in test_loader:
        outputs = model(images.to(device))
        y_pred.extend(outputs.argmax(dim=1).cpu().tolist())
        y_true.extend(labels.tolist())

print("\nLaporan evaluasi:")
print(classification_report(y_true, y_pred, labels=list(range(len(dataset.classes))), target_names=dataset.classes, zero_division=0))
torch.save({"model_state_dict": model.state_dict(), "classes": dataset.classes}, "model_deforestasi.pth")
print("Model tersimpan: model_deforestasi.pth")
