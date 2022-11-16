# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hwselect.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_hwselect(object):
    def setupUi(self, hwselect):
        if not hwselect.objectName():
            hwselect.setObjectName(u"hwselect")
        hwselect.resize(229, 187)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(hwselect.sizePolicy().hasHeightForWidth())
        hwselect.setSizePolicy(sizePolicy)
        hwselect.setStyleSheet(u".QPushButton{padding:10px;\n"
"border:1px solid rgb(255,255,255);}\n"
"*{background-color:rgb(37, 74, 146);\n"
"color:rgb(255,255,255);}\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(hwselect)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(hwselect)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(167, 156))
        self.groupBox.setMaximumSize(QSize(167, 156))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 9)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(143, 40))
        self.pushButton.setMaximumSize(QSize(143, 40))
        self.pushButton.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(88, 40))
        self.pushButton_2.setMaximumSize(QSize(88, 40))
        self.pushButton_2.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_2, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.groupBox, 0, Qt.AlignTop)


        self.retranslateUi(hwselect)

        QMetaObject.connectSlotsByName(hwselect)
    # setupUi

    def retranslateUi(self, hwselect):
        hwselect.setWindowTitle(QCoreApplication.translate("hwselect", u"Form", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("hwselect", u"\u8bf7\u9009\u62e9\u4e0d\u540c\u6a21\u5f0f", None))
        self.pushButton.setText(QCoreApplication.translate("hwselect", u"MX HADWARE NO.1", None))
        self.pushButton_2.setText(QCoreApplication.translate("hwselect", u"PLAYBACK", None))
    # retranslateUi

