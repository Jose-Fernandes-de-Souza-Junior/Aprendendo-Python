from mailbox import NotEmptyError
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow, QLabel, QGridLayout, QWidget, QMenu, QMessageBox, QPushButton
from PyQt5.QtCore import  QSize, QTimer
from PyQt5.QtGui import  QIcon, QPixmap, QFont
from janela1 import *
from janela2 import *
from janela3 import *

class janelaTerciaria (QMainWindow):
    def __init__(self):
        super().__init__()
        self.jan3 = Ui_janelaTerceira()
        self.jan3.setupUi(self)
        self.j1 = janelaPrimaria()

        #colocar o Get (recuperar a informação armazenada)




        self.jan3.labelRecebeNome.setText(self.j1.get_nome())
        '''print(self.j1.nome)
        self.j1.rg_set(rg)'''
        


        
        
        
        
        

class janelaSecundaria (QMainWindow):
    def __init__(self):
        super().__init__()
        self.jan2 = Ui_janelaSegunda()
        self.jan2.setupUi(self)
        
        self.j1=janelaPrimaria()
        self.j3 = janelaTerciaria()
        
        self.jan2.botaoVoltar.clicked.connect(self.voltar)     
        self.jan2.botaoConcluir.clicked.connect(self.enviarJanela3)
        
    def voltar(self):
        self.j1.show()
        self.hide()
    
    def enviarJanela3(self):
          
        self.j3.show()
        self.hide()
           
        
     
class janelaPrimaria (QMainWindow):
    def __init__(self,nome,rg,email):
        super().__init__()
        self.jan1 = Ui_janelaPrimeira()   #Usar o Set para armazenara informação
        self.jan1.setupUi(self)
        self.nome = nome
        self.rg = rg
        self.email = email
        


        
        self.jan1.botaoEnviar.clicked.connect(self.enviarJanela2)
        
    
       
    def enviarJanela2(self):
        self.j2 = janelaSecundaria()
        self.j2.show()
        self.hide()

        self.nome = self.jan1.inputNome.text()
        self.rg = self.jan1.inputRg.text()
        self.email = self.jan1.inputEmail.text()


    def get_nome(self):
        return self.nome

    def get_rg(self):
        return self.rg   

    def get_email(self):
        return self.email

    def nome_set (self):
        return self.nome

    def rg_set (self):
        return self.rg

    def email_set (self):
        return self.email

        
    
      
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    arq = janelaPrimaria())
    arq.show()
    sys.exit(app.exec())