def avaliate(text):
    points = 3
    words = text.split(" ")
    if("sozinho" not in words):
        sz = "sozinha"
    else:
        sz = "sozinho"
    if("sentindo" not in words or "estou" not in words):
        points = 0
    else:
        if(words.index("sozinho") < words.index("sentindo")):
            points -= 1
        if(words[words.index("sentindo")-1] != "me"):
            points -= 1
    if(words[words.index("estou")-1] == "não" or words[words.index("estou")-1] == "n"):
        points -= 1
    return points
