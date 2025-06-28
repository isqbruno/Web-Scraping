# Converter o arquivo .txt para um arquivo excel utilizando a biblioteca pandas
import pandas as pd
import os

def converter_txt_excel():
    print("\n-> Processo de conversão de datos TXT para Excel")

    CAMINHO_ARQUIVO_TXT = 'data/raw_txt/dados_site.txt'
    CAMINHO_ARQUIVO_EXCEL = 'data/processed_excel/dados_site.xlsx'

    try:
        with open(CAMINHO_ARQUIVO_TXT, 'r') as f:
            linhas = f.readlines()

        dados_organizados = []
        noticia_atual = {}

        for linha in linhas:
            linha_limpa = linha.strip()

            if linha_limpa == '---':
                if noticia_atual:
                    dados_organizados.append(noticia_atual)
                noticia_atual = {}
            elif linha_limpa.startswith('TITULO:'):
                noticia_atual['Titulo da Matéria'] = linha_limpa.replace('TITULO:', ' ', 2)
            elif linha_limpa.startswith('LINK:'):
                noticia_atual['Link da Matéria'] = linha_limpa.replace('LINK:', ' ', 2)

        if noticia_atual:
            dados_organizados.append(noticia_atual)

        if dados_organizados:
            df = pd.DataFrame(dados_organizados)

            #Garante que a pasta exista antes de salvar
            os.makedirs(os.path.dirname(CAMINHO_ARQUIVO_EXCEL), exist_ok=True)
            df.to_excel(CAMINHO_ARQUIVO_EXCEL, index=False)
            print(f"\n-> Processo finalizado. Arquivo salvo em: {CAMINHO_ARQUIVO_EXCEL}")
        else:
            print("\nERRO! - Nenhum dado convertido.")

    except FileNotFoundError:
        print(f"\nERRO: Arquivo não encontrado em {CAMINHO_ARQUIVO_TXT}.")
    except Exception as erro:
        print(f"\n->ERRO!{erro}")
        



