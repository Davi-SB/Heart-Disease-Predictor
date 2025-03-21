## 1. Arquivo dados
### Limpeza, observações, estruturação e padronificação
### Como resultado, vamos ter um novo dataset (arquivo), arrumado e concentrado
- [X] Remover campos que não vai ser do nosso interesse de usar para treinar, como uma coisa que não influencia tanto ou não sabemos muito como afeta ou o que é;
- [X] Tirar colunas que tiverem menos de X% com dado;
- [X] Identificar colunas com registros fora do padrão e adequar elas para o nosso padrão (numérico). Ex: Sexo == 1 e Sexo == M;
- [ ] Plotar métricas interessantes que podem afetar mais diretamente. Os plots devem ser não só gráfico mas também a head dos nossos dataframes (primeiras linhas) para mostrar como a estrutura do nosso dataset está ficando. Ex: Colesterol e pressão alto podem indicar bem diretamente saúde ruim do coração, então vão ser dados que vamos frequentemente olhar na fase dos testes;
- [X] A resposta do nosso modelo deve ser bool, adequar a nota do coração isso

## 2. Arquivo Modelo
### sklearn.naive_bayes existe...
- [X] Escolher entre biblioteca e implementação manual
> Obs: essa sklearn tem umas funções mto boas até pra avaliar testes, pra executar deve ter tbm acho q a gnt estar aberto a usar ela ia ser bem potente. Ex: ` from sklearn.naive_bayes import GaussianNB;
from sklearn.metrics import accuracy_score`

## 3. Funcionamento do Classificador de Bayes
### Relação direta com o teorema de Bayes
- **Teorema de Bayes**
  O teorema de Bayes afirma que
  $$
  \displaystyle P(C|X) = \frac{P(X|C)P(C)}{P(X)}
  $$  
  onde \(P(C|X)\) é a probabilidade de uma classe \(C\) dado um conjunto de características \(X\).

- **Independência Condicional:**  
  O GaussianNB assume que os parâmetros de uma classe são independentes. Assim, a probabilidade \(P(X|C)\) pode ser fatorada como o produto das probabilidades de cada parâmetro.

- **Distribuição Gaussiana:**  
  Para cada parâmetro, é assumido que os valores seguem uma distribuição normal. Isso permite calcular \(P(x_j|C)\) usando a função densidade da normal com parâmetros (média e variância) estimados a partir dos dados.

- **Classificação:**  
  O classificador é treinado calculando \(P(C|X)\) para cada classe, usando os valores estimados para \(P(C)\) e \(P(X|C)\) (calculado com a distribuição gaussiana para cada parâmetro) e, ao ser aplicado, escolhe a classe com a maior probabilidade.

Dessa forma, o GaussianNB aplica o teorema de Bayes com a simplificação da independência condicional e o uso de distribuições gaussianas para cada parâmetro, o que torna o cálculo das probabilidades eficiente e direto para classificação.

## 4. Testes e avaliação
### Execução, análise e conclusão sobre diferentes testes
- [X] Fazer diferentes testes pra evitar o famigerado overfitting
- [X] Existem diferentes testes que existem, mas a gente pode mirar no aleatório pra evitar resultados enviesados
- [X] Tipo de teste 1 (Hold-Out): Pegar N linhas aleatórias (geralmente 70-80%) e usar e o resto das linhas para testar/avaliar
- [X] Tipo de teste 2 (Cross-validation): Teste cruzado, Em vez de dividir os dados uma única vez, a validação cruzada divide os dados em vários subconjuntos (chamados de folds) e realiza várias rodadas de treinamento e teste. A k-fold cross-validation é a mais comum: Divide os dados em k partes (folds). Em cada rodada, o modelo é treinado em k-1 folds e testado no fold restante. Esse processo se repete para cada fold. O desempenho final do modelo é a média dos resultados de cada rodada.
- [X] Tipo de teste 3, (Stratified K Fold): Similar ao teste cruzado k-fold, mas essa leva em consideração o desequilíbrio de classes, garantindo que cada fold tenha a mesma proporção de amostras de cada classe que os dados originais, reduzindo o risco de enviesar a avaliação do modelo.
- [X] Tipo de teste 4, (Bootstrap): São criadas várias amostras (com reposição) a partir dos dados originais. Em cada amostra, o modelo é treinado e uma estatística (como a acurácia) é calculada. Repetindo o processo muitas vezes, obtém-se uma distribuição da estatística que permite estimar média, variância e intervalos de confiança sem pressupor uma distribuição teórica.

> Outro que eu pesquisei e descobri que existe: Split com dados de validação
