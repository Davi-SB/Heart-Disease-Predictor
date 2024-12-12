# Heart-Disease-Predictor

Este projeto utiliza um classificador Ingênuo de Bayes, uma técnica de aprendizado de máquina, para prever o diagnóstico de doença cardíaca com base em um conjunto de variáveis relacionadas à saúde do coração. A ideia é aplicar um modelo simples e eficaz para estimar a probabilidade de uma pessoa apresentar uma condição cardíaca com base em seus dados clínicos.

## Variáveis no Dataset

Abaixo, listamos as variáveis do conjunto de dados, juntamente com nomes mais diretos e suas explicações detalhadas:

1. **Idade** (`age`): A idade do paciente em anos.
2. **Sexo** (`sex`): O sexo biológico do paciente (1 para masculino, 0 para feminino).
3. **TipoDorToracica** (`chestPain`): Tipo de dor no peito experimentada pelo paciente. Os valores categóricos representam:
   - 0: Angina típica
   - 1: Angina atípica
   - 2: Dor não anginosa
   - 3: Assintomático
4. **PressaoSanguineaRepouso** (`restingBloodPressure`): Pressão arterial em repouso (mm Hg).
5. **ColesterolSerico** (`serumCholestoral`): Nível de colesterol sérico em mg/dL.
6. **GlicoseJejumElevada** (`fastingBloodSugar>120`): Indicador binário de glicose em jejum acima de 120 mg/dL (1 para verdadeiro, 0 para falso).
7. **EletrocardiogramaRepouso** (`restingEletroc`): Resultados do eletrocardiograma em repouso:
   - 0: Normal
   - 1: Anormalidade na onda ST-T (inversão de onda T ou elevação/depresso na ST)
   - 2: Hipertrofia ventricular esquerda provável ou definitiva
8. **FrequenciaCardiacaMaxima** (`maximumHeartRate`): Frequência cardíaca máxima alcançada durante o teste.
9. **AnginaPorExercicio** (`exerciseInducedAngina`): Indicador binário de dor no peito induzida por exercício (1 para sim, 0 para não).
10. **DepressaoST** (`oldpeak`): Depressão do segmento ST em relação ao repouso, medida em mm.
11. **InclinaçãoST** (`op_slope`): Inclinação do segmento ST durante o exercício:
    - 0: Para cima
    - 1: Plano
    - 2: Para baixo
12. **NumeroVasosPrincipais** (`numberMajorVessels`): Número de vasos principais (0-3) coloridos pela fluoroscopia.
13. **FluxoSanguineoTalio** (`bloodFlow_thal`): Resultados do teste de estresse com tálio:
    - 3: Normal
    - 6: Defeito fixo
    - 7: Defeito reversível
14. **Diagnostico** (`diagnosis(FURate)`): Variável alvo que indica a presença de doença cardíaca (0 para ausência, 1 para presença).

## Objetivo do Projeto

O objetivo é treinar um classificador Ingênuo de Bayes que possa prever a variável alvo, **Diagnóstico**, com base nos dados fornecidos. A abordagem de Bayes foi escolhida devido à sua simplicidade, interpretabilidade e eficácia em cenários com variáveis categóricas e numéricas.

## Estrutura do Projeto

1. **Preparação dos Dados**:

   - Limpeza e normalização dos dados.
   - Conversão de variáveis categóricas para formatos compatíveis.

2. **Treinamento do Modelo**:

   - Divisão dos dados em conjuntos de treinamento e teste.
   - Treinamento do classificador Ingênuo de Bayes.

3. **Avaliação do Modelo**:

   - Cálculo de métricas como acurácia, precisão, recall e F1-score.

4. **Validação e Ajuste**:

   - Ajustes nos parâmetros do modelo para melhorar o desempenho.

## Como Executar

1. Clone este repositório.
2. Instale as dependências necessárias usando `pip install -r requirements.txt`.
3. Execute o script principal com `python main.py`.
4. Verifique os resultados no terminal ou em arquivos de saída.

## Contribuições

Sinta-se à vontade para contribuir com melhorias, correções ou novos recursos. Submeta um Pull Request com suas sugestões!

