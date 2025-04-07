#-*-coding:UTF-8-*-
print("Bem-vindo(a) ao centro de treinamento para o seu personagem de RPG! Aqui você poderá exercitar seu combatente para aumentar seus atributos!")
nome=str(input("Escreva o nome do seu personagem: "))
atr=str(input("Escreva o atributo que você quer aumentar. Digite 'V' para velocidade, 'F' para força e 'I' para inteligência: "))
pon=int(input("Agora insira quantos pontos de atributo você quer utilizar: "))

if atr=="F" or atr=="f":
    print(f"Você aumentou sua força em {pon} ponto(s)!")
elif atr=="V" or atr=="v":
    print(f"Você aumentou sua velocidade em {pon} ponto(s)!")