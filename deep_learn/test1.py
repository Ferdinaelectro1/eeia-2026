"""
Entraînement d'un petit réseau de neurones (MLP) pour détecter si un
composant électronique est défectueux, à partir de :
  - tension (V)
  - température (°C)
  - niveau d'odeur (0-10)

100% CPU, pas besoin de GPU pour un réseau aussi petit.
"""

import csv
import torch
import torch.nn as nn
import random

torch.manual_seed(42)
device = torch.device("cpu")

# -----------------------------
# 1. Chargement des données CSV
# -----------------------------
X, y = [], []
with open("composants.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        X.append([
            float(row["tension_V"]),
            float(row["temperature_C"]),
            float(row["odeur_0_10"]),
        ])
        y.append(float(row["defectueux"]))

X = torch.tensor(X, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.float32).unsqueeze(1)  # shape (N, 1)

# -----------------------------
# 2. Normalisation des entrées
# -----------------------------
# Important : tension, température et odeur n'ont pas la même échelle.
# On centre-réduit chaque colonne (moyenne 0, écart-type 1) pour que
# l'entraînement converge bien plus vite et plus proprement.
X_mean = X.mean(dim=0)
X_std = X.std(dim=0)
X_norm = (X - X_mean) / X_std

# -----------------------------
# 3. Split train / test
# -----------------------------
n = X_norm.shape[0]
indices = list(range(n))
random.seed(42)
random.shuffle(indices)

n_train = int(0.8 * n)
train_idx, test_idx = indices[:n_train], indices[n_train:]

X_train, y_train = X_norm[train_idx], y[train_idx]
X_test, y_test = X_norm[test_idx], y[test_idx]

print(f"Train: {len(train_idx)} exemples | Test: {len(test_idx)} exemples")

# -----------------------------
# 4. Définition du réseau
# -----------------------------
# 3 entrées -> 8 neurones (couche cachée 1) -> 4 neurones (couche cachée 2) -> 1 sortie (sigmoid)
class DetecteurDefaut(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(3, 8),
            nn.ReLU(),
            nn.Linear(8, 4),
            nn.ReLU(),
            nn.Linear(4, 1),
            nn.Sigmoid(),
        )

    def forward(self, x):
        return self.net(x)

model = DetecteurDefaut().to(device)
print(model)

n_params = sum(p.numel() for p in model.parameters())
print(f"Nombre total de paramètres (poids + biais) : {n_params}")

# -----------------------------
# 5. Entraînement
# -----------------------------
criterion = nn.BCELoss()  # binary cross-entropy, adaptée à une sortie sigmoid 0/1
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

EPOCHS = 300

for epoch in range(1, EPOCHS + 1):
    model.train()
    optimizer.zero_grad()

    predictions = model(X_train)
    loss = criterion(predictions, y_train)

    loss.backward()   # backprop : calcule les gradients
    optimizer.step()  # met à jour les poids (w, b)

    if epoch % 50 == 0 or epoch == 1:
        with torch.no_grad():
            model.eval()
            test_preds = model(X_test)
            test_loss = criterion(test_preds, y_test)
            test_acc = ((test_preds > 0.5).float() == y_test).float().mean()
        print(f"Epoch {epoch:4d} | loss train: {loss.item():.4f} | loss test: {test_loss.item():.4f} | accuracy test: {test_acc.item()*100:.1f}%")

# -----------------------------
# 6. Évaluation finale
# -----------------------------
model.eval()
with torch.no_grad():
    test_preds = model(X_test)
    test_acc = ((test_preds > 0.5).float() == y_test).float().mean()
print(f"\nAccuracy finale sur le test set : {test_acc.item()*100:.2f}%")

# -----------------------------
# 7. Test sur des exemples concrets "à la main"
# -----------------------------
def predire(tension, temperature, odeur):
    x = torch.tensor([[tension, temperature, odeur]], dtype=torch.float32)
    x_norm = (x - X_mean) / X_std
    with torch.no_grad():
        proba = model(x_norm).item()
    verdict = "DEFECTUEUX" if proba > 0.5 else "BON"
    return proba, verdict

print("\n--- Exemples concrets ---")
exemples = [
    (12.0, 28.0, 0.2, "composant qu'on attend BON"),
    (9.0, 75.0, 7.5, "composant qu'on attend DEFECTUEUX (surchauffe + odeur forte)"),
    (11.7, 33.0, 1.0, "cas limite, plutôt normal"),
    (16.0, 50.0, 4.0, "surtension + chaleur"),
    (12.0, 100.0, 7.5, "Défectueus grave")
]

for tension, temperature, odeur, description in exemples:
    proba, verdict = predire(tension, temperature, odeur)
    print(f"V={tension}V, T={temperature}°C, odeur={odeur}/10 -> proba défaut = {proba:.3f} -> {verdict}  ({description})")

# Sauvegarde du modèle entraîné
torch.save(model.state_dict(), "modele_detecteur.pt")
print("\nModèle sauvegardé dans modele_detecteur.pt")