file = "0.52_RealLifeData.txt"

with open(file, errors="ignore") as data:
    list_of_text = data.read()

list_of_text = list_of_text.lower()
text = ""

wanted_characters = [' ', "a", "b", "c", "d", "e", "f", "g", "h", 'i', 'j', 'k', 'l', 'm',
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in list_of_text:
    if i not in wanted_characters:
        text += " "
    else:
        text += i

with open(file, mode="w") as data:
    data.write(text)
