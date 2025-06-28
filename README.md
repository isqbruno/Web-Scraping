#Coleta de Notícias (Web Scraper)

## Visão Geral do Projeto

Este projeto é uma ferramenta de automação construída em Python. O seu principal objetivo é eliminar o trabalho manual e repetitivo de coletar informações de sites. Ele foi programado para funcionar como um robô que visita o portal de notícias G1, identifica as manchetes mais recentes e as organiza de forma automática numa planilha Excel, pronta para ser utilizada.

---

## Objetivo do projeto

O processo é dividido em duas missões claras, executadas em sequência:

1.  **Missão 1: A Coleta (Scraping)**
    -   O robô recebe a ordem para visitar a página inicial do G1.
    -   Ele "lê" o código-fonte HTML da página, que é a estrutura por trás do que vemos no navegador.
    -   Dentro desse código, ele procura por padrões específicos que identificam os títulos das notícias e os seus respetivos links.
    -   Toda a informação "bruta" que ele encontra é guardada num arquivo de texto (`dados_site.txt`) como um registo de segurança.

2.  **Missão 2: A Organização (Processamento)**
    -   Uma vez que a coleta termina, o robô pega o arquivo de texto bruto.
    -   Ele lê cada linha, limpa qualquer "lixo" (espaços extras, etc.) e separa os títulos dos links.
    -   Utilizando a poderosa biblioteca Pandas, ele monta uma tabela organizada com duas colunas: "Título da Matéria" e "Link para Matéria".
    -   Finalmente, esta tabela é exportada como uma planilha Excel (`dados_site.xlsx`), limpa e profissional.

---

## Guia Completo: Como Colocar o Robô Para Trabalhar

Siga estes 4 passos no seu terminal para configurar e executar o projeto.

### Passo 1: Vá Para o Local Certo

Antes de mais nada, o seu terminal precisa de estar "dentro" da pasta principal do projeto.


### Passo 2: Crie e Ative o Seu Ambiente de Trabalho

Isto cria um espaço de trabalho isolado para o projeto, para que as ferramentas (bibliotecas) que instalarmos não se misturem com as de outros projetos.

```bash
# 1. Crie o ambiente (só precisa de fazer isto uma vez por projeto)
python3 -m venv venv

# 2. Ative o ambiente (precisa de fazer isto sempre que for trabalhar no projeto)
source venv/bin/activate
```

Dica: Quando o ambiente está ativo, o nome (venv) aparecerá no início da linha do seu terminal. Isto confirma que está no espaço de trabalho correto.

### Passo 3: Instale as Ferramentas Necessárias

Agora, vamos instalar todas as ferramentas que o robô precisa para funcionar. O pip faz isso automaticamente lendo a lista de compras (`requirements.txt`).

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

O script irá mostrar o seu progresso no terminal. Quando terminar, a sua planilha Excel estará à sua espera dentro da pasta `data/`.