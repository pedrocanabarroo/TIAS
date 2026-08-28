### Análise dos resultados

A partir dos resultados obtidos, verificou-se que o desempenho dos modelos varia significativamente entre os dois problemas analisados.

No primeiro problema, relacionado à previsão de compra de um produto, o Random Forest apresentou o melhor desempenho no conjunto de teste, alcançando acurácia de 69,33% e F1-Score Macro de 65,14%. Entretanto, o modelo apresentou 100% de acurácia e F1-Score no treinamento, caracterizando indícios de overfitting. O mesmo comportamento foi observado na Decision Tree e, de forma ainda mais evidente, no Gradient Boosting.

Modelos como Logistic Regression e Naive Bayes apresentaram resultados mais próximos entre os conjuntos de treinamento e teste, indicando melhor capacidade de generalização, porém com desempenho geral inferior. Dessa forma, os resultados do primeiro problema indicam que os algoritmos conseguem encontrar padrões nos dados, mas ainda apresentam uma capacidade de previsão relativamente limitada.

No segundo problema, relacionado ao risco de internação, os resultados foram superiores. O Naive Bayes apresentou o melhor desempenho, com 81,33% de acurácia e 81,25% de F1-Score no conjunto de teste. Além disso, não apresentou sinais relevantes de overfitting, pois seu desempenho no treinamento foi de aproximadamente 76,57%.

A Logistic Regression também apresentou boa capacidade de generalização, mantendo resultados praticamente iguais entre treinamento e teste. Em contrapartida, Decision Tree, Random Forest e Gradient Boosting atingiram resultados de 100% ou próximos disso no treinamento, mas tiveram desempenho inferior no conjunto de teste, indicando sobreajuste aos dados de treinamento.

A análise das matrizes de confusão também demonstra a importância de observar os tipos de erros cometidos pelos modelos. No problema de saúde, por exemplo, os falsos negativos merecem atenção especial, pois representam pacientes classificados como de baixo risco quando, na realidade, pertencem ao grupo de alto risco.

Portanto, considerando conjuntamente acurácia, F1-Score, matriz de confusão e diferença entre os resultados de treinamento e teste, o Naive Bayes apresentou o melhor equilíbrio no segundo problema. Já no primeiro problema, apesar de o Random Forest possuir o maior F1-Score no teste, seus indícios de overfitting tornam necessária uma análise mais cuidadosa antes de considerá-lo o melhor modelo.

De modo geral, os experimentos mostram que a escolha de um algoritmo não deve ser realizada apenas pelo maior valor de acurácia. É necessário avaliar também sua capacidade de generalização, o F1-Score e os erros apresentados na matriz de confusão.
