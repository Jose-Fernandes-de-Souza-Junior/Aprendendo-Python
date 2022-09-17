import sys
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu, QMessageBox,QLabel   
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QTimer, QSize

class Janela (QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(100,500,800,600)    
        self.setWindowTitle("Primeira Janela")
        label = QLabel(self)
        label.setText("Opções: ")
        label.setFont(QFont('Arial', 20))
        label.move(55,10)
        
        
        self.botao1 = QPushButton("Botao 1",self)
        self.botao2 = QPushButton(self)
        self.botao3 = QPushButton("Cancelar",self)
        self.botao4 = QPushButton("Menu", self)
        self.botao5 = QPushButton("Enviar Mensagem",self)
        self.botao6 = QPushButton("Contador",self)
        self.botaoLabel = QPushButton ("LABEL",self)


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
        
        #botaoLabel
        self.botaoLabel.move (450,200)
        self.botaoLabel.resize (300,350)
            
        #ações
        self.botao1.clicked.connect(self.usarLabel)   
        self.botao3.clicked.connect(self.clean)
        self.botao5.clicked.connect(self.enviaMensagem)
        
        
        self.show()

    def botaoClicado(self):
        print ("Cliquei")
        

    def usarLabel(self):
        self.botaoLabel.setText("Novo Texto")
        

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