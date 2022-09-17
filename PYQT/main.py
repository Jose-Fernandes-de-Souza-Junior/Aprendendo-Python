import sys
from webbrowser import BackgroundBrowser
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QAction,QMenu,QMessageBox
from PyQt5.QtGui import QPixmap,QIcon


class Janela (QMainWindow): 

    def __init__(self):
        super().__init__()

        self.setGeometry(100,500,800,600)
        self.setWindowTitle("JANELA")


        botao1 = QPushButton ("Botão 1 ",self)
        botao2 = QPushButton (self)
        salvar = QPushButton ("SALVAR ",self)
        botao3 = QPushButton ("Menu",self)
        botao4 = QPushButton ("Enviar Mensagem",self)

        botao1.move (150,200)
        botao1.resize (150,70)
        botao1.clicked.connect(self.botaoClicado)


        
        
        botao2.move (150,500)
        botao2.resize (150,100)
        botao2.setIcon (QIcon(QPixmap("imagens\python img.png")))


       

        
        
        salvar.move (350,300)
        salvar.resize (150,70)
        salvar.clicked.connect(self.botaoSalvar)
        salvar.setStyleSheet('QPushButton {background-color:blue}')

        
        botao3.move (150,400)
        botao3.resize (150,70)
        
        menu = QMenu(self)
        menu.addAction("Opção 1")
        menu.addAction("Opção 2")
        menu.addAction("Opção 3")
        botao3.setMenu(menu)

        
        botao4.setText ("Hello World",self)
        botao4.move (150,300)
        botao4.resize (150,70)
        botao4.clicked.connect(self.enviarMensagem)









        
        self.show()
        


        

    
    def botaoClicado (self):

        print ("Cliquei")

    def botaoClicado2(self):
        print ("Cliquei 2")

    def botaoSalvar (self):

        print ("Salvo com Sucesso!")

    def enviarMensagem (self):
        msg = QMessageBox (self)
        msg.setIcon"Hello World")

  



    
        

        
aplicacao = QApplication (sys.argv)
j = Janela ()

sys.exit(aplicacao.exec_())