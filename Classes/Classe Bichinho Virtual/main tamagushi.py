from tamagushi import tamagushi

bich = tamagushi("Tiburcio",3,7,55)

bich.retornarNome()
bich.retornarFome()
bich.retornarSaude()
bich.retornarIdade()


saude = int(input("Digite o valor para a saude: "))
fome = int(input("Digite o valor para fome: "))

bich.alterarSaude(saude)
bich.alterarFome(fome)

if bich.saude>=6 and bich.fome>=8 and bich.fome<=10:
    bich.retornarSaude()

    print('Humor: Feliz')


elif bich.saude<6 and bich.fome<8:
    bich.retornarSaude()
    print("Humor: Triste")






