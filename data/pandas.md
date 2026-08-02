# Pandas

## 1. O que é Pandas?

Pandas é uma biblioteca de código aberto para a linguagem Python voltada principalmente para manipulação e análise de dados.

A biblioteca oferece estruturas de dados e ferramentas que facilitam tarefas como organização, limpeza, transformação e exploração de informações.

---

## 2. DataFrame

O DataFrame é uma das principais estruturas de dados do Pandas.

Ele organiza informações em formato de linhas e colunas, sendo semelhante a uma tabela.

Exemplo:

```python
import pandas as pd

dados = {
    "Nome": ["Ana", "João", "Maria"],
    "Idade": [20, 25, 22]
}

df = pd.DataFrame(dados)
```

Nesse exemplo, `df` representa um DataFrame com duas colunas: `Nome` e `Idade`.

---

## 3. Series

A Series é uma estrutura unidimensional do Pandas que pode armazenar uma sequência de valores.

Exemplo:

```python
import pandas as pd

idades = pd.Series([20, 25, 22])
```

Uma Series pode representar uma única coluna de dados.

---

## 4. Leitura de Dados

O Pandas permite carregar dados de diferentes formatos.

Um exemplo comum é a leitura de arquivos CSV:

```python
import pandas as pd

df = pd.read_csv("dados.csv")
```

Após carregar os dados, é possível realizar diferentes operações de análise.

---

## 5. Visualização Inicial

Alguns comandos podem ser utilizados para compreender a estrutura de um DataFrame.

Exemplo:

```python
df.head()
```

O método `head()` permite visualizar as primeiras linhas do conjunto de dados.

Outro exemplo:

```python
df.info()
```

O método `info()` apresenta informações sobre as colunas, tipos de dados e valores não nulos.

---

## 6. Seleção de Dados

O Pandas permite selecionar colunas específicas.

Exemplo:

```python
df["Idade"]
```

Também é possível selecionar múltiplas colunas:

```python
df[["Nome", "Idade"]]
```

---

## 7. Filtragem

A filtragem permite selecionar registros que atendem a determinada condição.

Exemplo:

```python
df[df["Idade"] > 20]
```

Nesse caso, serão selecionadas as linhas em que a idade é maior que 20.

---

## 8. Valores Ausentes

Durante uma análise, podem existir valores ausentes.

O Pandas possui ferramentas para identificar e tratar esses valores.

Exemplo:

```python
df.isnull()
```

Também é possível verificar a quantidade de valores ausentes:

```python
df.isnull().sum()
```

---

## 9. Agrupamento

O método `groupby()` permite agrupar dados de acordo com uma determinada coluna.

Exemplo:

```python
df.groupby("Categoria")["Valor"].mean()
```

Esse recurso pode ser utilizado para calcular métricas agrupadas.

---

## 10. Importância para o DataMentor

Pandas é uma das principais bibliotecas utilizadas no projeto DataMentor.

O assistente pode utilizar esse conteúdo para explicar conceitos como:

* DataFrame;
* Series;
* Leitura de arquivos;
* Filtragem;
* Valores ausentes;
* Agrupamentos;
* Manipulação de dados.
