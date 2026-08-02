import streamlit as st
from pathlib import Path

# Configuração da página

st.set_page_config(
page_title="DataMentor",
page_icon="🤖",
layout="centered"
)

# Título

st.title("🤖 DataMentor")
st.subheader("Assistente de Análise de Dados")

st.write(
"Olá! Sou o DataMentor. "
"Posso ajudar você a aprender sobre Python, Pandas, NumPy "
"e conceitos de Análise de Dados."
)

# Caminho da base de conhecimento

DATA_PATH = Path(**file**).parent.parent / "data"

# Função para carregar a base de conhecimento

def carregar_base_conhecimento():
conhecimento = ""

```
if not DATA_PATH.exists():
    return conhecimento

for arquivo in DATA_PATH.glob("*.md"):
    try:
        conteudo = arquivo.read_text(encoding="utf-8")

        conhecimento += (
            f"\n\n--- Fonte: {arquivo.name} ---\n\n"
            f"{conteudo}"
        )

    except Exception as erro:
        st.warning(
            f"Não foi possível carregar o arquivo {arquivo.name}: {erro}"
        )

return conhecimento
```

# Carrega a base

base_conhecimento = carregar_base_conhecimento()

# Mostra o status da base

with st.expander("📚 Ver base de conhecimento"):
if base_conhecimento:
st.success("Base de conhecimento carregada com sucesso!")
st.write(
"O DataMentor está utilizando os arquivos disponíveis "
"na pasta data/."
)
else:
st.warning(
"Nenhum arquivo de conhecimento foi encontrado."
)

# Campo para pergunta

pergunta = st.text_input(
"💬 Digite sua pergunta:",
placeholder="Exemplo: O que é um DataFrame?"
)

# Processamento da pergunta

if st.button("Perguntar ao DataMentor"):

```
if not pergunta.strip():

    st.warning(
        "Digite uma pergunta antes de continuar."
    )

elif not base_conhecimento:

    st.error(
        "Não foi possível responder porque a base de conhecimento "
        "não está disponível."
    )

else:

    pergunta_minuscula = pergunta.lower()

    # Palavras-chave relacionadas a cada arquivo
    palavras_chave = {
        "python.md": [
            "python",
            "variável",
            "variaveis",
            "função",
            "funcoes",
            "funções",
            "lista",
            "dicionário",
            "dicionario",
            "if",
            "for",
            "while"
        ],

        "pandas.md": [
            "pandas",
            "dataframe",
            "data frame",
            "series",
            "csv",
            "filtrar",
            "filtragem",
            "valor ausente",
            "valores ausentes",
            "groupby"
        ],

        "numpy.md": [
            "numpy",
            "array",
            "ndarray",
            "vetorização",
            "vetorizacao",
            "média",
            "media",
            "desvio padrão",
            "desvio padrao"
        ],

        "analise-de-dados.md": [
            "análise de dados",
            "analise de dados",
            "eda",
            "análise exploratória",
            "analise exploratoria",
            "dados",
            "insight",
            "insights",
            "visualização",
            "visualizacao",
            "limpeza de dados",
            "limpeza"
        ]
    }

    # Identifica possíveis arquivos relacionados
    arquivos_relevantes = []

    for arquivo, palavras in palavras_chave.items():

        if any(
            palavra in pergunta_minuscula
            for palavra in palavras
        ):
            arquivos_relevantes.append(arquivo)

    # Se nenhum assunto específico for identificado,
    # utiliza toda a base de conhecimento
    if not arquivos_relevantes:

        contexto = base_conhecimento

    else:

        contexto = ""

        for arquivo in arquivos_relevantes:

            caminho = DATA_PATH / arquivo

            if caminho.exists():

                conteudo = caminho.read_text(
                    encoding="utf-8"
                )

                contexto += (
                    f"\n\n--- Fonte: {arquivo} ---\n\n"
                    f"{conteudo}"
                )

    # Exibe a pergunta
    st.markdown("### 👤 Sua pergunta")

    st.write(pergunta)

    # Exibe o contexto encontrado
    st.markdown("### 📚 Informações encontradas na base")

    if arquivos_relevantes:

        st.write(
            "A pergunta foi relacionada aos seguintes conteúdos:"
        )

        for arquivo in arquivos_relevantes:

            st.write(f"- `{arquivo}`")

    else:

        st.write(
            "Nenhum conteúdo específico foi identificado. "
            "A busca considerou toda a base de conhecimento."
        )

    # Resposta baseada na base
    st.markdown("### 🤖 DataMentor")

    st.info(
        "A base de conhecimento possui informações relacionadas "
        "à sua pergunta. Consulte os conteúdos indicados acima "
        "para encontrar a explicação correspondente."
    )

    # Mostra um trecho da base
    with st.expander("🔎 Ver conteúdo utilizado"):

        st.markdown(contexto)

    st.caption(
        "O DataMentor utiliza uma base de conhecimento local "
        "composta por arquivos Markdown."
    )
```
