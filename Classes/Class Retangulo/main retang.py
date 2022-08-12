from retangulo import retangulo

ret1 = retangulo(10,15)

ret1.calc_Area()
ret1.calc_Perimetro()
ret1.retornarValor()

ladoA = float(input("Digite um novo tamanho para a altura: "))
ladoB = float(input("Digite um novo tamanho para a base: "))

ret1.mudarValor(ladoA,ladoB)
ret1.calc_Area()
ret1.calc_Perimetro()

ret1.retornarValor()