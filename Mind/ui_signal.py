# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_signal(object):
    def setupUi(self, signal):
        if not signal.objectName():
            signal.setObjectName(u"signal")
        signal.resize(561, 410)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(signal.sizePolicy().hasHeightForWidth())
        signal.setSizePolicy(sizePolicy)
        signal.setStyleSheet(u"QWidget#signal{border:1px solid rgb(255,255,255)}\n"
"*{\n"
"	background-color:rgb(14, 49, 117);\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QLineEdit{\n"
"	background-color:rgb(255,255,255);\n"
"	color:rgb(0,0,0);\n"
"}\n"
"QGroupBox{border:none;}")
        self.verticalLayout_4 = QVBoxLayout(signal)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(signal)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 9)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 40))
        self.label_13.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_13)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(90, 35))
        self.lineEdit.setMaximumSize(QSize(90, 40))
        self.lineEdit.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(90, 35))
        self.lineEdit_2.setMaximumSize(QSize(90, 40))

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 9, -1, -1)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(76, 24))

        self.horizontalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(76, 24))

        self.horizontalLayout.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(76, 24))

        self.horizontalLayout.addWidget(self.label_4, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout.addWidget(self.label_11)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.widget_2 = QWidget(self.groupBox)
        self.widget_2.setObjectName(u"widget_2")

        self.horizontalLayout_3.addWidget(self.widget_2)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 7)

        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(270, 281))
        self.widget.setMaximumSize(QSize(270, 281))
        self.widget.setStyleSheet(u"background-color:white;\n"
"")

        self.horizontalLayout_4.addWidget(self.widget)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addWidget(self.groupBox)


        self.retranslateUi(signal)

        QMetaObject.connectSlotsByName(signal)
    # setupUi

    def retranslateUi(self, signal):
        signal.setWindowTitle(QCoreApplication.translate("signal", u"Form", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("signal", u"signal", None))
        self.label_13.setText(QCoreApplication.translate("signal", u"thresholds:", None))
        self.lineEdit.setText(QCoreApplication.translate("signal", u"750k", None))
        self.lineEdit_2.setText(QCoreApplication.translate("signal", u"2500k", None))
        self.label_2.setText(QCoreApplication.translate("signal", u"channel", None))
        self.label_3.setText(QCoreApplication.translate("signal", u"N-status", None))
        self.label_4.setText(QCoreApplication.translate("signal", u"P-status", None))
        self.label_5.setText(QCoreApplication.translate("signal", u"1", None))
        self.label_6.setText(QCoreApplication.translate("signal", u"2", None))
        self.label_11.setText(QCoreApplication.translate("signal", u"3", None))
        self.label_7.setText(QCoreApplication.translate("signal", u"4", None))
        self.label_10.setText(QCoreApplication.translate("signal", u"5", None))
        self.label_8.setText(QCoreApplication.translate("signal", u"6", None))
    # retranslateUi

