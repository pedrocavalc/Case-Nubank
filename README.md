# nubankcase

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>


## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         nubankcase and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── src   <- Source code for use in this project.

```

--------

## 🎬 Movie Recommendation System

Bem-vindo ao repositório do Movie Recommendation System! Este projeto tem como objetivo recomendar filmes com base nos favoritos informados pelo usuário, utilizando técnicas de aprendizado de máquina e um sistema de recomendação baseado em similaridade de preferências.

 ## Funcionalidades
Recomendações Personalizadas: Receba sugestões de filmes com base nos seus filmes favoritos (via IMDb ID).

Visualização com Pôsteres: Veja as recomendações com imagens dos filmes obtidas via OMDb.

Plataformas de Streaming: Descubra em quais plataformas os filmes recomendados estão disponíveis.

Integração Backend + Frontend: Backend com FastAPI e frontend com Streamlit para uma experiência interativa.
## 🧰 Tech Stack
Python: Linguagem principal do projeto.

FastAPI: API moderna e rápida para servir recomendações.

Streamlit: Interface amigável para interação com o usuário.

LightGBM: Algoritmo utilizado para treinar o modelo de recomendação.

Pandas: Manipulação e análise dos dados.

OMDb API: Para buscar pôsteres dos filmes recomendados.

## **Executando localmente**
Clone o repositório:

```bash
git clone https://github.com/seu-usuario/movie-recommender.git
cd movie-recommender
```
Instale as dependências:

```bash
pip install -r requirements.txt
```
Inicie o backend (FastAPI):

```bash
uvicorn app.main:app --reload
```
Inicie o frontend (Streamlit):
```bash
streamlit run front/app.py
```

## 🧠 Como funciona
Input do Usuário: O usuário informa os imdbId dos seus filmes favoritos.

Treinamento Dinâmico: Um modelo LightGBM é treinado com base nos filmes favoritos como positivos.

Geração de Scores: O modelo estima a probabilidade do usuário gostar de outros filmes.

Top N Recomendações: Os filmes com maior probabilidade (e que o usuário ainda não assistiu) são recomendados.

Visualização com Pôster e Plataforma: A recomendação é exibida com o pôster e links das plataformas onde o filme está disponível.

## 🛠️ MLOps Pipeline com MLflow
Além disso, este projeto implementa uma esteira de MLOps para treinamento e avaliação de modelos de classificação, com suporte a múltiplos algoritmos (XGBoost, Random Forest, LightGBM), usando:

MLflow para rastreamento de experimentos,
GridSearchCV para busca de hiperparâmetros,
Estrutura modular e reutilizável com componentes customizados de DataLoader, Pipeline, Model Manager e Model Configuration.
