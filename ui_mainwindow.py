# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1050, 864)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 40))
        self.frame_superior.setMaximumSize(QSize(16777215, 40))
        self.frame_superior.setStyleSheet(u"background-color: rgb(19, 86, 120);")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_menu = QPushButton(self.frame_superior)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setMinimumSize(QSize(200, 35))
        self.btn_menu.setMaximumSize(QSize(16777215, 35))
        self.btn_menu.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	alternate-background-color: rgb(60, 115, 120);\n"
"	font: 87 12pt \"Arial Black\";\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(60, 100, 120);\n"
"	font: 87 12pt \"Arial Black\";\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u"images/lista.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btn_menu)

        self.horizontalSpacer = QSpacerItem(656, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_minimizar = QPushButton(self.frame_superior)
        self.btn_minimizar.setObjectName(u"btn_minimizar")
        self.btn_minimizar.setMaximumSize(QSize(16777215, 35))
        self.btn_minimizar.setStyleSheet(u"QPushButton{\n"
"border-radius:7px;\n"
"background-color: rgb(60, 100, 120);\n"
"}\n"
"QPushButton:hover{\n"
"	border:10px solid rgb(50, 83, 100);\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"images/3686939.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimizar.setIcon(icon1)
        self.btn_minimizar.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btn_minimizar)

        self.btn_restaurar = QPushButton(self.frame_superior)
        self.btn_restaurar.setObjectName(u"btn_restaurar")
        self.btn_restaurar.setMaximumSize(QSize(16777215, 35))
        self.btn_restaurar.setStyleSheet(u"QPushButton{\n"
"border-radius:7px;\n"
"background-color: rgb(60, 100, 120);\n"
"}\n"
"QPushButton:hover{\n"
"	border:5px solid rgb(50, 83, 100);\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"images/3287392.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_restaurar.setIcon(icon2)
        self.btn_restaurar.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btn_restaurar)

        self.btn_maximizar = QPushButton(self.frame_superior)
        self.btn_maximizar.setObjectName(u"btn_maximizar")
        self.btn_maximizar.setMaximumSize(QSize(16777215, 35))
        self.btn_maximizar.setStyleSheet(u"QPushButton{\n"
"border-radius:7px;\n"
"background-color: rgb(60, 100, 120);\n"
"}\n"
"QPushButton:hover{\n"
"	border:5px solid rgb(50, 83, 100);\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"images/3287396.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximizar.setIcon(icon3)
        self.btn_maximizar.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btn_maximizar)

        self.btn_cerrar = QPushButton(self.frame_superior)
        self.btn_cerrar.setObjectName(u"btn_cerrar")
        self.btn_cerrar.setMaximumSize(QSize(16777215, 35))
        self.btn_cerrar.setStyleSheet(u"QPushButton{\n"
"border-radius:7px;\n"
"background-color: rgb(60, 100, 120);\n"
"}\n"
"QPushButton:hover{\n"
"	border:10px solid rgb(50, 83, 100);\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"images/51517.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cerrar.setIcon(icon4)
        self.btn_cerrar.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btn_cerrar)


        self.verticalLayout.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.centralwidget)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_menu = QFrame(self.frame_inferior)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(200, 0))
        self.frame_menu.setMaximumSize(QSize(0, 16777215))
        self.frame_menu.setStyleSheet(u"QFrame{\n"
"background-color: rgb(60, 100, 120);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(0, 85, 120);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"font: 75 12pt \"Arial Narrow\";\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(50, 84, 100);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"font: 75 12pt \"Arial Narrow\";\n"
"}")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 5)
        self.btn_inicio = QPushButton(self.frame_menu)
        self.btn_inicio.setObjectName(u"btn_inicio")
        self.btn_inicio.setMinimumSize(QSize(0, 40))
        self.btn_inicio.setMaximumSize(QSize(16777215, 40))
        self.btn_inicio.setLayoutDirection(Qt.LeftToRight)
        self.btn_inicio.setAutoFillBackground(False)
        self.btn_inicio.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_inicio.setText(u"   Inicio")
        icon5 = QIcon()
        icon5.addFile(u"images/845022.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_inicio.setIcon(icon5)
        self.btn_inicio.setIconSize(QSize(30, 30))
        self.btn_inicio.setCheckable(False)
        self.btn_inicio.setChecked(False)
        self.btn_inicio.setAutoExclusive(False)
        self.btn_inicio.setAutoDefault(False)
        self.btn_inicio.setFlat(False)

        self.verticalLayout_3.addWidget(self.btn_inicio)

        self.btn_viajes = QPushButton(self.frame_menu)
        self.btn_viajes.setObjectName(u"btn_viajes")
        self.btn_viajes.setMinimumSize(QSize(0, 40))
        self.btn_viajes.setMaximumSize(QSize(16777215, 40))
        self.btn_viajes.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon6 = QIcon()
        icon6.addFile(u"images/carro-familiar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_viajes.setIcon(icon6)
        self.btn_viajes.setIconSize(QSize(30, 30))
        self.btn_viajes.setCheckable(False)
        self.btn_viajes.setChecked(False)
        self.btn_viajes.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.btn_viajes)

        self.btn_conductor = QPushButton(self.frame_menu)
        self.btn_conductor.setObjectName(u"btn_conductor")
        self.btn_conductor.setMinimumSize(QSize(0, 40))
        self.btn_conductor.setMaximumSize(QSize(16777215, 40))
        self.btn_conductor.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon7 = QIcon()
        icon7.addFile(u"images/conductor (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_conductor.setIcon(icon7)
        self.btn_conductor.setIconSize(QSize(30, 30))
        self.btn_conductor.setCheckable(False)
        self.btn_conductor.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.btn_conductor)

        self.btn_historico = QPushButton(self.frame_menu)
        self.btn_historico.setObjectName(u"btn_historico")
        self.btn_historico.setMinimumSize(QSize(0, 40))
        self.btn_historico.setMaximumSize(QSize(16777215, 40))
        self.btn_historico.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon8 = QIcon()
        icon8.addFile(u"images/1584786.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_historico.setIcon(icon8)
        self.btn_historico.setIconSize(QSize(30, 30))
        self.btn_historico.setCheckable(False)
        self.btn_historico.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.btn_historico)

        self.btn_factura = QPushButton(self.frame_menu)
        self.btn_factura.setObjectName(u"btn_factura")
        self.btn_factura.setMinimumSize(QSize(0, 40))
        self.btn_factura.setMaximumSize(QSize(16777215, 40))
        self.btn_factura.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon9 = QIcon()
        icon9.addFile(u"images/679769 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_factura.setIcon(icon9)
        self.btn_factura.setIconSize(QSize(30, 30))
        self.btn_factura.setCheckable(False)
        self.btn_factura.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.btn_factura)

        self.btn_ajustes = QPushButton(self.frame_menu)
        self.btn_ajustes.setObjectName(u"btn_ajustes")
        self.btn_ajustes.setMinimumSize(QSize(0, 40))
        self.btn_ajustes.setMaximumSize(QSize(16777215, 40))
        self.btn_ajustes.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon10 = QIcon()
        icon10.addFile(u"images/1077198.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ajustes.setIcon(icon10)
        self.btn_ajustes.setIconSize(QSize(30, 30))
        self.btn_ajustes.setCheckable(False)
        self.btn_ajustes.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.btn_ajustes)

        self.verticalSpacer = QSpacerItem(20, 263, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label = QLabel(self.frame_menu)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_menu)

        self.frame_contenedor = QFrame(self.frame_inferior)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        self.frame_contenedor.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_contenedor)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_contenedor)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"QStackedWidget::setStyleSheet(\"QStackedWidget:: QToolButton {border: none;}\")")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.stackedWidget.setLineWidth(1)
        self.pg_inicio = QWidget()
        self.pg_inicio.setObjectName(u"pg_inicio")
        self.verticalLayout_17 = QVBoxLayout(self.pg_inicio)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_5 = QFrame(self.pg_inicio)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 350))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.groupBox_5 = QGroupBox(self.frame_5)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(16777215, 156))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.groupBox_5.setFont(font1)
        self.groupBox_5.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(240, 240, 240, 255), stop:1 rgba(60, 115, 150, 255));\n"
"border-top-left-radius:30px;\n"
" border-bottom-right-radius:30px;\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(90, 90))
        self.label_10.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_10.setPixmap(QPixmap(u"images/3388856.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setWordWrap(False)

        self.horizontalLayout_6.addWidget(self.label_10)

        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(81, 31))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_11.setFont(font2)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.horizontalSpacer_7 = QSpacerItem(607, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.label_13 = QLabel(self.groupBox_5)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(90, 90))
        self.label_13.setMaximumSize(QSize(90, 90))
        self.label_13.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_13.setPixmap(QPixmap(u"images/5044540.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_13)


        self.verticalLayout_6.addWidget(self.groupBox_5)

        self.frame_18 = QFrame(self.frame_5)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_18)
        self.verticalLayout_24.setSpacing(6)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.groupBox_22 = QGroupBox(self.frame_18)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.groupBox_22.setMaximumSize(QSize(16777215, 60))
        self.groupBox_22.setStyleSheet(u"background-color: rgb(250, 250, 250);\n"
"border:none;")
        self.gridLayout_26 = QGridLayout(self.groupBox_22)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_24 = QLabel(self.groupBox_22)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_26.addWidget(self.label_24, 0, 0, 1, 1)


        self.verticalLayout_24.addWidget(self.groupBox_22)

        self.groupBox_18 = QGroupBox(self.frame_18)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.gridLayout_25 = QGridLayout(self.groupBox_18)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setVerticalSpacing(8)
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_22 = QLabel(self.groupBox_18)
        self.label_22.setObjectName(u"label_22")
        font3 = QFont()
        font3.setPointSize(10)
        self.label_22.setFont(font3)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_22)

        self.fecha_sistema_dateTimeEdit = QDateTimeEdit(self.groupBox_18)
        self.fecha_sistema_dateTimeEdit.setObjectName(u"fecha_sistema_dateTimeEdit")
        self.fecha_sistema_dateTimeEdit.setFont(font3)
        self.fecha_sistema_dateTimeEdit.setWrapping(False)
        self.fecha_sistema_dateTimeEdit.setFrame(False)
        self.fecha_sistema_dateTimeEdit.setAlignment(Qt.AlignCenter)
        self.fecha_sistema_dateTimeEdit.setReadOnly(True)
        self.fecha_sistema_dateTimeEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.fecha_sistema_dateTimeEdit.setProperty("showGroupSeparator", False)
        self.fecha_sistema_dateTimeEdit.setDateTime(QDateTime(QDate(2023, 4, 9), QTime(12, 27, 0)))
        self.fecha_sistema_dateTimeEdit.setTime(QTime(12, 27, 0))

        self.verticalLayout_25.addWidget(self.fecha_sistema_dateTimeEdit)

        self.label_33 = QLabel(self.groupBox_18)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font3)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_33)

        self.ledt_numero_semana = QLineEdit(self.groupBox_18)
        self.ledt_numero_semana.setObjectName(u"ledt_numero_semana")
        self.ledt_numero_semana.setFrame(False)
        self.ledt_numero_semana.setAlignment(Qt.AlignCenter)
        self.ledt_numero_semana.setReadOnly(True)

        self.verticalLayout_25.addWidget(self.ledt_numero_semana)


        self.gridLayout_25.addLayout(self.verticalLayout_25, 0, 0, 1, 1)


        self.verticalLayout_24.addWidget(self.groupBox_18)


        self.verticalLayout_6.addWidget(self.frame_18)


        self.verticalLayout_17.addWidget(self.frame_5)

        self.frame_23 = QFrame(self.pg_inicio)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_23)
        self.gridLayout_22.setSpacing(0)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.groupBox_16 = QGroupBox(self.frame_23)
        self.groupBox_16.setObjectName(u"groupBox_16")
        sizePolicy.setHeightForWidth(self.groupBox_16.sizePolicy().hasHeightForWidth())
        self.groupBox_16.setSizePolicy(sizePolicy)
        self.gridLayout_23 = QGridLayout(self.groupBox_16)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_15)

        self.label_16 = QLabel(self.groupBox_16)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_21.addWidget(self.label_16)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_3)

        self.label_20 = QLabel(self.groupBox_16)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_21.addWidget(self.label_20)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_6)

        self.label_21 = QLabel(self.groupBox_16)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_21.addWidget(self.label_21)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_7)

        self.label_17 = QLabel(self.groupBox_16)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(180, 0))

        self.verticalLayout_21.addWidget(self.label_17)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_8)

        self.label_18 = QLabel(self.groupBox_16)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_21.addWidget(self.label_18)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_9)

        self.label_19 = QLabel(self.groupBox_16)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_21.addWidget(self.label_19)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_17)


        self.horizontalLayout_7.addLayout(self.verticalLayout_21)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_16)

        self.dateTimeEdit_2 = QDateTimeEdit(self.groupBox_16)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setWrapping(False)
        self.dateTimeEdit_2.setFrame(False)
        self.dateTimeEdit_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.dateTimeEdit_2.setReadOnly(True)
        self.dateTimeEdit_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateTimeEdit_2.setDateTime(QDateTime(QDate(2023, 4, 9), QTime(12, 27, 0)))
        self.dateTimeEdit_2.setTime(QTime(12, 27, 0))

        self.verticalLayout_22.addWidget(self.dateTimeEdit_2)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_10)

        self.lineEdit_5 = QLineEdit(self.groupBox_16)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFrame(False)
        self.lineEdit_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_5.setReadOnly(True)

        self.verticalLayout_22.addWidget(self.lineEdit_5)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_11)

        self.lineEdit_6 = QLineEdit(self.groupBox_16)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFrame(False)
        self.lineEdit_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_6.setReadOnly(True)

        self.verticalLayout_22.addWidget(self.lineEdit_6)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_12)

        self.lineEdit_2 = QLineEdit(self.groupBox_16)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_2.setReadOnly(True)

        self.verticalLayout_22.addWidget(self.lineEdit_2)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_13)

        self.lineEdit_3 = QLineEdit(self.groupBox_16)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_3.setReadOnly(True)

        self.verticalLayout_22.addWidget(self.lineEdit_3)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_14)

        self.lineEdit_4 = QLineEdit(self.groupBox_16)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFrame(False)
        self.lineEdit_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_4.setReadOnly(True)

        self.verticalLayout_22.addWidget(self.lineEdit_4)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_18)


        self.horizontalLayout_7.addLayout(self.verticalLayout_22)


        self.gridLayout_23.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_9, 0, 0, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_17, 0, 2, 1, 1)


        self.gridLayout_22.addWidget(self.groupBox_16, 0, 0, 1, 1)


        self.verticalLayout_17.addWidget(self.frame_23)

        self.stackedWidget.addWidget(self.pg_inicio)
        self.pg_viaje = QWidget()
        self.pg_viaje.setObjectName(u"pg_viaje")
        self.verticalLayout_23 = QVBoxLayout(self.pg_viaje)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame = QFrame(self.pg_viaje)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 243))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 156))
        self.groupBox_2.setFont(font1)
        self.groupBox_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(240, 240, 240, 255), stop:1 rgba(60, 115, 150, 255));\n"
"border-top-left-radius:30px;\n"
" border-bottom-right-radius:30px;\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(111, 131))
        self.label_9.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_9.setPixmap(QPixmap(u"images/4277494.png"))

        self.horizontalLayout_3.addWidget(self.label_9)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(81, 31))
        self.label_3.setFont(font2)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(607, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QSize(90, 90))
        self.label_12.setMaximumSize(QSize(90, 90))
        self.label_12.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_12.setPixmap(QPixmap(u"images/1672225.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_12)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_21 = QGroupBox(self.frame)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setMinimumSize(QSize(0, 0))
        self.groupBox_21.setMaximumSize(QSize(16777215, 85))
        self.groupBox_21.setFont(font3)
        self.groupBox_21.setStyleSheet(u"background-color: rgb(250, 250, 250);\n"
"border:none;")
        self.horizontalLayout_19 = QHBoxLayout(self.groupBox_21)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 6)
        self.label_7 = QLabel(self.groupBox_21)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 0))
        self.label_7.setMaximumSize(QSize(900, 160))

        self.horizontalLayout_19.addWidget(self.label_7)


        self.verticalLayout_4.addWidget(self.groupBox_21)


        self.verticalLayout_23.addWidget(self.frame)

        self.frame_19 = QFrame(self.pg_viaje)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 190))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_19)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.groupBox_6 = QGroupBox(self.frame_19)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(0, 190))
        self.groupBox_6.setMaximumSize(QSize(16777215, 190))
        self.groupBox_6.setFont(font3)
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, -1)
        self.horizontalSpacer_31 = QSpacerItem(39, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_31)

        self.frame_34 = QFrame(self.groupBox_6)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_34)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(315, 141))
        self.frame_35.setMaximumSize(QSize(301, 141))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_35)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_76 = QLabel(self.frame_35)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font3)

        self.gridLayout_28.addWidget(self.label_76, 0, 0, 1, 1)

        self.ledt_viajes_folio = QLineEdit(self.frame_35)
        self.ledt_viajes_folio.setObjectName(u"ledt_viajes_folio")

        self.gridLayout_28.addWidget(self.ledt_viajes_folio, 0, 1, 1, 1)

        self.label_77 = QLabel(self.frame_35)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font3)

        self.gridLayout_28.addWidget(self.label_77, 1, 0, 1, 1)

        self.ledt_viajes_conductor = QLineEdit(self.frame_35)
        self.ledt_viajes_conductor.setObjectName(u"ledt_viajes_conductor")

        self.gridLayout_28.addWidget(self.ledt_viajes_conductor, 1, 1, 1, 1)

        self.label_78 = QLabel(self.frame_35)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font3)

        self.gridLayout_28.addWidget(self.label_78, 2, 0, 1, 1)

        self.ledt_viajes_empresa = QLineEdit(self.frame_35)
        self.ledt_viajes_empresa.setObjectName(u"ledt_viajes_empresa")

        self.gridLayout_28.addWidget(self.ledt_viajes_empresa, 2, 1, 1, 1)

        self.label_79 = QLabel(self.frame_35)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font3)

        self.gridLayout_28.addWidget(self.label_79, 3, 0, 1, 1)

        self.ledt_viajes_matricula = QLineEdit(self.frame_35)
        self.ledt_viajes_matricula.setObjectName(u"ledt_viajes_matricula")

        self.gridLayout_28.addWidget(self.ledt_viajes_matricula, 3, 1, 1, 1)

        self.label_80 = QLabel(self.frame_35)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setFont(font3)

        self.gridLayout_28.addWidget(self.label_80, 4, 0, 1, 1)

        self.ledt_viajes_tipo = QLineEdit(self.frame_35)
        self.ledt_viajes_tipo.setObjectName(u"ledt_viajes_tipo")

        self.gridLayout_28.addWidget(self.ledt_viajes_tipo, 4, 1, 1, 1)


        self.gridLayout_27.addWidget(self.frame_35, 0, 0, 1, 1)


        self.horizontalLayout_15.addWidget(self.frame_34)

        self.frame_33 = QFrame(self.groupBox_6)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_33)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.verticalSpacer_5 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_24.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.horizontalSpacer_32 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_32, 1, 0, 1, 1)

        self.btn_guardar_viaje = QPushButton(self.frame_33)
        self.btn_guardar_viaje.setObjectName(u"btn_guardar_viaje")
        self.btn_guardar_viaje.setMinimumSize(QSize(80, 25))
        self.btn_guardar_viaje.setStyleSheet(u"QPushButton{\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"	background-color: rgb(60, 115, 120);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 85, 120);\n"
"}")

        self.gridLayout_24.addWidget(self.btn_guardar_viaje, 1, 1, 1, 1)

        self.horizontalSpacer_33 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_33, 1, 2, 1, 1)


        self.horizontalLayout_15.addWidget(self.frame_33)

        self.frame_36 = QFrame(self.groupBox_6)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_36)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.frame_37 = QFrame(self.frame_36)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(315, 141))
        self.frame_37.setMaximumSize(QSize(301, 141))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_37)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.label_81 = QLabel(self.frame_37)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setFont(font3)

        self.gridLayout_30.addWidget(self.label_81, 0, 0, 1, 1)

        self.ledt_viajes_contacto = QLineEdit(self.frame_37)
        self.ledt_viajes_contacto.setObjectName(u"ledt_viajes_contacto")

        self.gridLayout_30.addWidget(self.ledt_viajes_contacto, 0, 1, 1, 1)

        self.label_82 = QLabel(self.frame_37)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setFont(font3)

        self.gridLayout_30.addWidget(self.label_82, 1, 0, 1, 1)

        self.ledt_viajes_municipio = QLineEdit(self.frame_37)
        self.ledt_viajes_municipio.setObjectName(u"ledt_viajes_municipio")

        self.gridLayout_30.addWidget(self.ledt_viajes_municipio, 1, 1, 1, 1)

        self.label_83 = QLabel(self.frame_37)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setFont(font3)

        self.gridLayout_30.addWidget(self.label_83, 2, 0, 1, 1)

        self.ledt_viajes_colonia = QLineEdit(self.frame_37)
        self.ledt_viajes_colonia.setObjectName(u"ledt_viajes_colonia")

        self.gridLayout_30.addWidget(self.ledt_viajes_colonia, 2, 1, 1, 1)

        self.label_84 = QLabel(self.frame_37)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setFont(font3)

        self.gridLayout_30.addWidget(self.label_84, 3, 0, 1, 1)

        self.ledt_viajes_calle = QLineEdit(self.frame_37)
        self.ledt_viajes_calle.setObjectName(u"ledt_viajes_calle")

        self.gridLayout_30.addWidget(self.ledt_viajes_calle, 3, 1, 1, 1)

        self.label_85 = QLabel(self.frame_37)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setFont(font3)

        self.gridLayout_30.addWidget(self.label_85, 4, 0, 1, 1)

        self.ledt_viajes_cel = QLineEdit(self.frame_37)
        self.ledt_viajes_cel.setObjectName(u"ledt_viajes_cel")

        self.gridLayout_30.addWidget(self.ledt_viajes_cel, 4, 1, 1, 1)


        self.gridLayout_29.addWidget(self.frame_37, 0, 0, 1, 1)


        self.horizontalLayout_15.addWidget(self.frame_36)

        self.horizontalSpacer_34 = QSpacerItem(39, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_34)


        self.verticalLayout_8.addWidget(self.groupBox_6)


        self.verticalLayout_23.addWidget(self.frame_19)

        self.frame_2 = QFrame(self.pg_viaje)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font3)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.groupBox_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabla_viajes = QTableWidget(self.frame_6)
        if (self.tabla_viajes.columnCount() < 13):
            self.tabla_viajes.setColumnCount(13)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_viajes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_viajes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_viajes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_viajes.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_viajes.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_viajes.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_viajes.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_viajes.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_viajes.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_viajes.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabla_viajes.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_viajes.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabla_viajes.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        self.tabla_viajes.setObjectName(u"tabla_viajes")
        self.tabla_viajes.setMinimumSize(QSize(0, 239))
        self.tabla_viajes.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(60, 115, 120);\n"
"	color: rgb(255, 255, 255);\n"
"	font-size:10pt;\n"
"}")

        self.gridLayout_3.addWidget(self.tabla_viajes, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 40))
        self.groupBox_4.setStyleSheet(u"background-color: rgb(60, 100, 120);")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.label_14)

        self.cbx_buscar_viaje = QComboBox(self.groupBox_4)
        self.cbx_buscar_viaje.addItem("")
        self.cbx_buscar_viaje.addItem("")
        self.cbx_buscar_viaje.addItem("")
        self.cbx_buscar_viaje.addItem("")
        self.cbx_buscar_viaje.addItem("")
        self.cbx_buscar_viaje.addItem("")
        self.cbx_buscar_viaje.addItem("")
        self.cbx_buscar_viaje.addItem("")
        self.cbx_buscar_viaje.setObjectName(u"cbx_buscar_viaje")
        self.cbx_buscar_viaje.setMinimumSize(QSize(180, 0))
        self.cbx_buscar_viaje.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.horizontalLayout_5.addWidget(self.cbx_buscar_viaje)

        self.horizontalSpacer_4 = QSpacerItem(119, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.ledt_buscar_viaje = QLineEdit(self.groupBox_4)
        self.ledt_buscar_viaje.setObjectName(u"ledt_buscar_viaje")
        self.ledt_buscar_viaje.setMinimumSize(QSize(180, 0))
        self.ledt_buscar_viaje.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.ledt_buscar_viaje.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.ledt_buscar_viaje)

        self.horizontalSpacer_5 = QSpacerItem(119, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.btn_buscar_viaje = QPushButton(self.groupBox_4)
        self.btn_buscar_viaje.setObjectName(u"btn_buscar_viaje")
        self.btn_buscar_viaje.setMinimumSize(QSize(180, 20))
        self.btn_buscar_viaje.setLayoutDirection(Qt.LeftToRight)
        self.btn_buscar_viaje.setStyleSheet(u"QPushButton{\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"	\n"
"	background-color: rgb(240, 240, 240);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(205, 205, 205);\n"
"}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u"images/751381.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_buscar_viaje.setIcon(icon11)

        self.horizontalLayout_5.addWidget(self.btn_buscar_viaje)


        self.verticalLayout_5.addWidget(self.groupBox_4)


        self.gridLayout_2.addWidget(self.groupBox_3, 0, 0, 1, 1)


        self.verticalLayout_23.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.pg_viaje)
        self.pg_conductor = QWidget()
        self.pg_conductor.setObjectName(u"pg_conductor")
        self.verticalLayout_26 = QVBoxLayout(self.pg_conductor)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_7 = QFrame(self.pg_conductor)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 243))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.groupBox_7 = QGroupBox(self.frame_7)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMaximumSize(QSize(16777215, 156))
        self.groupBox_7.setFont(font1)
        self.groupBox_7.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(240, 240, 240, 255), stop:1 rgba(60, 115, 150, 255));\n"
"border-top-left-radius:30px;\n"
" border-bottom-right-radius:30px;\n"
"")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_25 = QLabel(self.groupBox_7)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(100, 100))
        self.label_25.setMaximumSize(QSize(100, 100))
        self.label_25.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_25.setPixmap(QPixmap(u"images/5283021.png"))
        self.label_25.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_25)

        self.label_4 = QLabel(self.groupBox_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(150, 0))
        self.label_4.setMaximumSize(QSize(81, 31))
        self.label_4.setFont(font2)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_4)

        self.horizontalSpacer_8 = QSpacerItem(607, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.label_26 = QLabel(self.groupBox_7)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setMinimumSize(QSize(90, 90))
        self.label_26.setMaximumSize(QSize(90, 90))
        self.label_26.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_26.setPixmap(QPixmap(u"images/6070696.png"))
        self.label_26.setScaledContents(True)
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_26)


        self.verticalLayout_9.addWidget(self.groupBox_7)

        self.groupBox_23 = QGroupBox(self.frame_7)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.groupBox_23.setMinimumSize(QSize(0, 0))
        self.groupBox_23.setMaximumSize(QSize(16777215, 85))
        self.groupBox_23.setFont(font3)
        self.groupBox_23.setStyleSheet(u"background-color: rgb(250, 250, 250);\n"
"border:none;")
        self.horizontalLayout_21 = QHBoxLayout(self.groupBox_23)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 6)
        self.label_34 = QLabel(self.groupBox_23)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(0, 0))
        self.label_34.setMaximumSize(QSize(900, 160))
        self.label_34.setStyleSheet(u"border-bottom-left-radius:50px;\n"
" border-top-right-radius:50px;\n"
"")

        self.horizontalLayout_21.addWidget(self.label_34)


        self.verticalLayout_9.addWidget(self.groupBox_23)


        self.verticalLayout_26.addWidget(self.frame_7)

        self.frame_21 = QFrame(self.pg_conductor)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 190))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_21)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_8 = QGroupBox(self.frame_21)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(0, 190))
        self.groupBox_8.setMaximumSize(QSize(16777215, 190))
        self.groupBox_8.setFont(font3)
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_26)

        self.frame_8 = QFrame(self.groupBox_8)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_8)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.frame_24 = QFrame(self.frame_8)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(315, 141))
        self.frame_24.setMaximumSize(QSize(301, 141))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_24)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_29 = QLabel(self.frame_24)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font3)

        self.gridLayout_15.addWidget(self.label_29, 0, 0, 1, 1)

        self.ledt_conductor_nombre = QLineEdit(self.frame_24)
        self.ledt_conductor_nombre.setObjectName(u"ledt_conductor_nombre")

        self.gridLayout_15.addWidget(self.ledt_conductor_nombre, 0, 1, 1, 1)

        self.label_31 = QLabel(self.frame_24)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font3)

        self.gridLayout_15.addWidget(self.label_31, 1, 0, 1, 1)

        self.ledt_conductor_numero = QLineEdit(self.frame_24)
        self.ledt_conductor_numero.setObjectName(u"ledt_conductor_numero")

        self.gridLayout_15.addWidget(self.ledt_conductor_numero, 1, 1, 1, 1)

        self.label_30 = QLabel(self.frame_24)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font3)

        self.gridLayout_15.addWidget(self.label_30, 2, 0, 1, 1)

        self.ledt_conductor_folio = QLineEdit(self.frame_24)
        self.ledt_conductor_folio.setObjectName(u"ledt_conductor_folio")

        self.gridLayout_15.addWidget(self.ledt_conductor_folio, 2, 1, 1, 1)

        self.label_27 = QLabel(self.frame_24)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)

        self.gridLayout_15.addWidget(self.label_27, 3, 0, 1, 1)

        self.ledt_conductor_matricula = QLineEdit(self.frame_24)
        self.ledt_conductor_matricula.setObjectName(u"ledt_conductor_matricula")

        self.gridLayout_15.addWidget(self.ledt_conductor_matricula, 3, 1, 1, 1)

        self.label_28 = QLabel(self.frame_24)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font3)

        self.gridLayout_15.addWidget(self.label_28, 4, 0, 1, 1)

        self.ledt_conductor_fecha = QLineEdit(self.frame_24)
        self.ledt_conductor_fecha.setObjectName(u"ledt_conductor_fecha")

        self.gridLayout_15.addWidget(self.ledt_conductor_fecha, 4, 1, 1, 1)


        self.gridLayout_12.addWidget(self.frame_24, 0, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.frame_8)

        self.frame_27 = QFrame(self.groupBox_8)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_27)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.verticalSpacer_2 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(25, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_11, 1, 0, 1, 1)

        self.btn_guardar_conductor = QPushButton(self.frame_27)
        self.btn_guardar_conductor.setObjectName(u"btn_guardar_conductor")
        self.btn_guardar_conductor.setMinimumSize(QSize(80, 25))
        self.btn_guardar_conductor.setStyleSheet(u"QPushButton{\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"	background-color: rgb(60, 115, 120);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 85, 120);\n"
"}")

        self.gridLayout_13.addWidget(self.btn_guardar_conductor, 1, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(25, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_10, 1, 2, 1, 1)


        self.horizontalLayout_9.addWidget(self.frame_27)

        self.frame_9 = QFrame(self.groupBox_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_9)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_26 = QFrame(self.frame_9)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(315, 141))
        self.frame_26.setMaximumSize(QSize(301, 141))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_26)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_36 = QLabel(self.frame_26)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font3)

        self.gridLayout_14.addWidget(self.label_36, 0, 0, 1, 1)

        self.ledt_conductor_calle = QLineEdit(self.frame_26)
        self.ledt_conductor_calle.setObjectName(u"ledt_conductor_calle")

        self.gridLayout_14.addWidget(self.ledt_conductor_calle, 2, 1, 1, 1)

        self.ledt_conductor_municipio = QLineEdit(self.frame_26)
        self.ledt_conductor_municipio.setObjectName(u"ledt_conductor_municipio")

        self.gridLayout_14.addWidget(self.ledt_conductor_municipio, 0, 1, 1, 1)

        self.label_32 = QLabel(self.frame_26)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font3)

        self.gridLayout_14.addWidget(self.label_32, 2, 0, 1, 1)

        self.ledt_conductor_colonia = QLineEdit(self.frame_26)
        self.ledt_conductor_colonia.setObjectName(u"ledt_conductor_colonia")

        self.gridLayout_14.addWidget(self.ledt_conductor_colonia, 1, 1, 1, 1)

        self.label_35 = QLabel(self.frame_26)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font3)

        self.gridLayout_14.addWidget(self.label_35, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_26, 0, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.frame_9)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_25)


        self.gridLayout.addWidget(self.groupBox_8, 0, 0, 1, 1)


        self.verticalLayout_26.addWidget(self.frame_21)

        self.frame_10 = QFrame(self.pg_conductor)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_10)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_9 = QGroupBox(self.frame_10)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setFont(font3)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.groupBox_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(9, 9, 9, 9)
        self.tabla_conductores = QTableWidget(self.frame_11)
        if (self.tabla_conductores.columnCount() < 9):
            self.tabla_conductores.setColumnCount(9)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabla_conductores.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabla_conductores.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabla_conductores.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabla_conductores.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabla_conductores.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tabla_conductores.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tabla_conductores.setHorizontalHeaderItem(6, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tabla_conductores.setHorizontalHeaderItem(7, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tabla_conductores.setHorizontalHeaderItem(8, __qtablewidgetitem21)
        self.tabla_conductores.setObjectName(u"tabla_conductores")
        self.tabla_conductores.setMinimumSize(QSize(0, 239))
        self.tabla_conductores.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(60, 115, 120);\n"
"	color: rgb(255, 255, 255);\n"
"	font-size:10pt;\n"
"}")

        self.gridLayout_5.addWidget(self.tabla_conductores, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_11)

        self.groupBox_10 = QGroupBox(self.groupBox_9)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMinimumSize(QSize(0, 40))
        self.groupBox_10.setStyleSheet(u"background-color: rgb(60, 100, 120);")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_37 = QLabel(self.groupBox_10)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font3)
        self.label_37.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.label_37)

        self.cbx_buscar_conductor = QComboBox(self.groupBox_10)
        self.cbx_buscar_conductor.addItem("")
        self.cbx_buscar_conductor.addItem("")
        self.cbx_buscar_conductor.addItem("")
        self.cbx_buscar_conductor.addItem("")
        self.cbx_buscar_conductor.addItem("")
        self.cbx_buscar_conductor.addItem("")
        self.cbx_buscar_conductor.setObjectName(u"cbx_buscar_conductor")
        self.cbx_buscar_conductor.setMinimumSize(QSize(180, 0))
        self.cbx_buscar_conductor.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.horizontalLayout_10.addWidget(self.cbx_buscar_conductor)

        self.horizontalSpacer_12 = QSpacerItem(119, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_12)

        self.ledt_buscar_conductor = QLineEdit(self.groupBox_10)
        self.ledt_buscar_conductor.setObjectName(u"ledt_buscar_conductor")
        self.ledt_buscar_conductor.setMinimumSize(QSize(180, 0))
        self.ledt_buscar_conductor.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.ledt_buscar_conductor.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.ledt_buscar_conductor)

        self.horizontalSpacer_13 = QSpacerItem(119, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_13)

        self.btn_buscar_conductor = QPushButton(self.groupBox_10)
        self.btn_buscar_conductor.setObjectName(u"btn_buscar_conductor")
        self.btn_buscar_conductor.setMinimumSize(QSize(180, 20))
        self.btn_buscar_conductor.setLayoutDirection(Qt.LeftToRight)
        self.btn_buscar_conductor.setStyleSheet(u"QPushButton{\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"	\n"
"	background-color: rgb(240, 240, 240);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(205, 205, 205);\n"
"}\n"
"")
        self.btn_buscar_conductor.setIcon(icon11)

        self.horizontalLayout_10.addWidget(self.btn_buscar_conductor)


        self.verticalLayout_7.addWidget(self.groupBox_10)


        self.gridLayout_4.addWidget(self.groupBox_9, 0, 0, 1, 1)


        self.verticalLayout_26.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.pg_conductor)
        self.pg_historico = QWidget()
        self.pg_historico.setObjectName(u"pg_historico")
        self.verticalLayout_12 = QVBoxLayout(self.pg_historico)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_14 = QFrame(self.pg_historico)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 156))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_14)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.groupBox_13 = QGroupBox(self.frame_14)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setMaximumSize(QSize(16777215, 156))
        self.groupBox_13.setFont(font1)
        self.groupBox_13.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(240, 240, 240, 255), stop:1 rgba(60, 115, 150, 255));\n"
"border-top-left-radius:30px;\n"
" border-bottom-right-radius:30px;\n"
"")
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_39 = QLabel(self.groupBox_13)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(100, 100))
        self.label_39.setMaximumSize(QSize(100, 100))
        self.label_39.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_39.setPixmap(QPixmap(u"images/5234393.png"))
        self.label_39.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.label_39)

        self.label_5 = QLabel(self.groupBox_13)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(150, 0))
        self.label_5.setMaximumSize(QSize(81, 31))
        self.label_5.setFont(font2)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_5)

        self.horizontalSpacer_16 = QSpacerItem(607, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_16)

        self.label_40 = QLabel(self.groupBox_13)
        self.label_40.setObjectName(u"label_40")
        sizePolicy.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy)
        self.label_40.setMinimumSize(QSize(90, 90))
        self.label_40.setMaximumSize(QSize(90, 90))
        self.label_40.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_40.setPixmap(QPixmap(u"images/5234473.png"))
        self.label_40.setScaledContents(True)
        self.label_40.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_40)


        self.verticalLayout_11.addWidget(self.groupBox_13)


        self.verticalLayout_12.addWidget(self.frame_14)

        self.frame_12 = QFrame(self.pg_historico)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 90))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_12)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.groupBox_24 = QGroupBox(self.frame_12)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.groupBox_24.setMinimumSize(QSize(0, 0))
        self.groupBox_24.setMaximumSize(QSize(16777215, 90))
        self.groupBox_24.setFont(font3)
        self.groupBox_24.setStyleSheet(u"background-color: rgb(250, 250, 250);\n"
"border:none;")
        self.horizontalLayout_22 = QHBoxLayout(self.groupBox_24)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 6)
        self.label_41 = QLabel(self.groupBox_24)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(0, 0))
        self.label_41.setMaximumSize(QSize(900, 90))
        self.label_41.setStyleSheet(u"border-bottom-left-radius:50px;\n"
" border-top-right-radius:50px;\n"
"")

        self.horizontalLayout_22.addWidget(self.label_41)


        self.gridLayout_6.addWidget(self.groupBox_24, 0, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.pg_historico)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_13)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.groupBox_11 = QGroupBox(self.frame_13)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setFont(font3)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_28 = QFrame(self.groupBox_11)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_28)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tabla_historico = QTableWidget(self.frame_28)
        if (self.tabla_historico.columnCount() < 11):
            self.tabla_historico.setColumnCount(11)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tabla_historico.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tabla_historico.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tabla_historico.setHorizontalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tabla_historico.setHorizontalHeaderItem(3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tabla_historico.setHorizontalHeaderItem(4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tabla_historico.setHorizontalHeaderItem(5, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tabla_historico.setHorizontalHeaderItem(6, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tabla_historico.setHorizontalHeaderItem(7, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tabla_historico.setHorizontalHeaderItem(8, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tabla_historico.setHorizontalHeaderItem(9, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tabla_historico.setHorizontalHeaderItem(10, __qtablewidgetitem32)
        self.tabla_historico.setObjectName(u"tabla_historico")
        self.tabla_historico.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(60, 115, 120);\n"
"	color: rgb(255, 255, 255);\n"
"	font-size:10pt;\n"
"}")

        self.gridLayout_7.addWidget(self.tabla_historico, 0, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_28)

        self.groupBox_12 = QGroupBox(self.groupBox_11)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setMinimumSize(QSize(0, 40))
        self.groupBox_12.setStyleSheet(u"background-color: rgb(60, 100, 120);")
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_38 = QLabel(self.groupBox_12)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font3)
        self.label_38.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.label_38)

        self.cbx_buscar_historico = QComboBox(self.groupBox_12)
        self.cbx_buscar_historico.addItem("")
        self.cbx_buscar_historico.addItem("")
        self.cbx_buscar_historico.setObjectName(u"cbx_buscar_historico")
        self.cbx_buscar_historico.setMinimumSize(QSize(180, 0))
        self.cbx_buscar_historico.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.cbx_buscar_historico.setFrame(False)

        self.horizontalLayout_11.addWidget(self.cbx_buscar_historico)

        self.horizontalSpacer_14 = QSpacerItem(119, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_14)

        self.ledt_buscar_historico = QLineEdit(self.groupBox_12)
        self.ledt_buscar_historico.setObjectName(u"ledt_buscar_historico")
        self.ledt_buscar_historico.setMinimumSize(QSize(180, 0))
        self.ledt_buscar_historico.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.ledt_buscar_historico.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.ledt_buscar_historico)

        self.horizontalSpacer_15 = QSpacerItem(119, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_15)

        self.btn_buscar_historico = QPushButton(self.groupBox_12)
        self.btn_buscar_historico.setObjectName(u"btn_buscar_historico")
        self.btn_buscar_historico.setMinimumSize(QSize(180, 20))
        self.btn_buscar_historico.setLayoutDirection(Qt.LeftToRight)
        self.btn_buscar_historico.setStyleSheet(u"QPushButton{\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"	\n"
"	background-color: rgb(240, 240, 240);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(205, 205, 205);\n"
"}\n"
"")
        self.btn_buscar_historico.setIcon(icon11)

        self.horizontalLayout_11.addWidget(self.btn_buscar_historico)


        self.verticalLayout_10.addWidget(self.groupBox_12)


        self.gridLayout_16.addWidget(self.groupBox_11, 0, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.frame_13)

        self.stackedWidget.addWidget(self.pg_historico)
        self.pg_factura = QWidget()
        self.pg_factura.setObjectName(u"pg_factura")
        self.verticalLayout_15 = QVBoxLayout(self.pg_factura)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_17 = QFrame(self.pg_factura)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 156))
        self.frame_17.setMaximumSize(QSize(16777215, 156))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_17)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.groupBox_15 = QGroupBox(self.frame_17)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setMaximumSize(QSize(16777215, 156))
        self.groupBox_15.setFont(font1)
        self.groupBox_15.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(240, 240, 240, 255), stop:1 rgba(60, 115, 150, 255));\n"
"border-top-left-radius:30px;\n"
" border-bottom-right-radius:30px;\n"
"")
        self.horizontalLayout_14 = QHBoxLayout(self.groupBox_15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_51 = QLabel(self.groupBox_15)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(100, 100))
        self.label_51.setMaximumSize(QSize(100, 100))
        self.label_51.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_51.setPixmap(QPixmap(u"images/7385193.png"))
        self.label_51.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.label_51)

        self.label_6 = QLabel(self.groupBox_15)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(150, 0))
        self.label_6.setMaximumSize(QSize(81, 31))
        self.label_6.setFont(font2)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_6)

        self.horizontalSpacer_19 = QSpacerItem(607, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_19)

        self.label_52 = QLabel(self.groupBox_15)
        self.label_52.setObjectName(u"label_52")
        sizePolicy.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy)
        self.label_52.setMinimumSize(QSize(90, 90))
        self.label_52.setMaximumSize(QSize(90, 90))
        self.label_52.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_52.setPixmap(QPixmap(u"images/3997635.png"))
        self.label_52.setScaledContents(True)
        self.label_52.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_52)


        self.verticalLayout_13.addWidget(self.groupBox_15)


        self.verticalLayout_15.addWidget(self.frame_17)

        self.frame_29 = QFrame(self.pg_factura)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(16777215, 90))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_29)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.groupBox_25 = QGroupBox(self.frame_29)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.groupBox_25.setMinimumSize(QSize(0, 0))
        self.groupBox_25.setMaximumSize(QSize(16777215, 90))
        self.groupBox_25.setFont(font3)
        self.groupBox_25.setStyleSheet(u"background-color: rgb(250, 250, 250);\n"
"border:none;")
        self.horizontalLayout_23 = QHBoxLayout(self.groupBox_25)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 6)
        self.label_42 = QLabel(self.groupBox_25)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(0, 0))
        self.label_42.setMaximumSize(QSize(900, 90))
        self.label_42.setStyleSheet(u"border-bottom-left-radius:50px;\n"
" border-top-right-radius:50px;\n"
"")

        self.horizontalLayout_23.addWidget(self.label_42)


        self.gridLayout_8.addWidget(self.groupBox_25, 0, 0, 1, 1)


        self.verticalLayout_15.addWidget(self.frame_29)

        self.frame_20 = QFrame(self.pg_factura)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_20)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setHorizontalSpacing(0)
        self.gridLayout_17.setContentsMargins(0, 0, 0, -1)
        self.groupBox_17 = QGroupBox(self.frame_20)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setFont(font3)
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_17)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_3 = QFrame(self.groupBox_17)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 43))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(293, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.dateEdit_2 = QDateEdit(self.frame_3)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setFont(font3)
        self.dateEdit_2.setWrapping(False)
        self.dateEdit_2.setFrame(False)
        self.dateEdit_2.setAlignment(Qt.AlignCenter)
        self.dateEdit_2.setReadOnly(True)
        self.dateEdit_2.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.horizontalLayout_4.addWidget(self.dateEdit_2)

        self.horizontalSpacer_3 = QSpacerItem(293, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_14.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.groupBox_17)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_4)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSpacer_4 = QSpacerItem(20, 465, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_4)

        self.btn_generar_factura = QPushButton(self.frame_4)
        self.btn_generar_factura.setObjectName(u"btn_generar_factura")
        self.btn_generar_factura.setStyleSheet(u"QPushButton{\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"	background-color: rgb(60, 115, 120);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 85, 120);\n"
"}")

        self.verticalLayout_19.addWidget(self.btn_generar_factura)


        self.verticalLayout_14.addWidget(self.frame_4)


        self.gridLayout_17.addWidget(self.groupBox_17, 0, 0, 1, 1)


        self.verticalLayout_15.addWidget(self.frame_20)

        self.stackedWidget.addWidget(self.pg_factura)
        self.pg_ajustes = QWidget()
        self.pg_ajustes.setObjectName(u"pg_ajustes")
        self.verticalLayout_18 = QVBoxLayout(self.pg_ajustes)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_22 = QFrame(self.pg_ajustes)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(16777215, 350))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_22)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.groupBox_19 = QGroupBox(self.frame_22)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setMaximumSize(QSize(16777215, 156))
        self.groupBox_19.setFont(font1)
        self.groupBox_19.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(240, 240, 240, 255), stop:1 rgba(60, 115, 150, 255));\n"
"border-top-left-radius:30px;\n"
" border-bottom-right-radius:30px;\n"
"")
        self.horizontalLayout_17 = QHBoxLayout(self.groupBox_19)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_64 = QLabel(self.groupBox_19)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(100, 100))
        self.label_64.setMaximumSize(QSize(100, 100))
        self.label_64.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_64.setPixmap(QPixmap(u"images/1522158.png"))
        self.label_64.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_64)

        self.label_8 = QLabel(self.groupBox_19)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(150, 0))
        self.label_8.setMaximumSize(QSize(81, 31))
        self.label_8.setFont(font2)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_8)

        self.horizontalSpacer_24 = QSpacerItem(607, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_24)

        self.label_65 = QLabel(self.groupBox_19)
        self.label_65.setObjectName(u"label_65")
        sizePolicy.setHeightForWidth(self.label_65.sizePolicy().hasHeightForWidth())
        self.label_65.setSizePolicy(sizePolicy)
        self.label_65.setMinimumSize(QSize(90, 90))
        self.label_65.setMaximumSize(QSize(90, 90))
        self.label_65.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_65.setPixmap(QPixmap(u"images/1835942.png"))
        self.label_65.setScaledContents(True)
        self.label_65.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_65)


        self.verticalLayout_16.addWidget(self.groupBox_19)

        self.groupBox_20 = QGroupBox(self.frame_22)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setMaximumSize(QSize(16777215, 190))
        self.groupBox_20.setFont(font3)
        self.horizontalLayout_13 = QHBoxLayout(self.groupBox_20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.groupBox = QGroupBox(self.groupBox_20)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_21 = QGridLayout(self.groupBox)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.frame_15 = QFrame(self.groupBox)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_15)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.dateTimeEdit = QDateTimeEdit(self.frame_15)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setFrame(False)
        self.dateTimeEdit.setAlignment(Qt.AlignCenter)
        self.dateTimeEdit.setReadOnly(True)
        self.dateTimeEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.verticalLayout_20.addWidget(self.dateTimeEdit)

        self.checkBox = QCheckBox(self.frame_15)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setLayoutDirection(Qt.LeftToRight)
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setChecked(True)

        self.verticalLayout_20.addWidget(self.checkBox)

        self.ajustes_fecha_label = QLabel(self.frame_15)
        self.ajustes_fecha_label.setObjectName(u"ajustes_fecha_label")
        self.ajustes_fecha_label.setStyleSheet(u"color: rgb(185, 185, 185);")
        self.ajustes_fecha_label.setFrameShape(QFrame.NoFrame)
        self.ajustes_fecha_label.setFrameShadow(QFrame.Sunken)
        self.ajustes_fecha_label.setTextFormat(Qt.AutoText)
        self.ajustes_fecha_label.setScaledContents(False)
        self.ajustes_fecha_label.setAlignment(Qt.AlignCenter)
        self.ajustes_fecha_label.setWordWrap(False)
        self.ajustes_fecha_label.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_20.addWidget(self.ajustes_fecha_label)

        self.ajustes_fecha_TimeEdit = QDateTimeEdit(self.frame_15)
        self.ajustes_fecha_TimeEdit.setObjectName(u"ajustes_fecha_TimeEdit")
        self.ajustes_fecha_TimeEdit.setMinimumSize(QSize(0, 18))
        self.ajustes_fecha_TimeEdit.setStyleSheet(u"color: rgb(185, 185, 185);")
        self.ajustes_fecha_TimeEdit.setWrapping(False)
        self.ajustes_fecha_TimeEdit.setFrame(True)
        self.ajustes_fecha_TimeEdit.setAlignment(Qt.AlignCenter)
        self.ajustes_fecha_TimeEdit.setReadOnly(True)
        self.ajustes_fecha_TimeEdit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.ajustes_fecha_TimeEdit.setKeyboardTracking(True)
        self.ajustes_fecha_TimeEdit.setProperty("showGroupSeparator", False)
        self.ajustes_fecha_TimeEdit.setCalendarPopup(True)

        self.verticalLayout_20.addWidget(self.ajustes_fecha_TimeEdit)

        self.btn_actualizar_fecha = QPushButton(self.frame_15)
        self.btn_actualizar_fecha.setObjectName(u"btn_actualizar_fecha")
        self.btn_actualizar_fecha.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	background-color: rgb(245, 245, 245);\n"
"	\n"
"	color: rgb(185, 185, 185);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(245, 245, 245);\n"
"}")
        self.btn_actualizar_fecha.setCheckable(False)
        self.btn_actualizar_fecha.setChecked(False)
        self.btn_actualizar_fecha.setFlat(False)

        self.verticalLayout_20.addWidget(self.btn_actualizar_fecha)


        self.gridLayout_21.addWidget(self.frame_15, 0, 0, 1, 1)


        self.horizontalLayout_13.addWidget(self.groupBox)

        self.groupBox_14 = QGroupBox(self.groupBox_20)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setMaximumSize(QSize(400, 16777215))
        self.gridLayout_9 = QGridLayout(self.groupBox_14)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_16 = QFrame(self.groupBox_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_16)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_15 = QLabel(self.frame_16)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_15)

        self.ledt_costo = QLineEdit(self.frame_16)
        self.ledt_costo.setObjectName(u"ledt_costo")
        self.ledt_costo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.ledt_costo)

        self.btn_actualizar_costo = QPushButton(self.frame_16)
        self.btn_actualizar_costo.setObjectName(u"btn_actualizar_costo")
        self.btn_actualizar_costo.setStyleSheet(u"QPushButton{\n"
"		border:none;\n"
"        color: rgb(255, 255, 255);\n"
"        background-color:  rgb(60, 115, 120);\n"
"}\n"
"QPushButton:hover{\n"
"	 background-color: rgb(0, 85, 120);\n"
"}\n"
"")
        self.btn_actualizar_costo.setCheckable(False)
        self.btn_actualizar_costo.setChecked(False)
        self.btn_actualizar_costo.setFlat(False)

        self.verticalLayout_27.addWidget(self.btn_actualizar_costo)


        self.gridLayout_9.addWidget(self.frame_16, 0, 0, 1, 1)


        self.horizontalLayout_13.addWidget(self.groupBox_14)


        self.verticalLayout_16.addWidget(self.groupBox_20)


        self.verticalLayout_18.addWidget(self.frame_22)

        self.frame_25 = QFrame(self.pg_ajustes)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_25)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_18.addWidget(self.frame_25)

        self.stackedWidget.addWidget(self.pg_ajustes)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_contenedor)


        self.verticalLayout.addWidget(self.frame_inferior)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btn_inicio.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)
        self.btn_actualizar_fecha.setDefault(False)
        self.btn_actualizar_costo.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u"   MENU", None))
        self.btn_minimizar.setText("")
        self.btn_restaurar.setText("")
        self.btn_maximizar.setText("")
        self.btn_cerrar.setText("")
        self.btn_viajes.setText(QCoreApplication.translate("MainWindow", u"   Viaje", None))
        self.btn_conductor.setText(QCoreApplication.translate("MainWindow", u"  Conductor", None))
        self.btn_historico.setText(QCoreApplication.translate("MainWindow", u"  Historico", None))
        self.btn_factura.setText(QCoreApplication.translate("MainWindow", u"  Factura", None))
        self.btn_ajustes.setText(QCoreApplication.translate("MainWindow", u"  Ajustes", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Universidad de Guadalajara", None))
        self.groupBox_5.setTitle("")
        self.label_10.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"INICIO", None))
        self.label_13.setText("")
        self.groupBox_22.setTitle("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Bienvenido!</p><p align=\"center\">Estamos para servirte</p></body></html>", None))
        self.groupBox_18.setTitle("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Fecha actual", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Semana en curso", None))
        self.ledt_numero_semana.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"Resumen", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Ultima modificacion:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Semana en curso:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Semana previa:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Total de ingresos semana previa:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Total de gastos semana previa:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Ganancia:", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"$ 0.0", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"$ 0.0", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"$ 0.0", None))
        self.groupBox_2.setTitle("")
        self.label_9.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"VIAJE", None))
        self.label_12.setText("")
        self.groupBox_21.setTitle("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Registra un nuevo viaje en el apartado &quot;Registro&quot; y presiona guardar para crear un nuevo registro.<br/>Dirigete al apartado &quot;Consulta&quot; para verificar los viajes de esta semana, puedes buscar un viaje<br/>espec\u00edfico en el apartado &quot;Buscar por&quot;.<br/>Para modificar o eliminar un registro, presiona dicho bot\u00f3n en el el registro espec\u00edfico.</p></body></html>", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Registro", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Folio:", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Conductor:", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Empresa:", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Matr\u00edcula:", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Tipo servicio:", None))
        self.btn_guardar_viaje.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Contacto:", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Municipio:", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Colonia:", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Calle:", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Cel. Contacto", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Consulta", None))
        ___qtablewidgetitem = self.tabla_viajes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Folio", None));
        ___qtablewidgetitem1 = self.tabla_viajes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem2 = self.tabla_viajes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Conductor", None));
        ___qtablewidgetitem3 = self.tabla_viajes.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Empresa", None));
        ___qtablewidgetitem4 = self.tabla_viajes.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Matricula", None));
        ___qtablewidgetitem5 = self.tabla_viajes.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Tipo Servicio", None));
        ___qtablewidgetitem6 = self.tabla_viajes.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Contacto", None));
        ___qtablewidgetitem7 = self.tabla_viajes.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Municipio", None));
        ___qtablewidgetitem8 = self.tabla_viajes.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Colonia", None));
        ___qtablewidgetitem9 = self.tabla_viajes.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Calle", None));
        ___qtablewidgetitem10 = self.tabla_viajes.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Cel. Contacto", None));
        ___qtablewidgetitem11 = self.tabla_viajes.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Modificar", None));
        ___qtablewidgetitem12 = self.tabla_viajes.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None));
        self.groupBox_4.setTitle("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Buscar por:", None))
        self.cbx_buscar_viaje.setItemText(0, QCoreApplication.translate("MainWindow", u"Folio", None))
        self.cbx_buscar_viaje.setItemText(1, QCoreApplication.translate("MainWindow", u"Conductor", None))
        self.cbx_buscar_viaje.setItemText(2, QCoreApplication.translate("MainWindow", u"Empresa", None))
        self.cbx_buscar_viaje.setItemText(3, QCoreApplication.translate("MainWindow", u"Matricula", None))
        self.cbx_buscar_viaje.setItemText(4, QCoreApplication.translate("MainWindow", u"Tipo de servicio", None))
        self.cbx_buscar_viaje.setItemText(5, QCoreApplication.translate("MainWindow", u"Municipio", None))
        self.cbx_buscar_viaje.setItemText(6, QCoreApplication.translate("MainWindow", u"Colonia", None))
        self.cbx_buscar_viaje.setItemText(7, QCoreApplication.translate("MainWindow", u"Contacto", None))

        self.ledt_buscar_viaje.setPlaceholderText(QCoreApplication.translate("MainWindow", u"000000000", None))
        self.btn_buscar_viaje.setText(QCoreApplication.translate("MainWindow", u"   Buscar", None))
        self.groupBox_7.setTitle("")
        self.label_25.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CONDUCTOR", None))
        self.label_26.setText("")
        self.groupBox_23.setTitle("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Registra un nuevo conductor en el apartado &quot;Registro&quot; y presiona guardar para crear un nuevo registro.<br/>Dirigete al apartado &quot;Consulta&quot; para verificar los conductores existentes, puedes buscar uno espec\u00edfico<br/>en el apartado &quot;Buscar por&quot;.<br/>Para modificar o eliminar un registro, presiona dicho bot\u00f3n en el el registro espec\u00edfico.</p></body></html>", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Registro", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"N\u00famero:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Folio identificaci\u00f3n:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Matr\u00edcula:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Fecha de contrataci\u00f3n:", None))
        self.btn_guardar_conductor.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Municipio:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Calle:", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Colonia:", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Consulta", None))
        ___qtablewidgetitem13 = self.tabla_conductores.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"No.", None));
        ___qtablewidgetitem14 = self.tabla_conductores.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem15 = self.tabla_conductores.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Numero", None));
        ___qtablewidgetitem16 = self.tabla_conductores.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Folio", None));
        ___qtablewidgetitem17 = self.tabla_conductores.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Matricula", None));
        ___qtablewidgetitem18 = self.tabla_conductores.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem19 = self.tabla_conductores.horizontalHeaderItem(6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Municipio", None));
        ___qtablewidgetitem20 = self.tabla_conductores.horizontalHeaderItem(7)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Colonia", None));
        ___qtablewidgetitem21 = self.tabla_conductores.horizontalHeaderItem(8)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Calle", None));
        self.groupBox_10.setTitle("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Buscar por:", None))
        self.cbx_buscar_conductor.setItemText(0, QCoreApplication.translate("MainWindow", u"Matricula", None))
        self.cbx_buscar_conductor.setItemText(1, QCoreApplication.translate("MainWindow", u"No.", None))
        self.cbx_buscar_conductor.setItemText(2, QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.cbx_buscar_conductor.setItemText(3, QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.cbx_buscar_conductor.setItemText(4, QCoreApplication.translate("MainWindow", u"Municipio", None))
        self.cbx_buscar_conductor.setItemText(5, QCoreApplication.translate("MainWindow", u"Colonia", None))

        self.ledt_buscar_conductor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A0000000", None))
        self.btn_buscar_conductor.setText(QCoreApplication.translate("MainWindow", u"   Buscar", None))
        self.groupBox_13.setTitle("")
        self.label_39.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"HISTORICO", None))
        self.label_40.setText("")
        self.groupBox_24.setTitle("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">En esta secci\u00f3n, usted puede revisar el registro hist\u00f3rico de viajes.<br/>Se pueden buscar viajes espec\u00edficos en el apartado &quot;Buscar por&quot;.<br/>En este apartado solo se puede visualizar la informaci\u00f3n.</p></body></html>", None))
        self.groupBox_11.setTitle("")
        ___qtablewidgetitem22 = self.tabla_historico.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Folio", None));
        ___qtablewidgetitem23 = self.tabla_historico.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem24 = self.tabla_historico.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Conductor", None));
        ___qtablewidgetitem25 = self.tabla_historico.horizontalHeaderItem(3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Empresa", None));
        ___qtablewidgetitem26 = self.tabla_historico.horizontalHeaderItem(4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Matricula", None));
        ___qtablewidgetitem27 = self.tabla_historico.horizontalHeaderItem(5)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Tipo Servicio", None));
        ___qtablewidgetitem28 = self.tabla_historico.horizontalHeaderItem(6)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Contacto", None));
        ___qtablewidgetitem29 = self.tabla_historico.horizontalHeaderItem(7)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Municipio", None));
        ___qtablewidgetitem30 = self.tabla_historico.horizontalHeaderItem(8)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Colonia", None));
        ___qtablewidgetitem31 = self.tabla_historico.horizontalHeaderItem(9)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Calle", None));
        ___qtablewidgetitem32 = self.tabla_historico.horizontalHeaderItem(10)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Cel. Contacto", None));
        self.groupBox_12.setTitle("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Buscar por:", None))
        self.cbx_buscar_historico.setItemText(0, QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.cbx_buscar_historico.setItemText(1, QCoreApplication.translate("MainWindow", u"No. Semana", None))

        self.btn_buscar_historico.setText(QCoreApplication.translate("MainWindow", u"   Buscar", None))
        self.groupBox_15.setTitle("")
        self.label_51.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"FACTURA", None))
        self.label_52.setText("")
        self.groupBox_25.setTitle("")
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">En esta secci\u00f3n, usted puede revisar el registro hist\u00f3rico de viajes.<br/>Se pueden buscar viajes espec\u00edficos en el apartado &quot;Buscar por&quot;.<br/>En este apartado solo se puede visualizar la informaci\u00f3n.</p></body></html>", None))
        self.groupBox_17.setTitle("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Factura a d\u00eda de: ", None))
        self.btn_generar_factura.setText(QCoreApplication.translate("MainWindow", u"Generar", None))
        self.groupBox_19.setTitle("")
        self.label_64.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"AJUSTES", None))
        self.label_65.setText("")
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"Ajustes", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Hora y fecha", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"                Establecer fecha automaticamente", None))
        self.ajustes_fecha_label.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.btn_actualizar_fecha.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Otros", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Costo por kilometro", None))
        self.btn_actualizar_costo.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
    # retranslateUi

