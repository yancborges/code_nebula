import web_scrapping_resources

phr = input("Frase teste: ")

words = []
f = open("Fake_db.txt", 'r')
data = f.readlines()
for line in data:
    x = line
    if(line.endswith("\n")):
        x = line[:-1]
    words.append(x)
#print(words)

print("Separando frase...")
sphr = phr.split(" ")
print(sphr)


for item in sphr:
    if(web_scrapping_resources.isAVerbInflection(item) == True):
        
        

        
        




