# Tecnologias Inteligentes Aplicadas à Saúde

- Apresentação do plano de aula
  
  - Temas ou conteúdos trabalhados

     Nova forma de avaliação
      - 20% da nota é a participação efetiva
      - 20% da nota será as anotações em sala de aula
      - 60% em desafios e trabalhos


# Predição

- **Sentido geral:** é o termo mais amplo. Refere-se ao ato de **estimar um valor, classe ou comportamento futuro, presente ou até passado desconhecido**, com base em dados e modelos.
- **Âmbito:** pode envolver:
  - **Classificação** (prever rótulos/categorias).
  - **Regressão** (prever valores numéricos).
- **Exemplos:**
  - Identificar se um cliente **vai** cancelar a assinatura (classificação).
  - Descobrir a idade de uma pessoa a partir de uma foto (a idade já ocorreu, mas não era conhecida — logo, é predição).
- **Importante:** a predição **não precisa ser, necessariamente, sobre o futuro**. Pode ser sobre o presente ou passado, desde que o dado real não seja conhecido no momento.

---

# Previsão

- **Sentido mais específico:** normalmente associada a **séries temporais** e eventos futuros.
- **Âmbito:** quase sempre lida com estimativas de **valores futuros** baseadas em padrões históricos.
- **Exemplos:**
  - Estimar a temperatura de amanhã com base nos dados climáticos dos últimos 10 anos.
  - Projetar o faturamento do próximo trimestre.
- **Importante:** a previsão implica **tempo** — está sempre ligada ao que ainda vai acontecer.

---

# Resumo

| Termo | Escopo | Pode ser sobre passado/presente desconhecido? | Sempre envolve futuro? | Exemplo |
|--------|--------|-----------------------------------------------|-------------------------|---------|
| **Predição** | Mais amplo | ✅ Sim | ❌ Não | Rotular a classe de um cliente atual ("alto risco") |
| **Previsão** | Mais específico (séries temporais) | ❌ Não | ✅ Sim | Prever o faturamento do mês que vem |

---

# Na Mineração de Dados

- Se o modelo **não depende diretamente do tempo** (ex.: classificação de imagens, detecção de fraude em transações), está se falando de **predição**.
- Se o modelo **usa o histórico temporal** para estimar algo que ainda vai acontecer, está se referindo a **previsão**.
