# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lsl.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from switchbutton import switchbutton

import res_rc

class Ui_lsl(object):
    def setupUi(self, lsl):
        if not lsl.objectName():
            lsl.setObjectName(u"lsl")
        lsl.resize(561, 410)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(lsl.sizePolicy().hasHeightForWidth())
        lsl.setSizePolicy(sizePolicy)
        lsl.setMinimumSize(QSize(561, 410))
        lsl.setMaximumSize(QSize(561, 410))
        lsl.setStyleSheet(u"*{\n"
"	background-color:rgb(14, 49, 117);\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QComboBox{\n"
"	background-color:rgb(255,255,255);\n"
"	color:rgb(0,0,0);\n"
"}\n"
"QLineEdit{\n"
"	background-color:rgb(255,255,255);\n"
"	color:rgb(0,0,0);\n"
"}\n"
"QGroupBox{border:none;}")
        self.verticalLayout_2 = QVBoxLayout(lsl)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(lsl)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/res/frame.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(236, 44))
        self.pushButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(18)
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.groupBox)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy1.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy1)
        self.comboBox_3.setMinimumSize(QSize(0, 0))
        self.comboBox_3.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.comboBox_3, 1, 3, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy1.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy1)
        self.comboBox_2.setMinimumSize(QSize(0, 0))
        self.comboBox_2.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.comboBox_2, 1, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy1.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy1)
        self.lineEdit_6.setMinimumSize(QSize(0, 0))
        self.lineEdit_6.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.lineEdit_6, 3, 2, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(0, 0))
        self.lineEdit.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1, Qt.AlignHCenter)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy1.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy1)
        self.lineEdit_3.setMinimumSize(QSize(0, 0))
        self.lineEdit_3.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.lineEdit_3, 3, 3, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy1.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy1)
        self.lineEdit_4.setMinimumSize(QSize(0, 0))
        self.lineEdit_4.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy1.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy1)
        self.lineEdit_5.setMinimumSize(QSize(0, 0))
        self.lineEdit_5.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.lineEdit_5, 2, 3, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1, Qt.AlignHCenter)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy2)
        self.lineEdit_2.setMinimumSize(QSize(0, 0))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.lineEdit_2, 2, 2, 1, 1)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setMinimumSize(QSize(0, 0))
        self.comboBox.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1, Qt.AlignHCenter)

        self.widget = switchbutton(self.groupBox)
        self.widget.setObjectName(u"widget")
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(80, 36))
        self.widget.setMaximumSize(QSize(80, 36))

        self.gridLayout.addWidget(self.widget, 4, 1, 1, 1, Qt.AlignRight)

        self.widget_2 = switchbutton(self.groupBox)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMinimumSize(QSize(80, 36))
        self.widget_2.setMaximumSize(QSize(80, 36))

        self.gridLayout.addWidget(self.widget_2, 4, 2, 1, 1, Qt.AlignRight)

        self.widget_3 = switchbutton(self.groupBox)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setMinimumSize(QSize(80, 36))
        self.widget_3.setMaximumSize(QSize(80, 36))

        self.gridLayout.addWidget(self.widget_3, 4, 3, 1, 1, Qt.AlignRight)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)

        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(lsl)

        QMetaObject.connectSlotsByName(lsl)
    # setupUi

    def retranslateUi(self, lsl):
        lsl.setWindowTitle(QCoreApplication.translate("lsl", u"Form", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("lsl", u"lsl", None))
        self.pushButton.setText("")
        self.label_9.setText("")
        self.comboBox_3.setItemText(0, QCoreApplication.translate("lsl", u"timeserise", None))

        self.label_8.setText(QCoreApplication.translate("lsl", u"type", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("lsl", u"timeseries", None))

        self.label_5.setText(QCoreApplication.translate("lsl", u"dataType", None))
        self.lineEdit_6.setText(QCoreApplication.translate("lsl", u"eeg", None))
        self.lineEdit.setText(QCoreApplication.translate("lsl", u"obci_eeg1", None))
        self.label_3.setText(QCoreApplication.translate("lsl", u"stream2", None))
        self.lineEdit_3.setText(QCoreApplication.translate("lsl", u"eeg", None))
        self.lineEdit_4.setText(QCoreApplication.translate("lsl", u"eeg", None))
        self.lineEdit_5.setText(QCoreApplication.translate("lsl", u"obci_eeg1", None))
        self.label_7.setText(QCoreApplication.translate("lsl", u"filter", None))
        self.label_4.setText(QCoreApplication.translate("lsl", u"stream3", None))
        self.label_6.setText(QCoreApplication.translate("lsl", u"Name", None))
        self.lineEdit_2.setText(QCoreApplication.translate("lsl", u"obci_eeg1", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("lsl", u"timeserise", None))

        self.label_2.setText(QCoreApplication.translate("lsl", u"stream1", None))
    # retranslateUi

