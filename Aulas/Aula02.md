# Técnicas de Inteligência Artificial

## Redes Neurais
- Inspiradas no funcionamento do cérebro humano.
- Utilizadas principalmente para **reconhecimento de padrões** em grandes volumes de dados.
- Aplicações:
  - Reconhecimento de imagens.
  - Diagnóstico por imagens médicas.
  - Reconhecimento de voz.
  - Detecção de fraudes.

## Base de Conhecimento
- Conjunto estruturado de informações utilizado pelo sistema para tomada de decisão.
- Pode ser composta por:
  - Regras definidas por especialistas.
  - Casos anteriores.
  - Bases de dados para treinamento de modelos.
- Muito utilizada em **Sistemas Especialistas**.

## Raciocínio Automatizado
- Capacidade de um sistema inferir conclusões a partir de regras e fatos conhecidos.
- Utiliza técnicas de lógica e inferência.
- Aplicações:
  - Sistemas especialistas.
  - Diagnóstico automático.
  - Tomada de decisão.

## Aprendizado de Máquina (Machine Learning)
- Área da IA que permite que computadores aprendam padrões a partir de dados.
- Principais tipos:
  - Aprendizado supervisionado.
  - Aprendizado não supervisionado.
  - Aprendizado por reforço.
- Aplicações:
  - Classificação.
  - Regressão.
  - Agrupamento (clustering).
  - Sistemas de recomendação.

## Processamento de Linguagem Natural (PLN)
- Permite que computadores compreendam e gerem linguagem humana.
- Aplicações:
  - Chatbots.
  - Tradução automática.
  - Análise de sentimentos.
  - Resumo automático de textos.
  - Assistentes virtuais.

## Sistemas Multiagentes
- Conjunto de agentes inteligentes que cooperam ou competem para resolver problemas.
- Cada agente possui autonomia e capacidade de comunicação.
- Aplicações:
  - Robótica.
  - Simulações.
  - Controle de tráfego.
  - Sistemas distribuídos.

---

# Aplicações da IA na Área da Saúde

## Medicina, Odontologia e Psicologia

### Diagnóstico
- Identificação automática de doenças ou condições clínicas.
- Utiliza:
  - Reconhecimento de padrões.
  - Redes neurais.
  - Aprendizado de máquina.
- Exemplos:
  - Diagnóstico por imagens.
  - Detecção de câncer.
  - Identificação de transtornos psicológicos.

### Recomendação
- Auxilia profissionais na tomada de decisão.
- Exemplos:
  - Sugestão de tratamentos.
  - Protocolos clínicos.
  - Recomendações terapêuticas.

---

## Enfermagem

### Monitoramento
- Acompanhamento contínuo do paciente.
- Utiliza sensores para coleta de sinais vitais.
- Exemplos:
  - Frequência cardíaca.
  - Pressão arterial.
  - Saturação de oxigênio.

### Sensoriamento e Atuação
- Integra sensores e dispositivos inteligentes.
- Pode realizar ações automáticas.
- Exemplos:
  - Alarmes automáticos.
  - Bombas de infusão inteligentes.
  - Monitoramento remoto.

---

## Farmácia, Biomedicina e Química

### Predição
- Estima resultados ainda desconhecidos.
- Exemplos:
  - Descoberta de novos medicamentos.
  - Predição da eficácia de compostos.
  - Toxicidade de substâncias.

### Previsão
- Estima acontecimentos futuros utilizando séries temporais.
- Exemplos:
  - Demanda de medicamentos.
  - Evolução de epidemias.
  - Consumo hospitalar.

### Recomendação
- Baseada em modelos de predição e previsão.
- Exemplos:
  - Sugestão de dosagens.
  - Seleção de medicamentos.
  - Apoio à decisão farmacêutica.

---

# Operações Realizadas pelos Sistemas de IA

## Diagnóstico

Objetivo:
- Identificar um problema ou condição existente.

Processo:
1. Coleta de dados.
2. Reconhecimento de padrões.
3. Aplicação de algoritmos de aprendizado de máquina.
4. Classificação do resultado.

Exemplos:
- Diagnóstico médico.
- Detecção de fraudes.
- Classificação de imagens.

---

## Monitoramento ou Sensoriamento

Objetivo:
- Acompanhar continuamente um ambiente ou paciente.

Características:
- Uso de sensores.
- Coleta contínua de dados.
- Geração de alertas.

Exemplos:
- Monitor cardíaco.
- IoT na saúde.
- Monitoramento industrial.

---

## Atuação (Automação)

Objetivo:
- Executar ações automaticamente após análise dos dados.

Exemplos:
- Acionar alarmes.
- Controlar equipamentos médicos.
- Ajustar parâmetros automaticamente.

---

## Predição e Previsão

### Predição
- Reconhece padrões em dados.
- Não depende necessariamente do tempo.
- Pode utilizar algoritmos de mineração de dados e aprendizado de máquina.

Exemplos:
- Classificar pacientes em grupos de risco.
- Detectar fraudes.
- Identificar doenças.

### Previsão
- Baseada em séries temporais.
- Estima acontecimentos futuros.

Exemplos:
- Prever número de internações.
- Prever vendas.
- Prever demanda hospitalar.

---

## Recomendação

Objetivo:
- Sugerir a melhor decisão ao usuário.

Baseia-se em:
- Predição.
- Previsão.
- Preferências.
- Histórico.
- Similaridade entre usuários ou itens.

Exemplos:
- Recomendação de medicamentos.
- Sistemas de apoio ao diagnóstico.
- Sugestão de tratamentos.

---

# Conceitos Importantes

## Sistema Especialista × Sistema de Recomendação

### Sistema Especialista
- Simula o conhecimento de especialistas humanos.
- Baseado em regras ("Se... então...").
- Possui uma base de conhecimento e um mecanismo de inferência.

Exemplo:
- Sistema que diagnostica doenças a partir de sintomas.

### Sistema de Recomendação
- Sugere itens ou decisões com base em dados e padrões.
- Utiliza aprendizado de máquina, filtragem colaborativa ou baseada em conteúdo.

Exemplos:
- Netflix.
- Spotify.
- Amazon.
- Recomendação de tratamentos médicos.

> **Importante:** um sistema especialista **não é o mesmo** que um sistema de recomendação, embora ambos possam apoiar a tomada de decisão.

---

# Estatística × Mineração de Dados

| Estatística | Mineração de Dados |
|-------------|--------------------|
| Trabalha normalmente com **amostras**. | Trabalha com **grandes volumes de dados** (ou toda a base disponível). |
| Busca compreender o comportamento da população a partir de uma amostra. | Busca encontrar padrões, relações e conhecimento oculto nos dados. |
| Forte fundamentação matemática e probabilística. | Combina Estatística, Inteligência Artificial, Machine Learning e Bancos de Dados. |
| Geralmente responde hipóteses formuladas previamente. | Pode descobrir padrões sem hipóteses prévias. |

### Resumo

- **Estatística:** utiliza uma **amostra** para fazer inferências sobre toda a população.
- **Mineração de Dados:** analisa grandes volumes de dados para descobrir padrões, tendências e gerar conhecimento útil sobre indivíduos, grupos ou processos.

---

# Fluxo Geral de Aplicação da IA

```text
Coleta de Dados
        ↓
Pré-processamento
        ↓
Mineração de Dados
        ↓
Aprendizado de Máquina
        ↓
Reconhecimento de Padrões
        ↓
Predição ou Previsão
        ↓
Recomendação ou Diagnóstico
        ↓
Tomada de Decisão
```
