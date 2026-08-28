import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score
)

# Modelos de classificação
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC


def avaliar_base(url, features, target, titulo):

    print("\n")
    print("=" * 70)
    print(titulo)
    print("=" * 70)

    # 1. Carregar os dados
    df = pd.read_csv(url)

    # 2. Features e variável alvo
    X = df[features]
    y = df[target]

    # 3. Divisão treino/teste
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=42,
        stratify=y
    )

    # 4. Padronização
    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # 5. Modelos
    modelos = {
        'Logistic Regression': LogisticRegression(
            max_iter=1000,
            random_state=42
        ),

        'Decision Tree': DecisionTreeClassifier(
            random_state=42
        ),

        'Random Forest': RandomForestClassifier(
            random_state=42
        ),

        'KNN': KNeighborsClassifier(),

        'Naive Bayes': GaussianNB(),

        'SVM': SVC(),

        'Gradient Boosting': GradientBoostingClassifier(
            random_state=42
        )
    }

    resultados = []

    # 6. Treinar e avaliar os modelos
    for nome, modelo in modelos.items():

        modelo.fit(X_train, y_train)

        # Previsões
        y_pred_train = modelo.predict(X_train)
        y_pred_test = modelo.predict(X_test)

        # Métricas de treino
        acc_train = accuracy_score(y_train, y_pred_train)

        f1_train = f1_score(
            y_train,
            y_pred_train,
            average='macro',
            zero_division=0
        )

        # Métricas de teste
        acc_test = accuracy_score(y_test, y_pred_test)

        f1_test = f1_score(
            y_test,
            y_pred_test,
            average='macro',
            zero_division=0
        )

        resultados.append(
            (
                nome,
                acc_train,
                f1_train,
                acc_test,
                f1_test
            )
        )

        print(f"\nModelo: {nome}")

        print(f"Acurácia - Treino: {acc_train:.4f}")
        print(f"Acurácia - Teste:  {acc_test:.4f}")

        print(f"F1-Score - Treino: {f1_train:.4f}")
        print(f"F1-Score - Teste:  {f1_test:.4f}")

        print("\nMatriz de Confusão:")
        print(confusion_matrix(y_test, y_pred_test))

        print("\nRelatório de Classificação:")
        print(
            classification_report(
                y_test,
                y_pred_test,
                zero_division=0
            )
        )

        print("-" * 70)

    # 7. Ranking pelo F1-Score do teste
    resultados.sort(
        key=lambda x: x[4],
        reverse=True
    )

    print("\nRANKING FINAL")
    print(
        f"{'Modelo':<25}"
        f"{'Acc Treino':<12}"
        f"{'Acc Teste':<12}"
        f"{'F1 Treino':<12}"
        f"{'F1 Teste':<12}"
    )

    print("-" * 73)

    for nome, acc_train, f1_train, acc_test, f1_test in resultados:

        print(
            f"{nome:<25}"
            f"{acc_train:<12.4f}"
            f"{acc_test:<12.4f}"
            f"{f1_train:<12.4f}"
            f"{f1_test:<12.4f}"
        )


# ==========================================================
# PROBLEMA 1
# ==========================================================

url1 = (
    'https://raw.githubusercontent.com/'
    'alexandrezamberlan/tias/refs/heads/main/'
    '3_predicao_previsao_codigos_exemplos/'
    'dados_predicao_modelos.csv'
)

features1 = [
    'Idade',
    'Renda_Anual_K',
    'Score_Credito',
    'Pontuacao_Engajamento'
]

target1 = 'Compro_Produto'

avaliar_base(
    url1,
    features1,
    target1,
    "PROBLEMA 1 - COMPRA DE PRODUTO"
)


# ==========================================================
# PROBLEMA 2
# ==========================================================

url2 = (
    'https://raw.githubusercontent.com/alexandrezamberlan/tias/refs/heads/main/3_predicao_previsao_codigos_exemplos/dados_saude_predicao.csv'
)

features2 = [
    'Idade',
    'Pressao_Arterial',
    'Colesterol_Total',
    'Frequencia_Cardiaca_Max'
]

target2 = 'Risco_Internacao'

avaliar_base(
    url2,
    features2,
    target2,
    "PROBLEMA 2 - RISCO DE INTERNAÇÃO"
)
