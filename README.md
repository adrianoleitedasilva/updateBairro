# Automatização de Processos com Python: Atualização e Armazenamento de Dados

Este projeto engloba uma série de scripts Python criados para processar, manipular e atualizar informações de clientes com base em arquivos Excel e integração com banco de dados MySQL, além de consultas em APIs externas.

## Script: Consulta de CEP na API do ViaCep e Atualização do Bairro

### Objetivo:

Percorrer uma planilha Excel contendo uma lista de CEPs e, com base em cada CEP, consultar o bairro usando a API do ViaCep. Os bairros são armazenados em uma nova coluna no mesmo arquivo Excel.

**Funcionalidades**:

- Leitura da planilha Excel com a biblioteca pandas.
- Consulta dos CEPs na API ViaCep para obter o bairro.
- Criação de uma nova coluna "bairro" no arquivo Excel com os resultados.
- Monitoramento do percentual de progresso durante o processamento.

### Tecnologias Utilizadas:

- Python
- Bibliotecas: pandas, requests, openpyxl

**Aplicação**:
Atualização automática de informações de endereços para sistemas ou planilhas, eliminando a necessidade de consultas manuais.

## Script: Preenchimento de Bairros no Banco de Dados MySQL

### Objetivo:

Preencher a informação de bairro no banco de dados MySQL com base nos dados existentes em um arquivo Excel.

**Funcionalidades**:

- Leitura de um arquivo Excel contendo colunas idCliente e bairro.
- Conexão com um banco de dados MySQL.
- Atualização dos registros de bairro na tabela do banco, com base no campo idCliente.
- Apresentação do percentual de progresso durante o processamento.
