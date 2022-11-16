# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Layout(object):
    def setupUi(self, Layout):
        if not Layout.objectName():
            Layout.setObjectName(u"Layout")
        Layout.resize(816, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Layout.sizePolicy().hasHeightForWidth())
        Layout.setSizePolicy(sizePolicy)
        Layout.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(Layout)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 6, -1, -1)
        self.w1 = QWidget(Layout)
        self.w1.setObjectName(u"w1")
        sizePolicy.setHeightForWidth(self.w1.sizePolicy().hasHeightForWidth())
        self.w1.setSizePolicy(sizePolicy)
        self.w1.setStyleSheet(u"background-color: rgb(14, 49, 117);")
        self.horizontalLayout_2 = QHBoxLayout(self.w1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.v1 = QVBoxLayout()
        self.v1.setObjectName(u"v1")
        self.v1.setSizeConstraint(QLayout.SetMinimumSize)

        self.horizontalLayout_2.addLayout(self.v1)


        self.verticalLayout.addWidget(self.w1)

        self.w4 = QWidget(Layout)
        self.w4.setObjectName(u"w4")
        sizePolicy.setHeightForWidth(self.w4.sizePolicy().hasHeightForWidth())
        self.w4.setSizePolicy(sizePolicy)
        self.w4.setStyleSheet(u"background-color: rgb(14, 49, 117);")
        self.horizontalLayout_5 = QHBoxLayout(self.w4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.v4 = QVBoxLayout()
        self.v4.setObjectName(u"v4")
        self.v4.setContentsMargins(-1, -1, -1, 6)

        self.horizontalLayout_5.addLayout(self.v4)


        self.verticalLayout.addWidget(self.w4)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 6, -1, -1)
        self.w2 = QWidget(Layout)
        self.w2.setObjectName(u"w2")
        sizePolicy.setHeightForWidth(self.w2.sizePolicy().hasHeightForWidth())
        self.w2.setSizePolicy(sizePolicy)
        self.w2.setStyleSheet(u"background-color: rgb(14, 49, 117);")
        self.horizontalLayout_3 = QHBoxLayout(self.w2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.v2 = QVBoxLayout()
        self.v2.setObjectName(u"v2")

        self.horizontalLayout_3.addLayout(self.v2)


        self.verticalLayout_2.addWidget(self.w2)

        self.w3 = QWidget(Layout)
        self.w3.setObjectName(u"w3")
        sizePolicy.setHeightForWidth(self.w3.sizePolicy().hasHeightForWidth())
        self.w3.setSizePolicy(sizePolicy)
        self.w3.setStyleSheet(u"background-color: rgb(14, 49, 117);")
        self.horizontalLayout_4 = QHBoxLayout(self.w3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.v3 = QVBoxLayout()
        self.v3.setObjectName(u"v3")
        self.v3.setContentsMargins(-1, -1, -1, 6)

        self.horizontalLayout_4.addLayout(self.v3)


        self.verticalLayout_2.addWidget(self.w3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Layout)

        QMetaObject.connectSlotsByName(Layout)
    # setupUi

    def retranslateUi(self, Layout):
        Layout.setWindowTitle(QCoreApplication.translate("Layout", u"Form", None))
    # retranslateUi

