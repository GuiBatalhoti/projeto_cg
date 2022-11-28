from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QLabel, QGroupBox, QRadioButton, QComboBox
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        # inicianlizando a interface
        super(UI, self).__init__()
        uic.loadUi('casinha/janela.ui', self)
        self.show()

        # Pegando os elementos da interface
        self.label_img = self.findChild(QLabel, "labelImg")
        self.btn_executa = self.findChild(QPushButton, "btnExecuta")

        #Grupos de Elementos
        #Grupo da Escala
        self.group_escala = self.findChild(QGroupBox, "groupEscala")
        self.btn_local = self.findChild(QRadioButton, "btnEscalaLocal")
        self.btn_global = self.findChild(QRadioButton, "btnEscalaGlobal")
        self.input_escala_x = self.findChild(QLineEdit, "inputEscalaZ")
        self.input_escala_y = self.findChild(QLineEdit, "inputEscalaY")
        self.input_escala_z = self.findChild(QLineEdit, "inputEscalaX")
        self.input_escala_global = self.findChild(QLineEdit, "inputEscalaGlobal")

        #Grupo da Translação
        self.group_translacao = self.findChild(QGroupBox, "groupTranslacao")
        self.input_translacao_x = self.findChild(QLineEdit, "inputTranslacaoZ")
        self.input_translacao_y = self.findChild(QLineEdit, "inputTranslacaoY")
        self.input_translacao_z = self.findChild(QLineEdit, "inputTranslacaoX")

        #Grupo da Rotação
        self.group_rotacao = self.findChild(QGroupBox, "groupRotacao")
        self.btn_origem = self.findChild(QRadioButton, "btnRotacaoOrigem")
        self.btn_centro_obejto = self.findChild(QRadioButton, "btnRotacaoCentroObjeto")
        self.eixo = self.findChild(QComboBox, "comoBoxEixo")
        self.input_rotacao_graus = self.findChild(QLineEdit, "inputRotacaoGraus")
        
        #Grupo do Shearing
        self.group_shearing = self.findChild(QGroupBox, "groupShearing")
        self.input_shearing_00 = self.findChild(QLineEdit, "shearing00")
        self.input_shearing_01 = self.findChild(QLineEdit, "shearing01")
        self.input_shearing_02 = self.findChild(QLineEdit, "shearing02")
        self.input_shearing_03 = self.findChild(QLineEdit, "shearing03")
        self.input_shearing_10 = self.findChild(QLineEdit, "shearing10")
        self.input_shearing_11 = self.findChild(QLineEdit, "shearing11")
        self.input_shearing_12 = self.findChild(QLineEdit, "shearing12")
        self.input_shearing_13 = self.findChild(QLineEdit, "shearing13")
        self.input_shearing_20 = self.findChild(QLineEdit, "shearing20")
        self.input_shearing_21 = self.findChild(QLineEdit, "shearing21")
        self.input_shearing_22 = self.findChild(QLineEdit, "shearing22")
        self.input_shearing_23 = self.findChild(QLineEdit, "shearing23")
        self.input_shearing_30 = self.findChild(QLineEdit, "shearing30")
        self.input_shearing_31 = self.findChild(QLineEdit, "shearing31")
        self.input_shearing_32 = self.findChild(QLineEdit, "shearing32")
        self.input_shearing_33 = self.findChild(QLineEdit, "shearing33")


if __name__ == '__main__':
	# Inicializa a janela
	app = QApplication(sys.argv)
	UIWindow = UI()
	app.exec_()