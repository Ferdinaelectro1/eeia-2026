"""
Test manuel du modèle avec TA PROPRE matrice 8x8
==================================================
On entraîne le même réseau que précédemment sur load_digits,
puis on teste sur des matrices 8x8 définies à la main (pas de données sklearn en test).
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

np.random.seed(42)

# ----------------------------------------------------------------------------
# 1. Entraînement du modèle (identique au script précédent)
# ----------------------------------------------------------------------------
digits = load_digits()
X = digits.data.astype(np.float64) / 16.0
y = digits.target

def one_hot(y, n_classes=10):
    out = np.zeros((y.size, n_classes))
    out[np.arange(y.size), y] = 1
    return out

Y = one_hot(y)
X_train, X_test, Y_train, Y_test, y_train, y_test = train_test_split(
    X, Y, y, test_size=0.2, random_state=42
)

n_features, n_hidden, n_classes = 64, 32, 10
W1 = np.random.randn(n_features, n_hidden) * np.sqrt(2.0 / n_features)
b1 = np.zeros((1, n_hidden))
W2 = np.random.randn(n_hidden, n_classes) * np.sqrt(2.0 / n_hidden)
b2 = np.zeros((1, n_classes))

def relu(z): return np.maximum(0, z)
def relu_derivative(z): return (z > 0).astype(float)
def softmax(z):
    exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
    return exp_z / np.sum(exp_z, axis=1, keepdims=True)
def cross_entropy_loss(Y_pred, Y_true):
    eps = 1e-9
    return -np.sum(Y_true * np.log(Y_pred + eps)) / Y_true.shape[0]

def forward(X, W1, b1, W2, b2):
    Z1 = X @ W1 + b1
    A1 = relu(Z1)
    Z2 = A1 @ W2 + b2
    A2 = softmax(Z2)
    return A2, (X, Z1, A1, Z2, A2)

def backward(cache, Y_true, W2):
    X, Z1, A1, Z2, A2 = cache
    n = X.shape[0]
    dZ2 = (A2 - Y_true) / n
    dW2 = A1.T @ dZ2
    db2 = np.sum(dZ2, axis=0, keepdims=True)
    dA1 = dZ2 @ W2.T
    dZ1 = dA1 * relu_derivative(Z1)
    dW1 = X.T @ dZ1
    db1 = np.sum(dZ1, axis=0, keepdims=True)
    return dW1, db1, dW2, db2

learning_rate, n_epochs = 0.5, 500
print("Entraînement en cours...")
for epoch in range(1, n_epochs + 1):
    A2, cache = forward(X_train, W1, b1, W2, b2)
    dW1, db1, dW2, db2 = backward(cache, Y_train, W2)
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

test_preds = np.argmax(forward(X_test, W1, b1, W2, b2)[0], axis=1)
print(f"Entraînement terminé. Précision test sklearn : {np.mean(test_preds == y_test):.2%}\n")

# ----------------------------------------------------------------------------
# 2. Fonction pour tester UNE matrice 8x8 définie manuellement
# ----------------------------------------------------------------------------
def predict_custom_matrix(matrix_8x8, label_attendu=None):
    """
    matrix_8x8 : liste de listes ou np.array de forme (8,8), valeurs 0-16
                 (0 = blanc/fond, 16 = noir max, comme dans load_digits)
    """
    matrix = np.array(matrix_8x8, dtype=np.float64)
    assert matrix.shape == (8, 8), f"La matrice doit être 8x8, reçu {matrix.shape}"

    # Même normalisation que pendant l'entraînement : /16.0
    x_flat = (matrix / 16.0).reshape(1, 64)

    probs, _ = forward(x_flat, W1, b1, W2, b2)
    prediction = np.argmax(probs)
    confiance = probs[0, prediction]

    # Affichage visuel
    fig, ax = plt.subplots(figsize=(3, 3))
    ax.imshow(matrix, cmap='gray_r', vmin=0, vmax=16)
    titre = f"Prédiction : {prediction} (confiance {confiance:.1%})"
    if label_attendu is not None:
        titre += f"\nAttendu : {label_attendu}"
    ax.set_title(titre, fontsize=10)
    ax.set_xticks(range(8))
    ax.set_yticks(range(8))
    ax.tick_params(labelsize=7)
    plt.tight_layout()

    print(f"Prédiction : {prediction}")
    print("Probabilités par classe (0 à 9) :")
    for i, p in enumerate(probs[0]):
        barre = "█" * int(p * 40)
        marque = " <-- " if i == prediction else ""
        print(f"  {i}: {p:.3f} {barre}{marque}")

    return fig, prediction, probs[0]

# ----------------------------------------------------------------------------
# 3. EXEMPLE : matrice dessinée à la main représentant un "1"
#    (dessinée manuellement, ligne verticale simple)
# ----------------------------------------------------------------------------
mon_1_dessine = [
    [0, 0, 2, 8, 8, 0, 0, 0],
    [0, 0, 4,14, 8, 0, 0, 0],
    [0, 0, 0,14, 8, 0, 0, 0],
    [0, 0, 0,14, 8, 0, 0, 0],
    [0, 0, 0,14, 8, 0, 0, 0],
    [0, 0, 0,14, 8, 0, 0, 0],
    [0, 0, 2,15, 9, 0, 0, 0],
    [0, 0, 3,16,10, 0, 0, 0],
]

# Un chiffre "0" dessiné à la main (un anneau)
chiffre_ambigu = [
    [0,  12,  8,  12, 0,  8,  2,  0],
    [12,  0, 15,  6,  6,  15, 10, 2],
    [16,  1, 4,  0,  0,  15,  4, 6],
    [18,  1, 3,  0,  6,  15,  0, 8],
    [18,  0, 0,  0,  0,  0,  2, 8],
    [6,  12,  4,  0,  0,  4,  14, 6],
    [2,  10, 1,  1,  1,  0,  10, 2],
    [0,  10,  8,  0,  1,  8,  2,  0],
]

mon_0_dessine = [
    [0, 6,14,10, 0, 0, 0, 0],
    [0,12, 6,12, 0, 0, 0, 0],
    [0,14, 0,12, 0, 0, 0, 0],
    [0, 8, 8,12, 12, 12, 0, 0],   
    [0, 0,10,12, 0, 0, 0, 0],   
    [0, 0, 0,12, 0, 0, 0, 0],
    [0, 0, 0,12, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0],
]


print("=" * 50)
print("TEST 1 : ma propre matrice représentant un '1'")
print("=" * 50)
fig1, pred1, probs1 = predict_custom_matrix(mon_1_dessine, label_attendu=1)
fig1.savefig('custom_test_1.png', dpi=150, bbox_inches='tight')

print("\n" + "=" * 50)
print("TEST 2 : ma propre matrice représentant un '0'")
print("=" * 50)
fig2, pred2, probs2 = predict_custom_matrix(mon_0_dessine, label_attendu=0)
fig2.savefig('custom_test_0.png', dpi=150, bbox_inches='tight')

print("\nImages sauvegardées : custom_test_1.png, custom_test_0.png")
