import pandas as pd
import requests

# Defina os arquivos e URLs aqui
INPUT_EXCEL_FILE = "dados.xlsx"  # Caminho para a planilha de entrada
OUTPUT_EXCEL_FILE = "saida.xlsx"   # Caminho para a planilha de saída
CEP_COLUMN_NAME = "Cep"            # Nome da coluna que contém os CEPs
NEW_COLUMN_NAME = "bairro"         # Nome da nova coluna a ser criada
CORREIOS_API_URL = "https://viacep.com.br/ws/{}/json/"  # API para consulta do CEP

# Função para consultar a API dos Correios e retornar o bairro
def consultar_bairro_por_cep(cep):
    try:
        response = requests.get(CORREIOS_API_URL.format(cep))
        if response.status_code == 200:
            data = response.json()
            return data.get("bairro", "Bairro não encontrado")
        else:
            return "Erro na consulta"
    except Exception as e:
        print(f"Erro ao consultar CEP {cep}: {e}")
        return "Erro na consulta"

# Função principal
def processar_planilha():
    try:
        # Carregar a planilha
        print("Carregando a planilha...")
        df = pd.read_excel(INPUT_EXCEL_FILE)

        # Verificar se a coluna de CEP existe
        if CEP_COLUMN_NAME not in df.columns:
            print(f"Erro: Coluna '{CEP_COLUMN_NAME}' não encontrada na planilha.")
            return

        # Inicializar nova coluna
        df[NEW_COLUMN_NAME] = ""

        # Total de linhas para cálculo de progresso
        total_linhas = len(df)
        print(f"Total de linhas a processar: {total_linhas}")

        # Percorrer as linhas e consultar o CEP
        print("Consultando os CEPs...")
        for index, row in df.iterrows():
            cep = str(row[CEP_COLUMN_NAME]).strip()  # Garantir que o CEP é string
            if cep:
                bairro = consultar_bairro_por_cep(cep)
                df.at[index, NEW_COLUMN_NAME] = bairro
            else:
                df.at[index, NEW_COLUMN_NAME] = "CEP inválido"

            # Mostrar progresso
            percentual = ((index + 1) / total_linhas) * 100
            print(f"Progresso: {percentual:.2f}% ({index + 1}/{total_linhas})", end="\r")

        # Salvar a planilha com a nova coluna
        print("\nSalvando a nova planilha...")
        df.to_excel(OUTPUT_EXCEL_FILE, index=False)
        print(f"Processamento concluído. Arquivo salvo em '{OUTPUT_EXCEL_FILE}'.")

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    processar_planilha()
