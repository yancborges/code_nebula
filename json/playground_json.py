import json

user = {'Name':'Abc', 'Password':'safepassword', 'Age': 15, 'Gender': 'Male'}
data_string = json.dumps(user)
arq = open('teste.json', 'wb')
arq.write(data_string.encode())
arq.close()

deck = ['Terreno','Terreno','Equip','Lacaio','Terreno','Magia']
deck_string = json.dumps(deck)
arq = open('teste.json', 'ab')
arq.write(deck_string.encode())
arq.close()

arq = open('teste.json', 'rb')
x = []
for i in arq.readlines():
    x.append(i)

print(x)
#obj = json.loads(x[0].decode())






