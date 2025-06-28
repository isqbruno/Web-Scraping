# Arquivo que irá agir como um robô que irá coletar as principais noticias do site e salva no arquivo de texto
import requests
from bs4 import BeautifulSoup
import time
import os

def coletar_salvar_dados():
    print("\n\n->Iniciando o o sistema de scraping de site")

    URL = "https://g1.globo.com/"
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    CAMINHO_ARQUIVO_TXT = 'data/raw_txt/dados_site.txt'

    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'lxml')

        # como o sites de noticias mudam sua estrutura precisa verificar qual é  a nova estrutura
        noticias = soup.find_all('div', class_='bastian-feed-item')

        if not noticias:
            print("\nERRO! - Nenhuma noticia encontrado - A estrutura do site pode ter mudado\n")

        os.makedirs(os.path.dirname(CAMINHO_ARQUIVO_TXT), exist_ok=True)

        with open(CAMINHO_ARQUIVO_TXT, 'w') as f:
            print(f"\n-> Encontrado {len(noticias)} noticia. Salbado em {CAMINHO_ARQUIVO_TXT}...")

            for noticia in noticias:
                #coleta os titulos da tag <a> dentro de um h2
                titulo_tag = noticia.find('a', class_='feed-post-link')

                if titulo_tag and titulo_tag.get('href'):
                    titulo = titulo_tag.get_text(strip=True)
                    link = titulo_tag.get('href')

                    # Escreve os dados bem estruturados
                    f.write("---\n")
                    f.write(f"TITULO: {titulo}")
                    f.write(F"LINK: {link}")
        
        print("\n-> Coleta de dados finalizado com sucesso")

    except requests.exceptions.RequestException as erro:
        print(f"\nERRO! Falha de conexão. {erro}\n")
    except Exception as erro:
        print(f"\nERRO! Erro inesperado. {erro}\n")

    finally:
        time.sleep(2)
        #pausa para não derrubar ou congestionar o site

    




