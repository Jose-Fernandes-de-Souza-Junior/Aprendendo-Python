import sys
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu, QMessageBox,QLabel,QRadioButton  
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QTimer, QSize
from tkinter import * 
from tkinter.ttk import *

class Janela (QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(100,500,800,600)    
        self.setWindowTitle("Primeira Janela")
        label = QLabel(self)
        label.setText("Opções: ")
        label.setFont(QFont('Arial', 20))
        label.move(55,10)

        label1 = QLabel(self)
        label1.setText("COR DO TEXTO")
        label1.setFont(QFont('Arial', 20))
        label1.move(55,10)
        
        
        self.botao1 = QPushButton("Botao 1",self)
        self.botao2 = QPushButton(self)
        self.botao3 = QPushButton("Cancelar",self)
        self.botao4 = QPushButton("Menu", self)
        self.botao5 = QPushButton("Enviar Mensagem",self)
        self.botao6 = QPushButton("Contador",self)
        self.botaoLabel = QPushButton ("LABEL",self)
        '''self.botaoVermelho =QPushButton ("Red",self)
        self.botaoAzul = QPushButton ("Blue",self)
        self.botaoVerde = QPushButton ("Green",self)
        self.botaoAmarelo = QPushButton ("Yellow",self)'''
        self.labelVermelho =QLabel ("Red",self)
        self.labelAzul = QLabel ("Blue",self)
        self.labelVerde = QLabel ("Green",self)
        self.labelAmarelo = QLabel ("Yellow",self)
        self.botaoCentral = QPushButton ("",self)
        self.vermelhoRadio = QRadioButton (self)
        self.azulRadio = QRadioButton (self)
        self.verdeRadio = QRadioButton (self)
        self.amareloRadio = QRadioButton (self)
        self.label1 = QLabel ("COR DO TEXTO",self)
        

        #botao1
        self.botao1.move(50,50)

    
        #botao2
        self.botao2.move(50,100)
        self.botao2.setIcon(QIcon(QPixmap("Documents\project\python.png")))

        #botao3
        self.botao3.move(50,150)

        #botao4
        self.botao4.move(50,200)
        menu = QMenu (self)
        menu.addAction("Opção 1")
        menu.addAction("Opção 2")
        menu.addAction("Opção 3")
        self.botao4.setMenu(menu)

        #botao5
        self.botao5.move(50,250)

        #botao6
        self.botao6.move(50,300)
        self.botao6.resize(300,300)
        self.cont = 3
        self.botao6.clicked.connect(self.startContador)
        self.time = QTimer(self)
        self.time.setInterval(1000)
        self.time.timeout.connect(self.atualiza)
        
        #botao Label
        self.botaoLabel.move (450,200)
        self.botaoLabel.resize (150,150)
        
        #botao Label1
        self.label1.move (1300,100)
        self.label1.resize (150,150)


        '''#botao Vermelho
    
        #self.botaoVermelho.move (800,500)
        #self.botaoVermelho.resize (100,50)
        #self.botaoVermelho.setStyleSheet ('QPushButton {background-color: red}')
        

        #botao Azul
        self.botaoAzul.move (1000,500)
        self.botaoAzul.resize (100,50)
        self.botaoAzul.setStyleSheet ('QPushButton {background-color: blue}')

        #botao Verde
        self.botaoVerde.move (1200,500)
        self.botaoVerde.resize (100,50)
        self.botaoVerde.setStyleSheet ('QPushButton {background-color: green}')

        #botao Amarelo
        self.botaoAmarelo.move (1400,500)
        self.botaoAmarelo.resize (100,50)
        self.botaoAmarelo.setStyleSheet ('QPushButton {background-color: yellow}')'''

        #label Vermelho
        self.vermelhoRadio.move(780,500)
        self.labelVermelho.move (800,500)

        #label Azul
        self.azulRadio.move(780,520)
        self.labelAzul.move (800,520)

        #label Verde
        self.verdeRadio.move(780,540)
        self.labelVerde.move (800,540)

        #label Amarelo
        self.amareloRadio.move(780,560)
        self.labelAmarelo.move (800,560)

        
        #botão Central

        self.botaoCentral.move (900,90)
        self.botaoCentral.resize (350,200)
        self.botaoCentral.setStyleSheet ('QPushButton {background-color: white}')


            
        #ações
        self.botao1.clicked.connect(self.usarLabel)   
        self.botao3.clicked.connect(self.clean)
        self.botao5.clicked.connect(self.enviaMensagem)

        self.vermelhoRadio.clicked.connect (self.BtVermelho)
        self.azulRadio.clicked.connect (self.BtAzul)
        self.verdeRadio.clicked.connect (self.BtVerde)
        self.amareloRadio.clicked.connect (self.BtAmarelo)

        '''self.botaoVermelho.clicked.connect (self.BtVermelho)
        self.botaoAzul.clicked.connect (self.BtAzul)
        self.botaoVerde.clicked.connect (self.BtVerde)
        self.botaoAmarelo.clicked.connect (self.BtAmarelo)'''

        
        
        self.show()

    def botaoClicado(self):
        print ("Cliquei")
        

    def usarLabel(self):
        self.botaoLabel.setText("Novo Texto")

    def BtVermelho (self):
        self.botaoCentral.setStyleSheet ('QPushButton {background-color: red}')
        self.label1.setStyleSheet ('QLabel {color: red}')

    def BtAzul (self):
        self.botaoCentral.setStyleSheet ('QPushButton {background-color: blue}')
        self.label1.setStyleSheet ('QLabel {color: blue}')
        

    def BtVerde (self):
        self.botaoCentral.setStyleSheet ('QPushButton {background-color: green}')
        self.label1.setStyleSheet ('QLabel {color: green}')
        

    def BtAmarelo (self):
        self.botaoCentral.setStyleSheet ('QPushButton {background-color: yellow}')
        self.label1.setStyleSheet ('QLabel {color: yellow}')
        
        

    def clean(self):
        self.closeButton.clicked.connect(self.close)
    
    def enviaMensagem(self):
        QMessageBox.about(j,"Minha mensagem", 'Apertei o botao 5')

    #método startContador 
    def startContador(self):
        if self.botao6.isEnabled():
            self.time.start()
            self.botao6.setEnabled(False)

    #método atualiza
    def atualiza(self):
        if self.cont > 0 :
            self.botao6.setText(str(self.cont)+' segundos')
            self.cont -=1
        else:
            self.time.stop()
            self.botao6.setEnabled(True)
            self.botao6.setText("Botão 6")
            self.cont = 3
        
if __name__ == "__main__":
    aplicacao = QtWidgets.QApplication(sys.argv)
    j=Janela()
    j.show()
    sys.exit(aplicacao.exec_())
