# Os pontos_modificados da casa são organizados da seguinte maneira:
# A = (0,0,0), B = (100,0,0), C = (100,0,100), D = (0,0,100),
# E = (0,100,0), F = (100,100,0), G = (100,100,100), H = (0,100,100),
# I = (50,150,0), J = (50,150,100).
# Os pontos_modificados que se ligam são 
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


class UI(QWidget):
    def __init__(self):
        # inicianlizando a interface
        super(UI, self).__init__()
        uic.loadUi('casinha/janela.ui', self)
        self.show()

        #Imagem do desenho
        self.canvas = QPixmap(5000,5000)

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
        self.pontos_originais = {"a":[0.0,0.0,0.0,1.0], "b":[100.0,0.0,0.0,1.0], "c":[100.0,0.0,100.0,1.0], "d":[0.0,0.0,100.0,1.0], 
                                 "e":[0.0,100.0,0.0,1.0], "f":[100.0,100.0,0.0,1.0], "g":[100.0,100.0,100.0,1.0], "h":[0.0,100.0,100.0,1.0],
                                 "i":[50.0,150.0,0.0,1.0], "j":[50.0,150.0,100.0,1.0]}
        self.pontos_modificados = None

        # deslocar os pontos para o centro da tela
        for ponto in self.pontos_originais:
            self.pontos_originais[ponto][0] *= -1
            self.pontos_originais[ponto][1] *= -1
            self.pontos_originais[ponto][2] *= -1
            self.pontos_originais[ponto][0] += 400
            self.pontos_originais[ponto][1] += 400
            self.pontos_originais[ponto][2] += 400

        #coloca os pontos_modificados originais dentro dos pontos_modificados modificados
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
        self.input_translacao_x = self.findChild(QLineEdit, "inputTranslacaoX")
        self.input_translacao_y = self.findChild(QLineEdit, "inputTranslacaoY")
        self.input_translacao_z = self.findChild(QLineEdit, "inputTranslacaoZ")

        #Grupo da Rotação
        self.group_rotacao = self.findChild(QGroupBox, "groupRotacao")
        self.btn_origem = self.findChild(QRadioButton, "btnRotacaoOrigem")
        self.btn_centro_objeto = self.findChild(QRadioButton, "btnRotacaoCentroObjeto")
        self.eixo_rotacao = self.findChild(QComboBox, "comboBoxEixo")
        self.input_angulo_rotacao = self.findChild(QLineEdit, "inputRotacaoGraus")
        
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


        self.render()
        
    
    def resetar_pontos(self):
        self.pontos_modificados = self.pontos_originais.copy()
        print("Pontos resetados!!\n")
        self.render()
        
        
    def executar(self):

        centro_objeto = self.centro_objeto()

        # Realiza as operações
        for key in self.pontos_modificados.keys():
            if self.group_escala.isChecked():
                self.pontos_modificados[key] = self.operacao_escala(self.pontos_modificados[key])
            if self.group_translacao.isChecked():
                self.pontos_modificados[key] = self.operacao_translacao(self.pontos_modificados[key])
            if self.group_rotacao.isChecked():
                self.pontos_modificados[key] = self.operacao_rotacao(self.pontos_modificados[key], centro_objeto)
            if self.group_shearing.isChecked():
                self.pontos_modificados[key] = self.operacao_shearing(self.pontos_modificados[key])
        self.render()


    def render(self):
        # Desenha a tela 
        self.canvas.fill(QColor(255,255,255))
        self.painter.drawLine(int(self.pontos_modificados["a"][0]), int(self.pontos_modificados["a"][1]), int(self.pontos_modificados["b"][0]), int(self.pontos_modificados["b"][1]))
        self.painter.drawLine(int(self.pontos_modificados["a"][0]), int(self.pontos_modificados["a"][1]), int(self.pontos_modificados["d"][0]), int(self.pontos_modificados["d"][1]))
        self.painter.drawLine(int(self.pontos_modificados["a"][0]), int(self.pontos_modificados["a"][1]), int(self.pontos_modificados["e"][0]), int(self.pontos_modificados["e"][1]))
        self.painter.drawLine(int(self.pontos_modificados["b"][0]), int(self.pontos_modificados["b"][1]), int(self.pontos_modificados["c"][0]), int(self.pontos_modificados["c"][1]))
        self.painter.drawLine(int(self.pontos_modificados["b"][0]), int(self.pontos_modificados["b"][1]), int(self.pontos_modificados["f"][0]), int(self.pontos_modificados["f"][1]))
        self.painter.drawLine(int(self.pontos_modificados["c"][0]), int(self.pontos_modificados["c"][1]), int(self.pontos_modificados["d"][0]), int(self.pontos_modificados["d"][1]))
        self.painter.drawLine(int(self.pontos_modificados["c"][0]), int(self.pontos_modificados["c"][1]), int(self.pontos_modificados["g"][0]), int(self.pontos_modificados["g"][1]))
        self.painter.drawLine(int(self.pontos_modificados["d"][0]), int(self.pontos_modificados["d"][1]), int(self.pontos_modificados["h"][0]), int(self.pontos_modificados["h"][1]))
        self.painter.drawLine(int(self.pontos_modificados["e"][0]), int(self.pontos_modificados["e"][1]), int(self.pontos_modificados["h"][0]), int(self.pontos_modificados["h"][1]))
        self.painter.drawLine(int(self.pontos_modificados["e"][0]), int(self.pontos_modificados["e"][1]), int(self.pontos_modificados["i"][0]), int(self.pontos_modificados["i"][1]))
        self.painter.drawLine(int(self.pontos_modificados["f"][0]), int(self.pontos_modificados["f"][1]), int(self.pontos_modificados["i"][0]), int(self.pontos_modificados["i"][1]))
        self.painter.drawLine(int(self.pontos_modificados["f"][0]), int(self.pontos_modificados["f"][1]), int(self.pontos_modificados["g"][0]), int(self.pontos_modificados["g"][1]))
        self.painter.drawLine(int(self.pontos_modificados["g"][0]), int(self.pontos_modificados["g"][1]), int(self.pontos_modificados["j"][0]), int(self.pontos_modificados["j"][1]))
        self.painter.drawLine(int(self.pontos_modificados["h"][0]), int(self.pontos_modificados["h"][1]), int(self.pontos_modificados["j"][0]), int(self.pontos_modificados["j"][1]))
        self.painter.drawLine(int(self.pontos_modificados["i"][0]), int(self.pontos_modificados["i"][1]), int(self.pontos_modificados["j"][0]), int(self.pontos_modificados["j"][1]))

        self.label_img.setPixmap(self.canvas)

    
    def operacao_escala(self, ponto: list) -> list:
        # Matriz de multiplicação
        matriz = np.identity(4)

        # Tranformando em numpy array para fazer a multiplicação
        ponto = np.array(ponto)

        # Se for escala Global
        if self.btn_global.isChecked():
            #pegando o valor da escala global 
            matriz[3][3] = float(self.input_escala_global.text())
            
            # Fazendo o produto entre a matriz e o ponto
            produto = np.dot(ponto, matriz).astype(float)

            #verificando as coordenadas homegêneas
            produto = self.verifica_coord_homogenea(produto)
            
            return produto
            
        # Se for escala local
        elif self.btn_local.isChecked():
            # Pegando os valores da escala local
            matriz[0][0] = float(self.input_escala_x.text())
            matriz[1][1] = float(self.input_escala_y.text())
            matriz[2][2] = float(self.input_escala_z.text())

            # Fazendo o produto
            produto = np.dot(ponto, matriz).astype(float)

            #verificando as coordenadas homegêneas
            produto = self.verifica_coord_homogenea(produto)

            return produto

        # se nada for selecionado retornar o próprio ponto,
        # é um caso impossível, mas apenas por garantia
        else:
            return ponto


    def operacao_translacao(self, ponto: list) -> list:
        # Matriz de multiplicação
        matriz = np.identity(4)

        # Tranformando em numpy array para fazer a multiplicação
        ponto = np.array(ponto)

        # pegando os valores de entrada
        matriz[3][0] = float(self.input_translacao_x.text())
        matriz[3][1] = float(self.input_translacao_y.text())
        matriz[3][2] = float(self.input_translacao_z.text())

        produto = np.dot(ponto, matriz)

        #verificando as coordenadas homegêneas
        produto = self.verifica_coord_homogenea(produto)

        return produto


    def operacao_rotacao(self, ponto: list, centro_objeto: list) -> list:
        # Tranformando em numpy array para fazer a multiplicação
        ponto = np.array(ponto)

        #se for rotação na origem
        if self.btn_origem.isChecked():
            # rotação apenas com as matrizes de rotação sem deslocamento
            matriz = self.matriz_rotacao()
            # Fazendo o produto
            produto = np.dot(ponto, matriz)
            #verificando as coordenadas homegêneas
            produto = self.verifica_coord_homogenea(produto)
            return produto

        # se for rotação no centro do objeto
        elif self.btn_centro_objeto.isChecked():
            # montando as matrizes necessárias para a operação
            matriz_rotacao = self.matriz_rotacao()
            matriz_translacao_centro = np.identity(4)
            matriz_translacao_centro[3][0] = -centro_objeto[0]
            matriz_translacao_centro[3][1] = -centro_objeto[1]
            matriz_translacao_centro[3][2] = -centro_objeto[2]

            matriz_translacao_centro_inversa = np.identity(4)
            matriz_translacao_centro_inversa[3][0] = centro_objeto[0]
            matriz_translacao_centro_inversa[3][1] = centro_objeto[1]
            matriz_translacao_centro_inversa[3][2] = centro_objeto[2]
            
            # leva o centro do objeto até a origem, rotaciona e volta para a aposição original
            produto = np.dot(np.dot(np.dot(ponto, matriz_translacao_centro), matriz_rotacao), matriz_translacao_centro_inversa)
            
            #verificando as coordenadas homegêneas
            produto = self.verifica_coord_homogenea(produto)

            return produto

        # se nada for selecionado retornar o próprio ponto,
        # é um caso impossível, mas apenas por garantia
        else:
            return ponto


    def operacao_shearing(self, ponto: list) -> list:
        # Matriz de multiplicação
        matriz = np.identity(4)

        # Tranformando em numpy array para fazer a multiplicação
        ponto = np.array(ponto)

        # Pegando os valores de entrada
        matriz[0][0] = float(self.input_shearing_00.text())
        matriz[0][1] = float(self.input_shearing_01.text())
        matriz[0][2] = float(self.input_shearing_02.text())
        matriz[0][3] = float(self.input_shearing_03.text())
        matriz[1][0] = float(self.input_shearing_10.text())
        matriz[1][1] = float(self.input_shearing_11.text())
        matriz[1][2] = float(self.input_shearing_12.text())
        matriz[1][3] = float(self.input_shearing_13.text())
        matriz[2][0] = float(self.input_shearing_20.text())
        matriz[2][1] = float(self.input_shearing_21.text())
        matriz[2][2] = float(self.input_shearing_22.text())
        matriz[2][3] = float(self.input_shearing_23.text())
        matriz[3][0] = float(self.input_shearing_30.text())
        matriz[3][1] = float(self.input_shearing_31.text())
        matriz[3][2] = float(self.input_shearing_32.text())
        matriz[3][3] = float(self.input_shearing_33.text())

        # Fazendo o produto entre a matriz e o ponto
        produto = np.dot(ponto, matriz)
        
        #verificando as coordenadas homogêneas
        produto = self.verifica_coord_homogenea(produto)

        return produto


    def verifica_coord_homogenea(self, produto: list) -> list:
        # Transformando em coordenadas homogênas ou somente fazendo o cast para inteiro
        if produto[3] != 1:
            produto = [i/produto[3] for i in produto]
        return produto


    def matriz_rotacao(self):
        # retorna a matriz de rotação específica do tipo de rotação
        eixo = str(self.eixo_rotacao.currentText())
        angulo = float(self.input_angulo_rotacao.text())
        
        # verificando qual é o eixo de rotação
        if eixo == "X":
            return np.array([[1, 0, 0, 0],
                            [0, np.cos(angulo), -np.sin(angulo), 0],
                            [0, np.sin(angulo), np.cos(angulo), 0],
                            [0, 0, 0, 1]])

        elif eixo == "Y":
            return np.array([[np.cos(angulo), 0, np.sin(angulo), 0],
                            [0, 1, 0, 0],
                            [-np.sin(angulo), 0, np.cos(angulo), 0],
                            [0, 0, 0, 1]])
            
        #o exio Z será o padrão
        else:
            return np.array([[np.cos(angulo), -np.sin(angulo), 0, 0],
                             [np.sin(angulo), np.cos(angulo), 0, 0],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]])
    

    def centro_objeto(self):
        # retorna o centro do objeto passabdo pelos pontos modificados
        tamanho = len(self.pontos_modificados.values())
        x = y = z = 0
        for i in self.pontos_modificados.values():
            x += i[0]
            y += i[1]
            z += i[2]
        return [x/tamanho, y/tamanho, z/tamanho]


if __name__ == '__main__':
	# Inicializa a janela
	app = QApplication(sys.argv)
	UIWindow = UI()
	app.exec_()