# ==========================================
# 3 VA 4-BO'LIMLAR: KLASSIFIKATSIYA VA TAQQOSLASH
# ==========================================

from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, \
    ConfusionMatrixDisplay

models = {
    "kNN (k=5)": KNeighborsClassifier(n_neighbors=5),
    "Naive Bayes": GaussianNB(),
    "SVM": SVC(kernel='rbf', random_state=42),
    "Qarorlar daraxti": DecisionTreeClassifier(random_state=42)
}

results = []

for name, model in models.items():
    model.fit(X_cls_train_scaled, y_cls_train)
    y_pred = model.predict(X_cls_test_scaled)

    results.append({
        "Algoritm": name,
        "Accuracy": round(accuracy_score(y_cls_test, y_pred), 4),
        "Precision": round(precision_score(y_cls_test, y_pred), 4),
        "Recall": round(recall_score(y_cls_test, y_pred), 4),
        "F1": round(f1_score(y_cls_test, y_pred), 4)
    })

df_results = pd.DataFrame(results)
print("=== KLASSIFIKATSIYA NATIJALARI JADVALI ===")
print(df_results.to_string(index=False))

# 1. Eng yaxshi model (SVM) uchun Qatoliklar matrisasi (Confusion Matrix)
best_model = models["SVM"]
y_best_pred = best_model.predict(X_cls_test_scaled)
cm = confusion_matrix(y_cls_test, y_best_pred)

plt.figure(figsize=(6, 5))
ConfusionMatrixDisplay(cm, display_labels=cancer.target_names).plot(cmap='Blues')
plt.title("Qatoliklar matrisasi (SVM)")
plt.show()

# 2. Qarorlar daraxtini vizuallashtirish
dt_model = models["Qarorlar daraxti"]
plt.figure(figsize=(16, 10))
plot_tree(dt_model, feature_names=cancer.feature_names, class_names=cancer.target_names, filled=True, max_depth=3)
plt.title("Qarorlar daraxti vizualizatsiyasi (Chuqurligi=3)")
plt.show()