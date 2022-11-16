# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'allbox.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_allbox(object):
    def setupUi(self, allbox):
        if not allbox.objectName():
            allbox.setObjectName(u"allbox")
        allbox.resize(764, 374)
        allbox.setStyleSheet(u"*{\n"
"	background-color:rgb(0,0,90);\n"
"	color:rgb(255,255,255);\n"
"}\n"
"#groupBox {\n"
"	background-color:rgb(0,0,127);\n"
"}\n"
"#groupBox>QLabel{\n"
"	background-color:rgb(0,0,127);\n"
"}\n"
"QComboBox{\n"
"	background-color:rgb(255,255,255);\n"
"	color:rgb(0,0,0);\n"
"}\n"
"QLineEdit{\n"
"	background-color:rgb(255,255,255);\n"
"	color:rgb(0,0,0);\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(allbox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_2 = QGroupBox(allbox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.filter = QComboBox(self.groupBox)
        self.filter.addItem("")
        self.filter.setObjectName(u"filter")
        self.filter.setMinimumSize(QSize(140, 35))
        self.filter.setStyleSheet(u"margin-bottom:5px;")

        self.horizontalLayout_2.addWidget(self.filter, 0, Qt.AlignHCenter)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_13)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.notch = QComboBox(self.groupBox)
        self.notch.addItem("")
        self.notch.setObjectName(u"notch")
        self.notch.setMinimumSize(QSize(140, 35))
        self.notch.setStyleSheet(u"margin-bottom:5px;")

        self.horizontalLayout_2.addWidget(self.notch)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(4, 1)
        self.horizontalLayout_2.setStretch(5, 1)
        self.horizontalLayout_2.setStretch(6, 4)

        self.verticalLayout_6.addWidget(self.groupBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(62, 19))

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(90, 35))
        self.pushButton.setStyleSheet(u"background-color: rgb(11, 28, 84);")

        self.verticalLayout.addWidget(self.pushButton)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(70, 19))

        self.verticalLayout_2.addWidget(self.label_4, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.start = QLineEdit(self.groupBox_2)
        self.start.setObjectName(u"start")
        self.start.setMinimumSize(QSize(90, 35))

        self.verticalLayout_2.addWidget(self.start)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_10)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(68, 19))

        self.verticalLayout_3.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.stop = QLineEdit(self.groupBox_2)
        self.stop.setObjectName(u"stop")
        self.stop.setMinimumSize(QSize(90, 35))

        self.verticalLayout_3.addWidget(self.stop)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_11)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(38, 19))

        self.verticalLayout_4.addWidget(self.label_6, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.type = QComboBox(self.groupBox_2)
        self.type.addItem("")
        self.type.setObjectName(u"type")
        self.type.setMinimumSize(QSize(140, 35))

        self.verticalLayout_4.addWidget(self.type)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_12)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(44, 19))

        self.verticalLayout_5.addWidget(self.label_7, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.order = QComboBox(self.groupBox_2)
        self.order.addItem("")
        self.order.setObjectName(u"order")
        self.order.setMinimumSize(QSize(90, 35))

        self.verticalLayout_5.addWidget(self.order)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 1)
        self.horizontalLayout.setStretch(5, 1)
        self.horizontalLayout.setStretch(6, 1)
        self.horizontalLayout.setStretch(7, 1)
        self.horizontalLayout.setStretch(8, 1)
        self.horizontalLayout.setStretch(9, 1)
        self.horizontalLayout.setStretch(10, 2)

        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.reset = QPushButton(self.groupBox_2)
        self.reset.setObjectName(u"reset")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset.sizePolicy().hasHeightForWidth())
        self.reset.setSizePolicy(sizePolicy)
        self.reset.setMinimumSize(QSize(85, 43))
        self.reset.setStyleSheet(u"padding:20px;\n"
"background-color: rgb(57, 114, 224);")
        self.reset.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.reset)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.save = QPushButton(self.groupBox_2)
        self.save.setObjectName(u"save")
        sizePolicy.setHeightForWidth(self.save.sizePolicy().hasHeightForWidth())
        self.save.setSizePolicy(sizePolicy)
        self.save.setMinimumSize(QSize(85, 43))
        self.save.setStyleSheet(u"padding:20px;\n"
"background-color: rgb(57, 114, 224);")
        self.save.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.save)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.load = QPushButton(self.groupBox_2)
        self.load.setObjectName(u"load")
        self.load.setMinimumSize(QSize(85, 43))
        self.load.setStyleSheet(u"padding:20px;\n"
"background-color: rgb(57, 114, 224);")
        self.load.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.load)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 56, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)


        self.verticalLayout_7.addWidget(self.groupBox_2)


        self.retranslateUi(allbox)

        QMetaObject.connectSlotsByName(allbox)
    # setupUi

    def retranslateUi(self, allbox):
        allbox.setWindowTitle(QCoreApplication.translate("allbox", u"Dialog", None))
        self.groupBox_2.setTitle("")
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("allbox", u"Filter", None))
        self.filter.setItemText(0, QCoreApplication.translate("allbox", u"Band Pass", None))

        self.label_2.setText(QCoreApplication.translate("allbox", u"Notch", None))
        self.notch.setItemText(0, QCoreApplication.translate("allbox", u"50+60Hz", None))

        self.label_3.setText(QCoreApplication.translate("allbox", u"Channel", None))
        self.pushButton.setText(QCoreApplication.translate("allbox", u"All", None))
        self.label_4.setText(QCoreApplication.translate("allbox", u"Start(Hz)", None))
        self.start.setText(QCoreApplication.translate("allbox", u"5.0", None))
        self.label_5.setText(QCoreApplication.translate("allbox", u"Stop(Hz)", None))
        self.stop.setText(QCoreApplication.translate("allbox", u"50.0", None))
        self.label_6.setText(QCoreApplication.translate("allbox", u"Type", None))
        self.type.setItemText(0, QCoreApplication.translate("allbox", u"Butterworth", None))

        self.label_7.setText(QCoreApplication.translate("allbox", u"Order", None))
        self.order.setItemText(0, QCoreApplication.translate("allbox", u"4", None))

        self.reset.setText(QCoreApplication.translate("allbox", u"Reset", None))
        self.save.setText(QCoreApplication.translate("allbox", u"Save", None))
        self.load.setText(QCoreApplication.translate("allbox", u"Load", None))
    # retranslateUi

