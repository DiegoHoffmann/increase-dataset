# increase-dataset
Objetivo: repositório com tecnicas para ampliação de data sets.

## Data Augmentation
Conjunto de técnicas comumente utilizadas, individualmente ou em conjunto, para aumentar as variações dos dados de treinamento em modelos de visão computacional e linguagem natural. Possui baixo custo para ser implementado reduzindo a necessidade da mineração de dados, possibilita a geração de métricas do treino a cada variação gerada e diminui a possibilidade de overfitting quando aplicado corretamente.


## Execução

Instale as dependências do projeto.
```
pip install -r requirements.txt
```

Acesse o diretório onde está o projeto e execute o comando abaixo.
```
python .\data_agmentation.py
```

Após a execução as imagens com as modificações estarão disponíveis em /imagens/geradas.