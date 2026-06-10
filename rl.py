"""
Regressão Logística com Visualização
=====================================
Exemplo completo usando dataset sintético de classificação binária.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    confusion_matrix, classification_report,
    roc_curve, auc, ConfusionMatrixDisplay
)
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification

# ── Reprodutibilidade ──────────────────────────────────────────────────────────
np.random.seed(42)

# ── 1. Gerar dados sintéticos ──────────────────────────────────────────────────
X, y = make_classification(
    n_samples=500,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    n_clusters_per_class=1,
    class_sep=1.2,
    random_state=42,
)

# ── 2. Dividir em treino / teste ───────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# ── 3. Normalizar features ─────────────────────────────────────────────────────
scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc  = scaler.transform(X_test)

# ── 4. Treinar modelo ──────────────────────────────────────────────────────────
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train_sc, y_train)

# ── 5. Predições ───────────────────────────────────────────────────────────────
y_pred      = model.predict(X_test_sc)
y_prob      = model.predict_proba(X_test_sc)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc     = auc(fpr, tpr)

print("=== Relatório de Classificação ===")
print(classification_report(y_test, y_pred, target_names=["Classe 0", "Classe 1"]))
print(f"AUC-ROC: {roc_auc:.4f}")

# ── 6. Helper: fronteira de decisão ───────────────────────────────────────────
def plot_decision_boundary(ax, model, X, y, title):
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, 400),
        np.linspace(y_min, y_max, 400),
    )
    Z = model.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
    Z = Z.reshape(xx.shape)

    cf = ax.contourf(xx, yy, Z, levels=50, cmap="RdYlBu_r", alpha=0.75)
    ax.contour(xx, yy, Z, levels=[0.5], colors="white", linewidths=2, linestyles="--")
    scatter = ax.scatter(
        X[:, 0], X[:, 1], c=y,
        cmap="RdYlBu_r", edgecolors="k", linewidths=0.5, s=40, zorder=3
    )
    ax.set_title(title, fontsize=13, fontweight="bold", pad=10)
    ax.set_xlabel("Feature 1 (padronizada)", fontsize=10)
    ax.set_ylabel("Feature 2 (padronizada)", fontsize=10)
    return cf

# ── 7. Curva sigmoide ──────────────────────────────────────────────────────────
def plot_sigmoid(ax):
    z   = np.linspace(-8, 8, 400)
    sig = 1 / (1 + np.exp(-z))
    ax.plot(z, sig, color="#E63946", linewidth=2.5)
    ax.axhline(0.5, color="gray", linestyle="--", linewidth=1, alpha=0.7)
    ax.axvline(0.0, color="gray", linestyle="--", linewidth=1, alpha=0.7)
    ax.fill_between(z, sig, 0.5, where=(sig > 0.5), alpha=0.12, color="#E63946")
    ax.fill_between(z, sig, 0.5, where=(sig < 0.5), alpha=0.12, color="#457B9D")
    ax.set_title("Função Sigmoide  σ(z) = 1 / (1 + e⁻ᶻ)",
                 fontsize=13, fontweight="bold", pad=10)
    ax.set_xlabel("z  (combinação linear)", fontsize=10)
    ax.set_ylabel("Probabilidade", fontsize=10)
    ax.set_ylim(-0.05, 1.05)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])

# ── 8. Curva ROC ───────────────────────────────────────────────────────────────
def plot_roc(ax):
    ax.plot(fpr, tpr, color="#E63946", lw=2.5, label=f"ROC  (AUC = {roc_auc:.3f})")
    ax.plot([0, 1], [0, 1], "k--", lw=1, label="Aleatório (AUC = 0.50)")
    ax.fill_between(fpr, tpr, alpha=0.12, color="#E63946")
    ax.set_title("Curva ROC", fontsize=13, fontweight="bold", pad=10)
    ax.set_xlabel("Taxa de Falsos Positivos", fontsize=10)
    ax.set_ylabel("Taxa de Verdadeiros Positivos", fontsize=10)
    ax.legend(fontsize=9)
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(-0.02, 1.05)

# ── 9. Matriz de confusão ──────────────────────────────────────────────────────
def plot_confusion(ax):
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                                  display_labels=["Classe 0", "Classe 1"])
    disp.plot(ax=ax, colorbar=False, cmap="Blues")
    ax.set_title("Matriz de Confusão", fontsize=13, fontweight="bold", pad=10)

# ── 10. Montar figura ──────────────────────────────────────────────────────────
fig = plt.figure(figsize=(16, 10))
fig.patch.set_facecolor("#F8F9FA")
fig.suptitle("Regressão Logística — Visão Geral",
             fontsize=17, fontweight="bold", y=0.98)

gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.42, wspace=0.35)

ax1 = fig.add_subplot(gs[0, :2])   # fronteira (treino)
ax2 = fig.add_subplot(gs[0, 2])    # sigmoide
ax3 = fig.add_subplot(gs[1, 0])    # fronteira (teste)
ax4 = fig.add_subplot(gs[1, 1])    # ROC
ax5 = fig.add_subplot(gs[1, 2])    # confusão

for ax in (ax1, ax2, ax3, ax4, ax5):
    ax.set_facecolor("#FFFFFF")
    for spine in ax.spines.values():
        spine.set_edgecolor("#CCCCCC")

cf1 = plot_decision_boundary(ax1, model, X_train_sc, y_train,
                             "Fronteira de Decisão — Conjunto de Treino")
cf3 = plot_decision_boundary(ax3, model, X_test_sc,  y_test,
                             "Fronteira de Decisão — Conjunto de Teste")

# Barra de cores compartilhada para os dois mapas
cbar = fig.colorbar(cf1, ax=[ax1, ax3], fraction=0.025, pad=0.02)
cbar.set_label("P(Classe 1)", fontsize=9)

plot_sigmoid(ax2)
plot_roc(ax4)
plot_confusion(ax5)

plt.savefig("/regressao_logistica.png",
            dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.show()
print("\nGráfico salvo em: regressao_logistica.png")