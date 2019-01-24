import json


#Looking for .json file

arq_json = open('data.json', 'r')
dados = json.load(arq_json)
x = dados['Pimenta']
b = dados['Banana']
   
print(x)
print(b)
    
    
    
