# Challenge 51 - Text-Speak Converter
dictionary = {
    "lol": "laugh out loud",
    "ts": "this crap",
    "pmo": "pees me off",
    "sybau": "shut your big axe up",
    "ngl": "not gonna lie",
    "icl": "i can't lie",
    "lmao": "laughing my ahh off",
    "imo": "in my opinion",
    "kys": "keep yourself safe",
    "lmfao": "laughing my fricking ahh off",
    "fr": "for real",
    "wdym": "what do you mean",
    "gng": "gang",
    "brb": "be right back",
    "idk": "I don't know",
    "smh": "shaking my head",
    "tbh": "to be honest",
    "fomo": "fear of missing out",
    "btw": "by the way",
    "omw": "on my way",
    "nvm": "never mind",
    "hru": "how are you",
    "gn": "good night",
    "rn": "right now",
    "omg": "oh my god",
    "rofl": "rolling on the floor laughing",
    "wth": "what the hell",
    "wtf": "what the frick",
    "pls": "please"
}

word = input("Input a message: ")
parts = word.split()

modified_parts = []

for part in parts:
    if part.lower() in dictionary:
        modified_parts.append(dictionary[part.lower()])
    else:
        modified_parts.append(part)

result = " ".join(modified_parts)
print(result)
