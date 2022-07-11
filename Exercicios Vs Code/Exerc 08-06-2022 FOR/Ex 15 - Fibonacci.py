#A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n−ésimo termo.
seq1 = 0
seq2=1
cont=3

limite= int(input(print("Quantos termos da serie de Fibonacci você quer mostrar?: ")))

print("Os numeros da serie são : {} - {}".format(seq1,seq2),end='')
for seq1 in range (0,limite):    
    while cont<=limite:
        seq3= seq1+seq2
        print(" - {}".format(seq3),end='')
        seq1 = seq2
        seq2 = seq3
        cont+=1
        

    

