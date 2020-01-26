import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

#Recuperando os dados
csv = pd.read_csv('dados.csv', sep=";")
csv = csv.drop(columns=['Número comentários','Compartilhamento'])

#Normatizando os valores
le = LabelEncoder()
csv['Tipo'] = le.fit_transform(csv['Tipo'])

#criando o modelo
dados = csv.values
atributos = dados[:,0:5] 
likes = dados[:,5]

#Modelo Like
modelo = LinearRegression()
modelo.fit(atributos, likes)

#Coletando as informações
tipo = int(input('Informe o número do tipo da postagem Foto[0]|Link[1]|Status[2]|Video[3]: '))
mes = int(input('Mês: '))
dia = int(input('Dia da semana: D[1]|S[2]|T[3]|Q[4]|Q[5]|S[6]|S[7]: '))
hora = int(input('Hora: '))
pago = int(input('Pago: SIM[1]|NÃO[0]: '))

retorno = modelo.predict([[tipo, mes, dia, hora, pago]])
print('Média de Likes: ', int(retorno[0]))