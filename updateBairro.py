import pandas as pd
import mysql.connector
from mysql.connector import Error

# Configuração do banco de dados MySQL
MYSQL_HOST = "localhost"
MYSQL_USER = "seu_usuario"
MYSQL_PASSWORD = "sua_senha"
MYSQL_DATABASE = "seu_banco_de_dados"
MYSQL_TABLE = "clientes"

# Caminho do arquivo fonte
SOURCE_FILE = "saida.xlsx"
ID_CLIENTE_COLUMN = "idCliente"
BAIRRO_COLUMN = "bairro"

def conectar_mysql():
    """Conecta ao banco de dados MySQL."""
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )
        if connection.is_connected():
            print("Conexão com MySQL estabelecida!")
            return connection
    except Error as e:
        print(f"Erro ao conectar no MySQL: {e}")
        return None

def atualizar_bairros(connection, df_source):
    """Atualiza os bairros no banco de dados com base no idCliente."""
    try:
        cursor = connection.cursor()
        total_linhas = len(df_source)
        print(f"Total de registros a atualizar: {total_linhas}")

        # Iterar sobre as linhas e atualizar os dados no banco
        for index, row in df_source.iterrows():
            id_cliente = row[ID_CLIENTE_COLUMN]
            bairro = row[BAIRRO_COLUMN]

            # Query SQL para atualizar o bairro no banco
            query = f"""
                UPDATE {MYSQL_TABLE}
                SET bairro = %s
                WHERE idCliente = %s
            """
            cursor.execute(query, (bairro, id_cliente))

            # Exibir progresso
            percentual = ((index + 1) / total_linhas) * 100
            print(f"Progresso: {percentual:.2f}% ({index + 1}/{total_linhas})", end="\r")

        connection.commit()
        print("\nAtualização concluída com sucesso!")
    except Error as e:
        print(f"Erro durante a atualização: {e}")
    finally:
        cursor.close()

def main():
    try:
        # Carregar os dados do arquivo Excel
        print("Carregando os dados do arquivo...")
        df_source = pd.read_excel(SOURCE_FILE)

        # Verificar se as colunas existem
        if ID_CLIENTE_COLUMN not in df_source.columns or BAIRRO_COLUMN not in df_source.columns:
            print("Erro: Colunas 'idCliente' ou 'bairro' não encontradas no arquivo.")
            return

        # Conectar ao banco de dados
        connection = conectar_mysql()
        if connection:
            # Atualizar os bairros no MySQL
            atualizar_bairros(connection, df_source)
            connection.close()
            print("Conexão encerrada.")
        else:
            print("Não foi possível conectar ao banco de dados.")

    except Exception as e:
        print(f"Erro geral: {e}")

if __name__ == "__main__":
    main()
