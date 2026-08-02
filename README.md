# 🤖 DataMentor — Assistente Virtual de Análise de Dados com IA

## 📌 Sobre o Projeto

O **DataMentor** é um protótipo de assistente virtual desenvolvido como projeto de estudo para demonstrar como a Inteligência Artificial e uma base de conhecimento estruturada podem apoiar o aprendizado na área de **Análise de Dados**.

O projeto foi desenvolvido com foco em estudantes e pessoas que estão iniciando seus estudos em programação e análise de dados.

A proposta é oferecer uma ferramenta simples, organizada e acessível para consultar conteúdos relacionados a:

* Python;
* Pandas;
* NumPy;
* Análise de Dados.

O projeto demonstra conceitos de construção de assistentes virtuais, organização de uma base de conhecimento, engenharia de prompts e desenvolvimento de uma aplicação funcional.

---

# 🎯 Objetivo

O principal objetivo do DataMentor é criar um assistente capaz de auxiliar estudantes na compreensão de conceitos fundamentais relacionados à programação e análise de dados.

A solução busca:

* Facilitar o acesso a conteúdos de estudo;
* Organizar informações em uma base de conhecimento;
* Identificar o assunto relacionado à pergunta do usuário;
* Direcionar a consulta para conteúdos relevantes;
* Apresentar informações de forma simples e organizada;
* Evitar respostas baseadas em informações que não estejam disponíveis na base de conhecimento;
* Demonstrar, na prática, como um assistente virtual pode apoiar o aprendizado.

---

# 👥 Público-Alvo

O DataMentor foi pensado principalmente para:

* Estudantes de Ciência da Computação;
* Pessoas iniciantes em Python;
* Estudantes de Análise de Dados;
* Pessoas que estão começando a estudar Pandas e NumPy;
* Usuários que desejam revisar conceitos básicos de análise de dados.

---

# 🧩 Problema

Durante o processo de aprendizagem em programação e análise de dados, estudantes frequentemente encontram dificuldades para compreender conceitos básicos e localizar informações organizadas para revisão.

Entre os principais desafios estão:

* Grande quantidade de conteúdos disponíveis na internet;
* Dificuldade para identificar materiais confiáveis;
* Falta de organização dos conteúdos;
* Dificuldade para relacionar conceitos de programação com análise de dados;
* Necessidade de respostas mais simples e contextualizadas.

O DataMentor busca apresentar uma solução inicial para esse problema por meio de um assistente virtual conectado a uma base de conhecimento organizada.

---

# 💡 Solução Proposta

O DataMentor utiliza uma aplicação desenvolvida em Python com Streamlit e uma base de conhecimento estruturada em arquivos Markdown.

O funcionamento básico ocorre da seguinte maneira:

```text
Usuário
   │
   ▼
Realiza uma pergunta
   │
   ▼
DataMentor recebe a pergunta
   │
   ▼
Analisa palavras-chave
   │
   ▼
Identifica o assunto relacionado
   │
   ▼
Consulta a base de conhecimento
   │
   ▼
Seleciona conteúdos relevantes
   │
   ▼
Apresenta as informações ao usuário
```

A aplicação utiliza os arquivos disponíveis na pasta `data/` como fonte de conhecimento.

---

# 📚 Base de Conhecimento

A base de conhecimento foi organizada em arquivos Markdown para facilitar a manutenção e a expansão do projeto.

Atualmente, ela contém:

### 🐍 Python

Arquivo:

```text
data/python.md
```

Conteúdos abordados:

* Conceitos básicos de Python;
* Variáveis;
* Tipos de dados;
* Estruturas condicionais;
* Estruturas de repetição;
* Funções;
* Aplicações de Python na análise de dados.

---

### 🐼 Pandas

Arquivo:

```text
data/pandas.md
```

Conteúdos abordados:

* Pandas;
* DataFrame;
* Series;
* Leitura de arquivos CSV;
* Seleção de dados;
* Filtragem;
* Valores ausentes;
* Agrupamento de dados.

---

### 🔢 NumPy

Arquivo:

```text
data/numpy.md
```

Conteúdos abordados:

* Conceitos básicos de NumPy;
* Arrays;
* Arrays multidimensionais;
* Operações numéricas;
* Operações estatísticas;
* Operações vetorizadas.

---

### 📊 Análise de Dados

Arquivo:

```text
data/analise-de-dados.md
```

Conteúdos abordados:

* Conceito de análise de dados;
* Coleta de dados;
* Limpeza de dados;
* Análise Exploratória de Dados;
* Visualização de dados;
* Identificação de insights;
* Processo de análise de dados;
* Uso de Python na análise de dados.

---

# 🧠 Engenharia de Prompts

A documentação dos prompts utilizados no projeto está disponível na pasta:

```text
docs/prompts.md
```

Os prompts foram estruturados considerando aspectos como:

* Objetivo do assistente;
* Público-alvo;
* Contexto;
* Base de conhecimento;
* Critérios de resposta;
* Limitações;
* Prevenção de informações inventadas;
* Tratamento de perguntas fora do escopo.

O objetivo é orientar o comportamento esperado do assistente e manter suas respostas relacionadas ao contexto de estudo proposto.

---

# 📖 Documentação

A documentação detalhada do projeto está disponível em:

```text
docs/documentacao.md
```

O documento apresenta informações sobre:

* Objetivo do DataMentor;
* Público-alvo;
* Problema identificado;
* Solução proposta;
* Funcionamento do assistente;
* Base de conhecimento;
* Limitações;
* Possíveis melhorias futuras.

---

# 💻 Aplicação Funcional

A aplicação foi desenvolvida utilizando:

* Python;
* Streamlit;
* Pathlib.

O arquivo principal da aplicação está localizado em:

```text
src/app.py
```

A aplicação possui uma interface simples onde o usuário pode:

1. Acessar o DataMentor;
2. Visualizar o status da base de conhecimento;
3. Digitar uma pergunta;
4. Enviar a pergunta ao assistente;
5. Identificar quais conteúdos estão relacionados à pergunta;
6. Visualizar o conteúdo utilizado como contexto.

---

# 🛠️ Tecnologias Utilizadas

| Tecnologia | Utilização                                  |
| ---------- | ------------------------------------------- |
| Python     | Desenvolvimento da aplicação                |
| Streamlit  | Criação da interface web                    |
| Pathlib    | Manipulação de arquivos e diretórios        |
| Markdown   | Organização da base de conhecimento         |
| Git        | Controle de versão                          |
| GitHub     | Armazenamento e compartilhamento do projeto |

---

# 📂 Estrutura do Projeto

```text
data-mentor-assistente-IA/
│
├── README.md
│
├── data/
│   ├── analise-de-dados.md
│   ├── python.md
│   ├── pandas.md
│   └── numpy.md
│
├── docs/
│   ├── documentacao.md
│   └── prompts.md
│
└── src/
    └── app.py
```

### `README.md`

Documento principal do projeto.

### `data/`

Contém a base de conhecimento utilizada pelo DataMentor.

### `docs/`

Contém a documentação e os prompts desenvolvidos para o projeto.

### `src/`

Contém o código da aplicação.

---

# 🚀 Como Executar o Projeto

## 1. Clone o repositório

Clone o projeto para seu computador utilizando Git.

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Entre na pasta:

```bash
cd data-mentor-assistente-IA
```

---

## 2. Instale o Streamlit

No terminal, execute:

```bash
python -m pip install streamlit
```

---

## 3. Execute a aplicação

Execute:

```bash
python -m streamlit run src/app.py
```

Após executar o comando, o Streamlit iniciará a aplicação e disponibilizará o DataMentor no navegador.

---

# 🧪 Exemplos de Perguntas

Algumas perguntas que podem ser utilizadas para testar o assistente:

```text
O que é Python?
```

```text
O que é um DataFrame?
```

```text
O que é Pandas?
```

```text
O que é um array no NumPy?
```

```text
O que é análise exploratória de dados?
```

```text
O que são valores ausentes?
```

---

# 📊 Avaliação do Protótipo

Durante os testes iniciais, foram utilizadas perguntas relacionadas aos principais conteúdos da base de conhecimento.

A avaliação considerou:

* Capacidade de identificar o tema da pergunta;
* Identificação do arquivo relacionado;
* Disponibilidade do conteúdo na base;
* Funcionamento da interface;
* Organização das informações apresentadas.

Os testes demonstraram que o protótipo consegue identificar assuntos relacionados a Python, Pandas, NumPy e Análise de Dados e apresentar os conteúdos correspondentes.

---

# ⚠️ Limitações Atuais

A versão atual do DataMentor é um protótipo inicial.

Atualmente, o sistema utiliza uma abordagem baseada em palavras-chave para identificar os conteúdos relacionados à pergunta.

A aplicação ainda não possui:

* Integração com um modelo de linguagem generativa;
* Busca semântica;
* Sistema de embeddings;
* Banco vetorial;
* Memória de conversação;
* Histórico de perguntas;
* Avaliação automatizada das respostas.

Essas limitações fazem parte do escopo atual do protótipo e representam oportunidades para futuras evoluções.

---

# 🔮 Melhorias Futuras

Como próximos passos, o projeto pode evoluir para incluir:

* Integração com uma API de Inteligência Artificial;
* Utilização de RAG (Retrieval-Augmented Generation);
* Busca semântica na base de conhecimento;
* Implementação de embeddings;
* Utilização de banco de dados vetorial;
* Histórico de conversas;
* Interface de chat mais completa;
* Sistema de avaliação automática;
* Expansão da base de conhecimento;
* Inclusão de novos conteúdos sobre SQL, Power BI e Machine Learning.

---

# 🎓 Aprendizados

O desenvolvimento do DataMentor permitiu explorar conceitos relacionados a:

* Desenvolvimento de aplicações em Python;
* Criação de interfaces com Streamlit;
* Organização de projetos no GitHub;
* Estruturação de uma base de conhecimento;
* Engenharia de prompts;
* Construção de assistentes virtuais;
* Organização de documentação técnica;
* Importância de limitar respostas ao contexto disponível;
* Integração entre programação e Inteligência Artificial.

---

# 👨‍💻 Autor

Projeto desenvolvido por **Rafael** como parte de um desafio de aprendizado e desenvolvimento de soluções utilizando Inteligência Artificial.

---

# 🚀 Conclusão

O **DataMentor** representa um protótipo de assistente virtual voltado para o aprendizado de Análise de Dados.

O projeto demonstra como uma base de conhecimento organizada pode ser utilizada em conjunto com uma aplicação Python para criar uma experiência de consulta simples e estruturada.

Embora a solução ainda esteja em uma etapa inicial, sua arquitetura permite futuras evoluções para aplicações mais avançadas utilizando Inteligência Artificial, busca semântica e técnicas de RAG.

**Projeto desenvolvido para fins educacionais.**
