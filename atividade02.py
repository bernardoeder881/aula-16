from sqlalchemy import create_engine
import pandas as pd

# Conectando ao BD

host = 'localhost'
user = 'root'
password = ''
database = 'bd_aula06'

engine = create_engine(
     f'mysql+pymysql://{user}:{password}@{host}/{database}'
    )
# Criar as planilhas como Data frames (df)
try:
    df_clientes = pd.read_sql('tb_clientes', engine)
    df_itens =pd.read_sql('tb_itens' , engine)
    df_pedidos =pd.read_sql('tb_pedidos' , engine)
    df_produtos =pd.read_sql('tb_produtos' , engine)
  

except Exception as e:
    print( f'Falha na conexão {e}')

# Unindo as planilhas em uma só.
try:
    df_merge1 = pd.merge(df_clientes,df_pedidos, on='codigo_cliente')
    df_merge2 = pd.merge(df_merge1,df_itens, on='codigo_pedido')
    df_final = pd.merge(df_merge2,df_produtos, on='codigo_produto')
    # criando filtro para cidade de São Paulo
    filtro = (
        (df_final['cidade'] == 'Sao Paulo')
    )
    #Criando planilha só com a cidade de São Paulo usando o filtro criado.
    df_sp = df_final[filtro]

    #Imprimindo a planilha de São paulo com as colunas desejadas.
    print( 
        df_sp [['nome','sobrenome',
              'cidade','codigo_pedido',
              'data_pedido','produto','valor'
            ]])
except Exception as e:
    print( f'Erro no tratamemto de dados {e}')



 
