# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'headsetting.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_headsetting(object):
    def setupUi(self, headsetting):
        if not headsetting.objectName():
            headsetting.setObjectName(u"headsetting")
        headsetting.resize(800, 600)
        headsetting.setStyleSheet(u"*{\n"
"	padding:6px;\n"
"	background-color:rgb(0,0,90);\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QPushButton{\n"
"margin:8px;padding:15px;\n"
"}\n"
"QComboBox{\n"
"	background-color:rgb(255,255,255);\n"
"	color:rgb(0,0,0);\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(headsetting)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(headsetting)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(9)
        self.srb11 = QComboBox(self.groupBox)
        self.srb11.addItem("")
        self.srb11.setObjectName(u"srb11")
        self.srb11.setMaximumSize(QSize(100, 35))
        self.srb11.setStyleSheet(u"background-color:rgb(255, 205, 201)")

        self.gridLayout.addWidget(self.srb11, 1, 5, 1, 1)

        self.pga1 = QComboBox(self.groupBox)
        self.pga1.addItem("")
        self.pga1.setObjectName(u"pga1")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pga1.sizePolicy().hasHeightForWidth())
        self.pga1.setSizePolicy(sizePolicy)
        self.pga1.setMinimumSize(QSize(100, 35))

        self.gridLayout.addWidget(self.pga1, 1, 1, 1, 1)

        self.input1 = QComboBox(self.groupBox)
        self.input1.addItem("")
        self.input1.setObjectName(u"input1")
        self.input1.setMinimumSize(QSize(100, 35))
        self.input1.setMaximumSize(QSize(100, 35))

        self.gridLayout.addWidget(self.input1, 1, 2, 1, 1)

        self.bias2 = QComboBox(self.groupBox)
        self.bias2.addItem("")
        self.bias2.setObjectName(u"bias2")
        self.bias2.setMaximumSize(QSize(100, 35))
        self.bias2.setStyleSheet(u"background-color:rgb(159, 255, 142);")

        self.gridLayout.addWidget(self.bias2, 2, 3, 1, 1)

        self.bias1 = QComboBox(self.groupBox)
        self.bias1.addItem("")
        self.bias1.setObjectName(u"bias1")
        self.bias1.setMaximumSize(QSize(100, 35))
        self.bias1.setStyleSheet(u"background-color:rgb(159, 255, 142);")

        self.gridLayout.addWidget(self.bias1, 1, 3, 1, 1)

        self.label_20 = QLabel(self.groupBox)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(36, 36))
        self.label_20.setStyleSheet(u"border:1px solid;\n"
"border-radius:16px;\n"
"background-color:rgb(0,0,150);")

        self.gridLayout.addWidget(self.label_20, 7, 0, 1, 1, Qt.AlignHCenter)

        self.srb22 = QComboBox(self.groupBox)
        self.srb22.addItem("")
        self.srb22.setObjectName(u"srb22")
        self.srb22.setMaximumSize(QSize(100, 35))
        self.srb22.setStyleSheet(u"background-color:rgb(159, 255, 142);")

        self.gridLayout.addWidget(self.srb22, 2, 4, 1, 1)

        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(36, 36))
        self.label_18.setStyleSheet(u"border:1px solid;\n"
"border-radius:16px;\n"
"background-color:rgb(0,0,150);")

        self.gridLayout.addWidget(self.label_18, 5, 0, 1, 1, Qt.AlignHCenter)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(36, 36))
        self.label_15.setStyleSheet(u"border:1px solid;\n"
"border-radius:16px;\n"
"background-color:rgb(0,120,90);")

        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1, Qt.AlignHCenter)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(36, 36))

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1, Qt.AlignHCenter)

        self.srb12 = QComboBox(self.groupBox)
        self.srb12.addItem("")
        self.srb12.setObjectName(u"srb12")
        self.srb12.setMaximumSize(QSize(100, 35))
        self.srb12.setStyleSheet(u"background-color:rgb(255, 205, 201)")

        self.gridLayout.addWidget(self.srb12, 2, 5, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1, Qt.AlignHCenter)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(36, 36))
        self.label_14.setStyleSheet(u"border:1px solid;\n"
"border-radius:16px;\n"
"background-color:rgb(240,0,0);")

        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1, Qt.AlignHCenter)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1, Qt.AlignHCenter)

        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(36, 36))
        self.label_19.setStyleSheet(u"border:1px solid;\n"
"border-radius:16px;\n"
"background-color:rgb(0,0,150);")

        self.gridLayout.addWidget(self.label_19, 6, 0, 1, 1, Qt.AlignHCenter)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1, Qt.AlignHCenter)

        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(36, 36))
        self.label_17.setStyleSheet(u"border:1px solid;\n"
"border-radius:16px;\n"
"background-color:rgb(0,0,150);")

        self.gridLayout.addWidget(self.label_17, 4, 0, 1, 1, Qt.AlignHCenter)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 5, 1, 1, Qt.AlignHCenter)

        self.input2 = QComboBox(self.groupBox)
        self.input2.addItem("")
        self.input2.setObjectName(u"input2")
        self.input2.setMinimumSize(QSize(100, 35))
        self.input2.setMaximumSize(QSize(100, 35))

        self.gridLayout.addWidget(self.input2, 2, 2, 1, 1)

        self.pga2 = QComboBox(self.groupBox)
        self.pga2.addItem("")
        self.pga2.setObjectName(u"pga2")
        self.pga2.setMinimumSize(QSize(100, 35))

        self.gridLayout.addWidget(self.pga2, 2, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(36, 36))
        self.label_16.setStyleSheet(u"border:1px solid;\n"
"border-radius:16px;\n"
"background-color:rgb(250,120,0);")

        self.gridLayout.addWidget(self.label_16, 3, 0, 1, 1, Qt.AlignHCenter)

        self.srb21 = QComboBox(self.groupBox)
        self.srb21.addItem("")
        self.srb21.setObjectName(u"srb21")
        self.srb21.setMaximumSize(QSize(100, 35))
        self.srb21.setStyleSheet(u"background-color:rgb(159, 255, 142);")

        self.gridLayout.addWidget(self.srb21, 1, 4, 1, 1)

        self.label_21 = QLabel(self.groupBox)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(36, 36))
        self.label_21.setStyleSheet(u"border:1px solid;\n"
"border-radius:16px;\n"
"background-color:rgb(0,0,150);")

        self.gridLayout.addWidget(self.label_21, 8, 0, 1, 1, Qt.AlignHCenter)

        self.pga3 = QComboBox(self.groupBox)
        self.pga3.addItem("")
        self.pga3.setObjectName(u"pga3")
        self.pga3.setMinimumSize(QSize(100, 35))

        self.gridLayout.addWidget(self.pga3, 3, 1, 1, 1)

        self.pga4 = QComboBox(self.groupBox)
        self.pga4.addItem("")
        self.pga4.setObjectName(u"pga4")
        self.pga4.setMinimumSize(QSize(100, 35))

        self.gridLayout.addWidget(self.pga4, 4, 1, 1, 1)

        self.pga5 = QComboBox(self.groupBox)
        self.pga5.addItem("")
        self.pga5.setObjectName(u"pga5")
        self.pga5.setMinimumSize(QSize(100, 35))

        self.gridLayout.addWidget(self.pga5, 5, 1, 1, 1)

        self.pga6 = QComboBox(self.groupBox)
        self.pga6.addItem("")
        self.pga6.setObjectName(u"pga6")
        self.pga6.setMinimumSize(QSize(100, 35))

        self.gridLayout.addWidget(self.pga6, 6, 1, 1, 1)

        self.pga7 = QComboBox(self.groupBox)
        self.pga7.addItem("")
        self.pga7.setObjectName(u"pga7")
        self.pga7.setMinimumSize(QSize(100, 35))

        self.gridLayout.addWidget(self.pga7, 7, 1, 1, 1)

        self.pga8 = QComboBox(self.groupBox)
        self.pga8.addItem("")
        self.pga8.setObjectName(u"pga8")
        self.pga8.setMinimumSize(QSize(100, 35))

        self.gridLayout.addWidget(self.pga8, 8, 1, 1, 1)

        self.input3 = QComboBox(self.groupBox)
        self.input3.addItem("")
        self.input3.setObjectName(u"input3")
        self.input3.setMinimumSize(QSize(100, 35))
        self.input3.setMaximumSize(QSize(100, 35))

        self.gridLayout.addWidget(self.input3, 3, 2, 1, 1)

        self.input4 = QComboBox(self.groupBox)
        self.input4.addItem("")
        self.input4.setObjectName(u"input4")
        self.input4.setMinimumSize(QSize(100, 35))
        self.input4.setMaximumSize(QSize(100, 35))

        self.gridLayout.addWidget(self.input4, 4, 2, 1, 1)

        self.input5 = QComboBox(self.groupBox)
        self.input5.addItem("")
        self.input5.setObjectName(u"input5")
        self.input5.setMinimumSize(QSize(100, 35))
        self.input5.setMaximumSize(QSize(100, 35))

        self.gridLayout.addWidget(self.input5, 5, 2, 1, 1)

        self.bias3 = QComboBox(self.groupBox)
        self.bias3.addItem("")
        self.bias3.setObjectName(u"bias3")
        self.bias3.setMaximumSize(QSize(100, 35))
        self.bias3.setStyleSheet(u"background-color:rgb(159, 255, 142);")

        self.gridLayout.addWidget(self.bias3, 3, 3, 1, 1)

        self.srb23 = QComboBox(self.groupBox)
        self.srb23.addItem("")
        self.srb23.setObjectName(u"srb23")
        self.srb23.setMaximumSize(QSize(100, 35))
        self.srb23.setStyleSheet(u"background-color:rgb(159, 255, 142);")

        self.gridLayout.addWidget(self.srb23, 3, 4, 1, 1)

        self.srb13 = QComboBox(self.groupBox)
        self.srb13.addItem("")
        self.srb13.setObjectName(u"srb13")
        self.srb13.setMaximumSize(QSize(100, 35))
        self.srb13.setStyleSheet(u"background-color:rgb(255, 205, 201)")

        self.gridLayout.addWidget(self.srb13, 3, 5, 1, 1)

        self.bias4 = QComboBox(self.groupBox)
        self.bias4.addItem("")
        self.bias4.setObjectName(u"bias4")
        self.bias4.setMaximumSize(QSize(100, 35))
        self.bias4.setStyleSheet(u"background-color:rgb(159, 255, 142);")

        self.gridLayout.addWidget(self.bias4, 4, 3, 1, 1)

        self.srb24 = QComboBox(self.groupBox)
        self.srb24.addItem("")
        self.srb24.setObjectName(u"srb24")
        self.srb24.setMaximumSize(QSize(100, 35))
        self.srb24.setStyleSheet(u"background-color:rgb(159, 255, 142);")

        self.gridLayout.addWidget(self.srb24, 4, 4, 1, 1)

        self.srb14 = QComboBox(self.groupBox)
        self.srb14.addItem("")
        self.srb14.setObjectName(u"srb14")
        self.srb14.setMaximumSize(QSize(100, 35))
        self.srb14.setStyleSheet(u"background-color:rgb(255, 205, 201)")

        self.gridLayout.addWidget(self.srb14, 4, 5, 1, 1)

        self.bias5 = QComboBox(self.groupBox)
        self.bias5.addItem("")
        self.bias5.setObjectName(u"bias5")
        self.bias5.setMaximumSize(QSize(100, 35))
        self.bias5.setStyleSheet(u"background-color:rgb(159, 255, 142);")

        self.gridLayout.addWidget(self.bias5, 5, 3, 1, 1)

        self.srb25 = QComboBox(self.groupBox)
        self.srb25.addItem("")
        self.srb25.setObjectName(u"srb25")
        self.srb25.setMaximumSize(QSize(100, 35))
        self.srb25.setStyleSheet(u"background-color:rgb(159, 255, 142);")

        self.gridLayout.addWidget(self.srb25, 5, 4, 1, 1)

        self.srb15 = QComboBox(self.groupBox)
        self.srb15.addItem("")
        self.srb15.setObjectName(u"srb15")
        self.srb15.setMaximumSize(QSize(100, 35))
        self.srb15.setStyleSheet(u"background-color:rgb(255, 205, 201)")

        self.gridLayout.addWidget(self.srb15, 5, 5, 1, 1)

        self.input6 = QComboBox(self.groupBox)
        self.input6.addItem("")
        self.input6.setObjectName(u"input6")
        self.input6.setMinimumSize(QSize(100, 35))
        self.input6.setMaximumSize(QSize(100, 35))

        self.gridLayout.addWidget(self.input6, 6, 2, 1, 1)

        self.input7 = QComboBox(self.groupBox)
        self.input7.addItem("")
        self.input7.setObjectName(u"input7")
        self.input7.setMinimumSize(QSize(100, 35))
        self.input7.setMaximumSize(QSize(100, 35))

        self.gridLayout.addWidget(self.input7, 7, 2, 1, 1)

        self.bias6 = QComboBox(self.groupBox)
        self.bias6.addItem("")
        self.bias6.setObjectName(u"bias6")
        self.bias6.setMaximumSize(QSize(100, 35))
        self.bias6.setStyleSheet(u"background-color:rgb(159, 255, 142);")

        self.gridLayout.addWidget(self.bias6, 6, 3, 1, 1)

        self.srb26 = QComboBox(self.groupBox)
        self.srb26.addItem("")
        self.srb26.setObjectName(u"srb26")
        self.srb26.setMaximumSize(QSize(100, 35))
        self.srb26.setStyleSheet(u"background-color:rgb(159, 255, 142);")

        self.gridLayout.addWidget(self.srb26, 6, 4, 1, 1)

        self.srb16 = QComboBox(self.groupBox)
        self.srb16.addItem("")
        self.srb16.setObjectName(u"srb16")
        self.srb16.setMaximumSize(QSize(100, 35))
        self.srb16.setStyleSheet(u"background-color:rgb(255, 205, 201)")

        self.gridLayout.addWidget(self.srb16, 6, 5, 1, 1)

        self.input8 = QComboBox(self.groupBox)
        self.input8.addItem("")
        self.input8.setObjectName(u"input8")
        self.input8.setMinimumSize(QSize(100, 35))
        self.input8.setMaximumSize(QSize(100, 35))

        self.gridLayout.addWidget(self.input8, 8, 2, 1, 1)

        self.bias7 = QComboBox(self.groupBox)
        self.bias7.addItem("")
        self.bias7.setObjectName(u"bias7")
        self.bias7.setMaximumSize(QSize(100, 35))
        self.bias7.setStyleSheet(u"background-color:rgb(159, 255, 142);")

        self.gridLayout.addWidget(self.bias7, 7, 3, 1, 1)

        self.bias8 = QComboBox(self.groupBox)
        self.bias8.addItem("")
        self.bias8.setObjectName(u"bias8")
        self.bias8.setMaximumSize(QSize(100, 35))
        self.bias8.setStyleSheet(u"background-color:rgb(159, 255, 142);")

        self.gridLayout.addWidget(self.bias8, 8, 3, 1, 1)

        self.srb27 = QComboBox(self.groupBox)
        self.srb27.addItem("")
        self.srb27.setObjectName(u"srb27")
        self.srb27.setMaximumSize(QSize(100, 35))
        self.srb27.setStyleSheet(u"background-color:rgb(159, 255, 142);")

        self.gridLayout.addWidget(self.srb27, 7, 4, 1, 1)

        self.srb17 = QComboBox(self.groupBox)
        self.srb17.addItem("")
        self.srb17.setObjectName(u"srb17")
        self.srb17.setMaximumSize(QSize(100, 35))
        self.srb17.setStyleSheet(u"background-color:rgb(255, 205, 201)")

        self.gridLayout.addWidget(self.srb17, 7, 5, 1, 1)

        self.srb28 = QComboBox(self.groupBox)
        self.srb28.addItem("")
        self.srb28.setObjectName(u"srb28")
        self.srb28.setMaximumSize(QSize(100, 35))
        self.srb28.setStyleSheet(u"background-color:rgb(159, 255, 142);")

        self.gridLayout.addWidget(self.srb28, 8, 4, 1, 1)

        self.srb18 = QComboBox(self.groupBox)
        self.srb18.addItem("")
        self.srb18.setObjectName(u"srb18")
        self.srb18.setMaximumSize(QSize(100, 35))
        self.srb18.setStyleSheet(u"background-color:rgb(255, 205, 201)")

        self.gridLayout.addWidget(self.srb18, 8, 5, 1, 1)

        self.gridLayout.setRowMinimumHeight(0, 100)
        self.gridLayout.setRowMinimumHeight(1, 100)
        self.gridLayout.setRowMinimumHeight(2, 100)
        self.gridLayout.setRowMinimumHeight(3, 100)
        self.gridLayout.setRowMinimumHeight(4, 100)
        self.gridLayout.setRowMinimumHeight(5, 100)
        self.gridLayout.setRowMinimumHeight(6, 100)
        self.gridLayout.setRowMinimumHeight(7, 100)
        self.gridLayout.setRowMinimumHeight(8, 100)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.reset = QPushButton(self.groupBox)
        self.reset.setObjectName(u"reset")

        self.horizontalLayout.addWidget(self.reset)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.save = QPushButton(self.groupBox)
        self.save.setObjectName(u"save")

        self.horizontalLayout.addWidget(self.save)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.load = QPushButton(self.groupBox)
        self.load.setObjectName(u"load")

        self.horizontalLayout.addWidget(self.load)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(headsetting)

        QMetaObject.connectSlotsByName(headsetting)
    # setupUi

    def retranslateUi(self, headsetting):
        headsetting.setWindowTitle(QCoreApplication.translate("headsetting", u"Form", None))
        self.groupBox.setTitle("")
        self.srb11.setItemText(0, QCoreApplication.translate("headsetting", u"Off", None))

        self.pga1.setItemText(0, QCoreApplication.translate("headsetting", u"x24", None))

        self.input1.setItemText(0, QCoreApplication.translate("headsetting", u"Normal", None))

        self.bias2.setItemText(0, QCoreApplication.translate("headsetting", u"Yes", None))

        self.bias1.setItemText(0, QCoreApplication.translate("headsetting", u"Yes", None))

        self.label_20.setText(QCoreApplication.translate("headsetting", u"7", None))
        self.srb22.setItemText(0, QCoreApplication.translate("headsetting", u"On", None))

        self.label_18.setText(QCoreApplication.translate("headsetting", u"5", None))
        self.label_15.setText(QCoreApplication.translate("headsetting", u"2", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("headsetting", u"PGA", None))
        self.srb12.setItemText(0, QCoreApplication.translate("headsetting", u"Off", None))

        self.label_5.setText(QCoreApplication.translate("headsetting", u"SRB2", None))
        self.label_14.setText(QCoreApplication.translate("headsetting", u"1", None))
        self.label_3.setText(QCoreApplication.translate("headsetting", u"input Type", None))
        self.label_19.setText(QCoreApplication.translate("headsetting", u"6", None))
        self.label_4.setText(QCoreApplication.translate("headsetting", u"Bias include", None))
        self.label_17.setText(QCoreApplication.translate("headsetting", u"4", None))
        self.label_6.setText(QCoreApplication.translate("headsetting", u"SRB1", None))
        self.input2.setItemText(0, QCoreApplication.translate("headsetting", u"Normal", None))

        self.pga2.setItemText(0, QCoreApplication.translate("headsetting", u"x24", None))

        self.label_16.setText(QCoreApplication.translate("headsetting", u"3", None))
        self.srb21.setItemText(0, QCoreApplication.translate("headsetting", u"On", None))

        self.label_21.setText(QCoreApplication.translate("headsetting", u"8", None))
        self.pga3.setItemText(0, QCoreApplication.translate("headsetting", u"x24", None))

        self.pga4.setItemText(0, QCoreApplication.translate("headsetting", u"x24", None))

        self.pga5.setItemText(0, QCoreApplication.translate("headsetting", u"x24", None))

        self.pga6.setItemText(0, QCoreApplication.translate("headsetting", u"x24", None))

        self.pga7.setItemText(0, QCoreApplication.translate("headsetting", u"x24", None))

        self.pga8.setItemText(0, QCoreApplication.translate("headsetting", u"x24", None))

        self.input3.setItemText(0, QCoreApplication.translate("headsetting", u"Normal", None))

        self.input4.setItemText(0, QCoreApplication.translate("headsetting", u"Normal", None))

        self.input5.setItemText(0, QCoreApplication.translate("headsetting", u"Normal", None))

        self.bias3.setItemText(0, QCoreApplication.translate("headsetting", u"Yes", None))

        self.srb23.setItemText(0, QCoreApplication.translate("headsetting", u"On", None))

        self.srb13.setItemText(0, QCoreApplication.translate("headsetting", u"Off", None))

        self.bias4.setItemText(0, QCoreApplication.translate("headsetting", u"Yes", None))

        self.srb24.setItemText(0, QCoreApplication.translate("headsetting", u"On", None))

        self.srb14.setItemText(0, QCoreApplication.translate("headsetting", u"Off", None))

        self.bias5.setItemText(0, QCoreApplication.translate("headsetting", u"Yes", None))

        self.srb25.setItemText(0, QCoreApplication.translate("headsetting", u"On", None))

        self.srb15.setItemText(0, QCoreApplication.translate("headsetting", u"Off", None))

        self.input6.setItemText(0, QCoreApplication.translate("headsetting", u"Normal", None))

        self.input7.setItemText(0, QCoreApplication.translate("headsetting", u"Normal", None))

        self.bias6.setItemText(0, QCoreApplication.translate("headsetting", u"Yes", None))

        self.srb26.setItemText(0, QCoreApplication.translate("headsetting", u"On", None))

        self.srb16.setItemText(0, QCoreApplication.translate("headsetting", u"Off", None))

        self.input8.setItemText(0, QCoreApplication.translate("headsetting", u"Normal", None))

        self.bias7.setItemText(0, QCoreApplication.translate("headsetting", u"Yes", None))

        self.bias8.setItemText(0, QCoreApplication.translate("headsetting", u"Yes", None))

        self.srb27.setItemText(0, QCoreApplication.translate("headsetting", u"On", None))

        self.srb17.setItemText(0, QCoreApplication.translate("headsetting", u"Off", None))

        self.srb28.setItemText(0, QCoreApplication.translate("headsetting", u"On", None))

        self.srb18.setItemText(0, QCoreApplication.translate("headsetting", u"Off", None))

        self.reset.setText(QCoreApplication.translate("headsetting", u"Reset", None))
        self.save.setText(QCoreApplication.translate("headsetting", u"Save", None))
        self.load.setText(QCoreApplication.translate("headsetting", u"Load", None))
    # retranslateUi

