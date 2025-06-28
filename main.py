# Importa as funções dos nossos outros arquivos
from scrapers.site_scraper import coletar_salvar_dados
from processor.converter import converter_txt_excel
import os

def main():
    print("\n========================================")
    print("INICIANDO PROJETO DE WEB SCRAPING")
    print("========================================")

    # --- ETAPA 1: Raspagem de Dados ---
    coletar_salvar_dados()

    print("\n----------------------------------------")

    # --- ETAPA 2: Processamento de Dados ---
    converter_txt_excel()

    print("\n========================================")
    print("PROJETO FINALIZADO COM SUCESSO!")
    print("========================================\n")

if __name__ == "__main__":
    main()