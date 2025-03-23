
# Predição de Doenças Cardíacas com Classificador Ingênuo de Bayes

Este projeto tem como objetivo aplicar e analisar um classificador ingênuo de Bayes para a predição de doenças cardíacas, utilizando um conjunto de dados do UCI Machine Learning Repository. Através de um processo completo que inclui a limpeza, exploração e modelagem dos dados, o estudo busca demonstrar a aplicabilidade de métodos probabilísticos na área da saúde, contribuindo para a identificação de fatores de risco e para a melhoria dos processos de diagnóstico e prevenção de enfermidades cardiovasculares.

## Sumário
- [Motivação e Objetivos](#motivação-e-objetivos)
- [Descrição do Dataset](#descrição-do-dataset)
- [Pré-processamento e Limpeza dos Dados](#pré-processamento-e-limpeza-dos-dados)
- [Análise Exploratória dos Dados](#análise-exploratória-dos-dados)
- [Implementação do Classificador Ingênuo de Bayes](#implementação-do-classificador-ingênuo-de-bayes)
- [Integrantes](#Integrantes)
- [Referências](#referências)

## Motivação e Objetivos

Este estudo busca:
- Aplicar um modelo preditivo utilizando o classificador ingênuo de Bayes para identificar a presença de doenças cardíacas.
- Explorar as propriedades estatísticas do modelo, mesmo considerando a suposição de independência condicional entre os atributos.
- Avaliar o desempenho do modelo por meio de métricas como acurácia, precisão e sensibilidade, utilizando diferentes estratégias de validação (Hold-Out, Bootstrap, Cross Validation e Stratified K-Fold).
- Investigar a relevância dos diferentes parâmetros clínicos e suas correlações com o diagnóstico, contribuindo para a discussão sobre a aplicação de aprendizado de máquina na área da saúde.

## Descrição do Dataset

O dataset utilizado foi obtido a partir do [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/45/heart+disease). Embora a base original contenha diversos parâmetros, neste estudo foram selecionadas as seguintes variáveis:
- **age** (idade)
- **sex** (sexo)
- **chestPain** (tipo de dor no peito)
- **restingBloodPressure** (pressão arterial em repouso)
- **serumCholestoral** (colesterol sérico)
- **restingEletroc** (resultados do eletrocardiograma em repouso)
- **maximumHeartRate** (frequência cardíaca máxima)
- **exerciseInducedAngina** (angina induzida pelo exercício)
- **diagnosis** (diagnóstico - variável alvo)

Cada variável foi escolhida por sua relevância clínica e potencial impacto na predição de doenças cardíacas.

## Pré-processamento e Limpeza dos Dados

A etapa de pré-processamento é realizada no arquivo `dataCleaning.ipynb`, onde:
- São identificados e tratados dados faltantes.
- São removidos registros inconsistentes e outliers.
- As variáveis são padronizadas para garantir consistência e facilitar a análise exploratória e modelagem preditiva.

## Análise Exploratória dos Dados

No notebook `dataAnalysis.ipynb`, foram realizadas diversas análises para compreender a distribuição dos dados e identificar padrões relevantes, como:
- **Distribuição do Diagnóstico vs. Variáveis Contínuas:** Gráficos de dispersão para idade, pressão arterial, colesterol e frequência cardíaca máxima.
- **Distribuição do Diagnóstico vs. Variáveis Categóricas:** Gráficos de contagem para sexo, dor no peito, eletrocardiograma em repouso e angina induzida pelo exercício.
- **Heatmap de Correlação:** Visualização da correlação entre os parâmetros e o diagnóstico, destacando os indicadores mais relevantes.

## Implementação do Classificador Ingênuo de Bayes

O classificador ingênuo de Bayes, cuja fundamentação teórica e fórmulas estão detalhadas no relatório, foi implementado nos notebooks:
- `NaiveBayes_Bootstrap.ipynb`
- `NaiveBayes_CrossValidation.ipynb`
- `NaiveBayes_StratifiedKFold.ipynb`

Cada arquivo demonstra uma abordagem de avaliação diferente, permitindo a análise do desempenho do modelo sob diversas metodologias:
- **Hold-Out:** Divisão simples dos dados em treinamento e teste.
- **Bootstrap:** Reamostragem para construir intervalos de confiança.
- **Cross Validation:** Divisão dos dados em k-folds para avaliação robusta.
- **Stratified K-Fold:** Validação cruzada com preservação da proporção das classes.

## Integrantes
- Davi Sorrentino Brilhante (dsb6)
- Davi Lyra Dubeux (dld2)
- Eduardo Mabesoone Melo (emm4)

## Referências

- Dua, D. and Graff, C. (2019). *UCI Machine Learning Repository: Heart Disease Data Set*. Disponível em: [UCI Repository](https://archive.ics.uci.edu/dataset/45/heart+disease).
- Murphy, K. P. (2012). *Machine Learning: A Probabilistic Perspective*. MIT Press.
- Russell, S. and Norvig, P. (2010). *Artificial Intelligence: A Modern Approach* (3ª ed.). Prentice Hall.
- Hastie, T., Tibshirani, R. and Friedman, J. (2009). *The Elements of Statistical Learning: Data Mining, Inference, and Prediction* (2ª ed.). Springer.


*Projeto desenvolvido como parte da disciplina de Estatística e Probabilidade para Computação do curso de Engenharia da Computação no Centro de informática da Universidade Federal de Pernambuco.*