import pandas as pd
from twilio.rest import Client

# Para cada arquivo:

# Verificar se algum valor na coluna vendas daquele arquivo é maior que 55.000

# se for maior do que 55.000 -> Envia um SMS com o Nome, mes e as vendas do vendedor

# Your Account SID from twilio.com/console
account_sid = "AC279e86c2ef89e1062299d8aca9c53183" # SID que irá receber na conta da twilio - não funciona com este token
# Your Auth Token from twilio.com/console
auth_token  = "e3b4a42396f9b38949bdd98545d60f90" # Token que irá receber no site da Twilio- não funciona com este token
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
       vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
       vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]


message = client.messages.create(
    to="+122345678", # colocar seu número do celular com o código do páis/ddd Regional/ número
    from_="+1212345678", # número que você obteve depois do cadastro no site da twilio
    body=f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')

print(message.sid)


