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
- [ ] Escolher entre biblioteca e implementação manual
- [ ] Ajuste de parâmetros
> Obs: essa sklearn tem umas funções mto boas até pra avaliar testes, pra executar deve ter tbm acho q a gnt estar aberto a usar ela ia ser bem potente. Ex: ` from sklearn.naive_bayes import GaussianNB;
from sklearn.metrics import accuracy_score`

## 3. Testes e avaliação
### Exceução, análise e conclusão sobre diferentes testes
- [ ] Fazer diferentes testes pra evitar o famigerado overfitting
- [ ] Existem diferentes testes que existem, mas a gente pode mirar no aleatório pra evitar resultados enviesados
- [ ] Tipo de teste 1 (Hold-Out): Pegar N linhas aleatórias (geralmente 70-80%) e usar e o resto das linhas para testar/avaliar
- [ ] Tipo de teste 2 (Cross-validation): Teste cruzado, Em vez de dividir os dados uma única vez, a validação cruzada divide os dados em vários subconjuntos (chamados de folds) e realiza várias rodadas de treinamento e teste. A k-fold cross-validation é a mais comum: Divide os dados em k partes (folds). Em cada rodada, o modelo é treinado em k-1 folds e testado no fold restante. Esse processo se repete para cada fold. O desempenho final do modelo é a média dos resultados de cada rodada. Achei esse bom pq a avaliação já pe definida por ele mesmo.
> Outros que eu pesquisei e descobri que existe: Divisão aleatória (Hold-out), Validação cruzada (Cross-validation), Validação Cruzada Estratificada, Split com dados de validação, Bootstrap (Amostragem com reposição)
