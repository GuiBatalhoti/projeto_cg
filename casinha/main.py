# Os pontos da casa são organizados da seguinte maneira:
# A = (0,0,0), B = (100,0,0), C = (100,0,100), D = (0,0,100),
# E = (0,100,0), F = (100,100,0), G = (100,100,100), H = (0,100,100),
# I = (50,150,0), J = (50,150,100).
# Os pontos que se ligam são 
# - AB, AD, AE;
# - BC, BF;
# - CD, CG;
# - DH;
# - EH, EI;
# - FI, FG;
# - GJ;
# - HJ;
# - IJ;

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QLabel, QGroupBox, QRadioButton, QComboBox
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QColor, QPainter, QPen
import sys
import numpy as np
from copy import deepcopy


class UI(QWidget):
    def __init__(self):
        # inicianlizando a interface
        super(UI, self).__init__()
        uic.loadUi('casinha/janela.ui', self)
        self.show()

        #Imagem do desenho
        self.canvas = QPixmap(10000,10000)

        #montando o abjeto de desenho
        self.painter = QPainter(self.canvas)
        self.canvas.fill(QColor(255,255,255))
        pen = QPen()
        self.painter.setPen(pen)

        # Pegando os elementos da interface
        self.label_img = self.findChild(QLabel, "labelImg")
        self.btn_executar = self.findChild(QPushButton, "btnExecuta")
        self.btn_resetar_pontos = self.findChild(QPushButton, "btnResetarPontos")

        #Pontos originais da casinha
        self.pontos_originais = {"a":[0,0,0,1], "b":[100,0,0,1], "c":[100,0,100,1], "d":[0,0,100,1], 
                                 "e":[0,100,0,1], "f":[100,100,0,1], "g":[100,100,100,1], "h":[0,100,100,1],
                                 "i":[50,150,0,1], "j":[50,150,100,1]}
        self.pontos_modificados = None

        #coloca os pontos originais dentro dos pontos modificados
        self.resetar_pontos()

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
        self.btn_centro_objeto = self.findChild(QRadioButton, "btnRotacaoCentroObjeto")
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

        #Evento de quando clicar em Executar
        self.btn_executar.clicked.connect(self.executar)
        self.btn_resetar_pontos.clicked.connect(self.resetar_pontos)

        #rederizando a primeira casinha
        self.render()

    
    def resetar_pontos(self):
        print("Pontos resetados!!\n")
        self.pontos_modificados = deepcopy(self.pontos_originais)
        self.render()
        
        
    def executar(self):
        # Realiza as operações

        for key in self.pontos_modificados.keys():
            if self.group_escala.isChecked():
                self.pontos_modificados[key] = self.operacao_escala(self.pontos_modificados[key])

            """if self.group_translacao.isChecked():
                ponto = self.operacao_translacao(ponto)

            if self.group_rotacao.isChecked():
                ponto = self.operacao_rotacao(ponto)

            if self.group_she
            aring.isChecked():
                ponto = self.operacao_shearing(ponto)"""

        self.render()

    
    def operacao_escala(self, ponto: list) -> list:
        # Matriz de multiplicação
        matriz = np.identity(4)
        ponto = np.array(ponto)

        if self.btn_global.isChecked():
            valor_global = float(self.input_escala_global.text())
            matriz[3][3] = valor_global
            
            produto = np.dot(ponto, matriz).astype(float)

            if produto[3] != 1:
                produto = [int(i/produto[3]) for i in produto]
            else:
                produto = [int(i) for i in produto]
            
            return produto
            
        elif self.btn_local.isChecked():
            valor_x = float(self.input_escala_x.text())
            valor_y = float(self.input_escala_y.text())
            valor_z = float(self.input_escala_z.text())

            matriz[0][0] = valor_x
            matriz[1][1] = valor_y
            matriz[2][2] = valor_z

            produto = np.dot(ponto, matriz).astype(float)

            if produto[3] != 1:
                produto = [int(i/produto[3]) for i in produto]
            else:
                produto = [int(i) for i in produto]

            return produto


    def operacao_translacao(self, ponto: list) -> list:
        pass


    def operacao_rotacao(self, ponto: list) -> list:
        if self.btn_origem.isChecked():
            print("Origem \n")
        else:
            print("Centro do Objeto\n")


    def operacao_shearing(self, ponto):
        pass


    def render(self):
        self.canvas.fill(QColor(255,255,255))
        self.painter.drawLine(self.pontos_modificados["a"][0], self.pontos_modificados["a"][1], self.pontos_modificados["b"][0], self.pontos_modificados["b"][1])
        self.painter.drawLine(self.pontos_modificados["a"][0], self.pontos_modificados["a"][1], self.pontos_modificados["d"][0], self.pontos_modificados["d"][1])
        self.painter.drawLine(self.pontos_modificados["a"][0], self.pontos_modificados["a"][1], self.pontos_modificados["e"][0], self.pontos_modificados["e"][1])
        self.painter.drawLine(self.pontos_modificados["b"][0], self.pontos_modificados["b"][1], self.pontos_modificados["c"][0], self.pontos_modificados["c"][1])
        self.painter.drawLine(self.pontos_modificados["b"][0], self.pontos_modificados["b"][1], self.pontos_modificados["f"][0], self.pontos_modificados["f"][1])
        self.painter.drawLine(self.pontos_modificados["c"][0], self.pontos_modificados["c"][1], self.pontos_modificados["d"][0], self.pontos_modificados["d"][1])
        self.painter.drawLine(self.pontos_modificados["c"][0], self.pontos_modificados["c"][1], self.pontos_modificados["g"][0], self.pontos_modificados["g"][1])
        self.painter.drawLine(self.pontos_modificados["d"][0], self.pontos_modificados["d"][1], self.pontos_modificados["h"][0], self.pontos_modificados["h"][1])
        self.painter.drawLine(self.pontos_modificados["e"][0], self.pontos_modificados["e"][1], self.pontos_modificados["h"][0], self.pontos_modificados["h"][1])
        self.painter.drawLine(self.pontos_modificados["e"][0], self.pontos_modificados["e"][1], self.pontos_modificados["i"][0], self.pontos_modificados["i"][1])
        self.painter.drawLine(self.pontos_modificados["f"][0], self.pontos_modificados["f"][1], self.pontos_modificados["i"][0], self.pontos_modificados["i"][1])
        self.painter.drawLine(self.pontos_modificados["f"][0], self.pontos_modificados["f"][1], self.pontos_modificados["g"][0], self.pontos_modificados["g"][1])
        self.painter.drawLine(self.pontos_modificados["g"][0], self.pontos_modificados["g"][1], self.pontos_modificados["j"][0], self.pontos_modificados["j"][1])
        self.painter.drawLine(self.pontos_modificados["h"][0], self.pontos_modificados["h"][1], self.pontos_modificados["j"][0], self.pontos_modificados["j"][1])
        self.painter.drawLine(self.pontos_modificados["i"][0], self.pontos_modificados["i"][1], self.pontos_modificados["j"][0], self.pontos_modificados["j"][1])

        self.label_img.setPixmap(self.canvas)
    


if __name__ == '__main__':
	# Inicializa a janela
	app = QApplication(sys.argv)
	UIWindow = UI()
	app.exec_()