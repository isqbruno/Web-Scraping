#Coleta de Notícias (Web Scraper)

![Status](https://img.shields.io/badge/status-funcional-green)
![Python](https://img.shields.io/badge/Python-3.9+-blue)

## Visão Geral do Projeto

Este projeto é uma ferramenta de automação construída em Python. O seu principal objetivo é eliminar o trabalho manual e repetitivo de coletar informações de sites. Ele foi programado para funcionar como um robô que visita o site, identifica os dados principais e as organiza de forma automática numa planilha Excel, pronta para ser utilizada.

---

## Objetivo do projeto

O processo é dividido em duas missões claras, executadas em sequência.

## 🛠️ Tecnologias Utilizadas

-   **Python 3.9+**
-   **Requests:** Para fazer as requisições HTTP e buscar o conteúdo HTML da página.
-   **BeautifulSoup4 & lxml:** Para analisar (fazer o "parse") do HTML e encontrar os dados de interesse.
-   **Pandas & openpyxl:** Para manipular os dados e criar o arquivo final em formato Excel.


## ⚙️ Como Funciona: O Fluxo de Trabalho

O processo é orquestrado pelo arquivo `main.py` e dividido em duas missões claras:

1.  **Missão 1: A Coleta (Scraping)**
    -   O sistema visita o site.
    -   Ele lê o código-fonte HTML da página.
    -   Dentro desse código, ele procura por padrões que identificam os títulos do site e os seus links.
    -   Toda a informação bruta que ele encontra é guardada no arquivo `data/raw_txt/dados_site.txt`.

2.  **Missão 2: A Organização (Processamento)**
    -   O sistema lê o arquivo de texto bruto (`dados_site.txt`).
    -   Ele limpa e separa os títulos dos links.
    -   Utilizando a biblioteca Pandas, ele monta uma tabela organizada.
    -   Finalmente, esta tabela é exportada como uma planilha Excel (`data/processed_excel/dados_site.xlsx`).

## 📂 Estrutura de Pastas do Projeto

````
/Web-Scraping/
|
├── scrapers/               # Contém o o sistema que irá fazer a coleta
│   └── site_scraper.py
|
├── processor/              # Contém os módulos de processamento
│   └── converter.py
|
├── data/                   # Onde os resultados são guardados
│   ├── raw_txt/            # Contém os dados da coleta
│   │   └── dados_site.txt
|   |
│   └── processed_excel/    # Contém as planilhas finais processadas
│       └── dados_site.xlsx
|
├── venv/                   # Pasta do ambiente virtual
|
├── main.py                 # Orquestrador principal do projeto
├── requirements.txt        # Lista de bibliotecas necessárias
└── README.md               # Documentação do projeto

````

## 🚀  Guia de funcionamento 

### Passo 1: Instale as Bibliotecas

Primeiro instale as bibliotecas no seu ambiente python.
```bash
    pip install requests beautifulsoup4 pandas
```

### Passo 2: Crie e Ative o Ambiente virtual

Isto cria um espaço de trabalho isolado para o projeto, para que as ferramentas (bibliotecas) que instalarmos não se misturem com as de outros projetos.

```bash
# 1. Crie o ambiente 
python3 -m venv venv

# 2. Ative o ambiente (precisa de fazer isto sempre que for trabalhar no projeto)

#No macOS ou Linux:
source venv/bin/activate

# No Windows:
venv\Scripts\activate
```

Dica: Quando o ambiente está ativo, o nome (venv) aparecerá no início da linha do seu terminal. Isto confirma que está no espaço de trabalho correto.

### Passo 3: Instale as Ferramentas Necessárias

Agora, vamos instalar todas as ferramentas que o projeto precisa para funcionar. O pip faz isso automaticamente lendo a lista de compras (`requirements.txt`).

```bash
# Com o ambiente (venv) ativo, execute:
    pip install -r requirements.txt
```

### Passo 4: Executar o programa
Com tudo pronto, inicie o processo com o seguinte comando:
```bash
# Com o ambiente (venv) ainda ativo, execute:
python main.py
```
O script irá rodar e, ao final, a sua planilha Excel estará pronta na pasta data/processed_excel.

---
## Conclusão e Próximos Passos

Este projeto serve para mostras como web scraping e automação de dados funciona. Ele demonstra de forma prática como transformar informações dispersas na web em um formato estruturado e útil, economizando tempo e permitindo análises mais aprofundadas.

Com esta base, as possibilidades de expansão são muitas:

- **Expandir para Outros Sites**: Adaptar para coletar dados de outros sites como fontes de notícias, e-commerces ou qualquer site de seu interesse.

- **Automatizar a Execução**: Utilize ferramentas como cron (em macOS/Linux) ou o Agendador de Tarefas (no Windows) para que o script rode automaticamente todos os dias.

- **Visualização de Dados**: Crie um segundo script que leia a planilha Excel e gere gráficos e visualizações sobre as notícias coletadas.

- **Notificações**: Integre o projeto com um serviço de e-mail ou mensageiros (como Telegram) para receber as manchetes do dia assim que forem coletadas.

Sinta-se à vontade para experimentar e evoluir este projeto. A automação é uma habilidade poderosa e este é apenas o começo!

---
#⚠️ Aviso Importante
Projetos de web scraping dependem da estrutura do site-alvo. Se os desenvolvedores do G1 alterarem o layout da página, o robô pode deixar de encontrar as informações. Caso isso aconteça, será necessário inspecionar o novo código do site e atualizar os seletores no arquivo scrapers/g1_scraper.py.

---

