import sys
from webbrowser import BackgroundBrowser
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel
from PyQt5.QtGui import QPixmap,QIcon

class Janela (QMainWindow): 

    def __init__(self):
        QMainWindow().__init__(self)

        self.setGeometry(100,500,800,600)
        self.setWindowTitle("JANELA")
        
        botao1 = QPushButton ("Botão 1 ",self)
        botao2 = QPushButton ("Botão 2 ",self)

        botao1.move (150,200)
        botao1.resize (150,70)
        botao1.clicked.connect(self.botaoClicado)


        
        
        botao2.move (150,300)
        
        botao2.resize (150,70)
        botao2.clicked.connect(self.botaoClicado2)

        botao2 = QPixmap (QIcon("python img",self))

        self.show()

        
    def botaoClicado (self):

        print ("Cliquei")

    def botaoClicado2(self):
        print ("Cliquei 2")

aplicacao = QApplication (sys.argv)
j = Janela ()
j.show()

sys.exit(aplicacao.exec_())