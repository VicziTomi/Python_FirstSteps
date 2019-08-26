import re

sentence = "Vertebrate animals are: fish, amphibian, reptile, bird, mammal"
check = re.search("bird", sentence)
check2 = re.search("mammal$", sentence)
check3 = re.search("insect", sentence)
check4 = re.findall("al", sentence)
check5 = re.split("i", sentence)
check6 = re.sub("an|al|am|at|ar", "**", sentence)
print(check, check.start())
print(check2)
print(check3)
print(check4)
print(check5)
print(check6)
