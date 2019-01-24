import urllib.request

def isAVerbInflection(word):
    
    pagina = urllib.request.urlopen(
        "https://www.priberam.pt/dlpo/" + word )
    
    resp = pagina.read().decode("utf8")
    
    start = resp.find('<div style="padding:10px;border:2px solid #d0d2d7;-webkit-border-radius: 2px;-moz-border-radius: 2px;border-radius: 2px;">')
    end = resp.find('<div style="background-color:#dadadd;display:none;">', start)
    
    mean = resp[start:end]
    
    if("1ª" in mean):
        return True
    return False
