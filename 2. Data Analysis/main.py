import pandas as pd 
from datetime import datetime

# Lê o arquivo
vendas = pd.read_csv('vendas.csv', header=0)

# Cria nova coluna com o total por linha
vendas['total'] = vendas['quantidade'] * vendas['preco_unitario']

# Calcula o faturamento por produto
faturamento_por_produto = vendas.groupby('produto')['total'].sum().reset_index()

# Produto de maior faturamento
produto_maior_faturamento = faturamento_por_produto.loc[faturamento_por_produto['total'].idxmax()]

# Produto de menor faturamento
produto_menor_faturamento = faturamento_por_produto.loc[faturamento_por_produto['total'].idxmin()]


# Visualização dos resultados
print('-------------------------------------------')
print(f'Faturamento por produto:\n')
print(f'{faturamento_por_produto}\n\n')
print('-------------------------------------------')
print(f'Produto mais faturado:\n')
print(f'{produto_maior_faturamento}\n\n')
print('-------------------------------------------')
print(f'Produto menos faturado:\n\n{produto_menor_faturamento}\n')