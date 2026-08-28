# Problema 1 — Compra de Produto

Aqui, o **Random Forest foi o melhor modelo no conjunto de teste**, com:

* Acurácia de teste: **69,33%**
* F1-Score de teste: **65,14%**

Porém, no treinamento ele teve **100% de acurácia e 100% de F1-Score**, o que mostra uma diferença grande entre treino e teste.

Isso é um forte indício de **overfitting**: o modelo aprendeu muito bem os dados de treino, mas não conseguiu generalizar tão bem para dados novos.

## Matriz de Confusão

```text
[[39  6]
 [17 13]]
```

Isso significa:

* **39 clientes que não compraram** foram classificados corretamente;
* **13 clientes que compraram** foram classificados corretamente;
* **6 falsos positivos:** foram classificados como compradores, mas não compraram;
* **17 falsos negativos:** compraram, mas o modelo disse que não comprariam.

O ponto mais preocupante são os **17 falsos negativos**, porque o modelo deixou de identificar muitos clientes compradores.

O **Decision Tree** apresenta um comportamento semelhante:

* Acurácia de treino: **100%**
* Acurácia de teste: **65,33%**

Isso também indica **overfitting**.

O caso mais evidente é o **Gradient Boosting**:

* Acurácia de treino: **99,43%**
* Acurácia de teste: **60%**
* F1-Score de treino: **99,40%**
* F1-Score de teste: **52,97%**

Aqui há uma queda muito acentuada, indicando forte sobreajuste aos dados de treinamento.

## Modelos mais estáveis no Problema 1

A **Logistic Regression** teve:

* Acurácia de treino: **70,86%**
* Acurácia de teste: **65,33%**

O **Naive Bayes** teve:

* Acurácia de treino: **72%**
* Acurácia de teste: **65,33%**

A diferença entre treino e teste é muito menor nesses modelos. Portanto, eles apresentam **menos evidência de overfitting**, embora tenham desempenho geral inferior ao Random Forest.

O ranking final deixa isso evidente: o Random Forest teve o maior F1-Score de teste, com **0,6514**, mas os resultados de todos os modelos ficaram relativamente próximos e abaixo de 70% de acurácia.

## Conclusão do Problema 1

> Os modelos conseguem identificar algum padrão nos dados, mas ainda possuem dificuldade para prever corretamente a compra do produto. O Random Forest apresentou o melhor desempenho no teste, porém demonstrou forte overfitting. Assim, nenhum dos modelos apresenta, neste experimento, um desempenho suficientemente forte para ser escolhido imediatamente para uma aplicação real sem ajustes adicionais.

---

# Problema 2 — Risco de Internação

Neste problema, os resultados foram consideravelmente melhores.

O **Naive Bayes foi o melhor modelo**, apresentando:

* Acurácia de treino: **76,57%**
* Acurácia de teste: **81,33%**
* F1-Score de treino: **76,56%**
* F1-Score de teste: **81,25%**

Esse comportamento é interessante porque o modelo teve desempenho até um pouco superior no teste.

Isso **não caracteriza overfitting**.

Esse resultado pode ocorrer porque os 75 registros selecionados para o conjunto de teste acabaram sendo ligeiramente mais fáceis de classificar do que os registros utilizados no treinamento.

O mais importante é que não existe uma queda grande entre o desempenho de treino e teste.

## Matriz de Confusão

```text
[[33  5]
 [ 9 28]]
```

Isso significa:

* **33 pacientes de baixo risco** foram corretamente identificados;
* **28 pacientes de alto risco** foram corretamente identificados;
* **5 falsos positivos**;
* **9 falsos negativos**.

Ou seja, dos **75 pacientes usados no teste**, o modelo acertou:

```text
33 + 28 = 61 acertos
```

Portanto:

```text
61 / 75 = 0,8133
```

Ou aproximadamente:

**81,33% de acurácia**.

## Conclusão do Problema 2

O Naive Bayes apresentou um bom equilíbrio entre desempenho de treinamento e teste, além de alcançar a maior acurácia e o maior F1-Score entre os modelos analisados.

Diferentemente dos modelos que atingiram valores próximos ou iguais a 100% no treinamento e tiveram quedas significativas no teste, o Naive Bayes apresentou boa capacidade de generalização.

Apesar disso, os **9 falsos negativos** merecem atenção, principalmente por se tratar de uma aplicação relacionada à saúde. Nesse caso, um falso negativo representa um paciente realmente pertencente ao grupo de alto risco sendo classificado como de baixo risco.






### Análise dos resultados

A partir dos resultados obtidos, verificou-se que o desempenho dos modelos varia significativamente entre os dois problemas analisados.

No primeiro problema, relacionado à previsão de compra de um produto, o Random Forest apresentou o melhor desempenho no conjunto de teste, alcançando acurácia de 69,33% e F1-Score Macro de 65,14%. Entretanto, o modelo apresentou 100% de acurácia e F1-Score no treinamento, caracterizando indícios de overfitting. O mesmo comportamento foi observado na Decision Tree e, de forma ainda mais evidente, no Gradient Boosting.

Modelos como Logistic Regression e Naive Bayes apresentaram resultados mais próximos entre os conjuntos de treinamento e teste, indicando melhor capacidade de generalização, porém com desempenho geral inferior. Dessa forma, os resultados do primeiro problema indicam que os algoritmos conseguem encontrar padrões nos dados, mas ainda apresentam uma capacidade de previsão relativamente limitada.

No segundo problema, relacionado ao risco de internação, os resultados foram superiores. O Naive Bayes apresentou o melhor desempenho, com 81,33% de acurácia e 81,25% de F1-Score no conjunto de teste. Além disso, não apresentou sinais relevantes de overfitting, pois seu desempenho no treinamento foi de aproximadamente 76,57%.

A Logistic Regression também apresentou boa capacidade de generalização, mantendo resultados praticamente iguais entre treinamento e teste. Em contrapartida, Decision Tree, Random Forest e Gradient Boosting atingiram resultados de 100% ou próximos disso no treinamento, mas tiveram desempenho inferior no conjunto de teste, indicando sobreajuste aos dados de treinamento.

A análise das matrizes de confusão também demonstra a importância de observar os tipos de erros cometidos pelos modelos. No problema de saúde, por exemplo, os falsos negativos merecem atenção especial, pois representam pacientes classificados como de baixo risco quando, na realidade, pertencem ao grupo de alto risco.

Portanto, considerando conjuntamente acurácia, F1-Score, matriz de confusão e diferença entre os resultados de treinamento e teste, o Naive Bayes apresentou o melhor equilíbrio no segundo problema. Já no primeiro problema, apesar de o Random Forest possuir o maior F1-Score no teste, seus indícios de overfitting tornam necessária uma análise mais cuidadosa antes de considerá-lo o melhor modelo.

De modo geral, os experimentos mostram que a escolha de um algoritmo não deve ser realizada apenas pelo maior valor de acurácia. É necessário avaliar também sua capacidade de generalização, o F1-Score e os erros apresentados na matriz de confusão.

Portanto, dentro deste experimento, o **Naive Bayes apresentou o melhor resultado geral para o Problema 2**.

