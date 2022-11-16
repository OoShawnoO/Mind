# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_config(object):
    def setupUi(self, config):
        if not config.objectName():
            config.setObjectName(u"config")
        config.resize(538, 480)
        config.setStyleSheet(u"*{\n"
"background-color:rgb(11, 28, 84);\n"
"color:rgb(255,255,255);\n"
"}\n"
"QRadioButton::indicator{\n"
"	width:15px;\n"
"	height:15px;\n"
"	border-radius:8px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: black;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	background-color:green;\n"
"}\n"
"QRadioButton::indicator:unchecked {\n"
"	background-color:rgb(255, 255, 255);\n"
"}\n"
"QLineEdit{\n"
"	background-color:rgb(255,255,255);\n"
"	color:rgb(0,0,0);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(config)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(config)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))
        self.label.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.label)

        self.groupBox = QGroupBox(config)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.retTime = QLineEdit(self.groupBox)
        self.retTime.setObjectName(u"retTime")
        self.retTime.setMinimumSize(QSize(210, 41))

        self.horizontalLayout_4.addWidget(self.retTime)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ipAddress = QLineEdit(self.groupBox)
        self.ipAddress.setObjectName(u"ipAddress")
        self.ipAddress.setMinimumSize(QSize(210, 41))

        self.horizontalLayout_5.addWidget(self.ipAddress)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.frequency = QGroupBox(self.groupBox)
        self.frequency.setObjectName(u"frequency")
        self.horizontalLayout = QHBoxLayout(self.frequency)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.h40 = QRadioButton(self.frequency)
        self.h40.setObjectName(u"h40")

        self.horizontalLayout.addWidget(self.h40)

        self.h20 = QRadioButton(self.frequency)
        self.h20.setObjectName(u"h20")

        self.horizontalLayout.addWidget(self.h20)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frequency)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.channels = QGroupBox(self.groupBox)
        self.channels.setObjectName(u"channels")
        self.horizontalLayout_2 = QHBoxLayout(self.channels)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.c8 = QRadioButton(self.channels)
        self.c8.setObjectName(u"c8")

        self.horizontalLayout_2.addWidget(self.c8)

        self.c16 = QRadioButton(self.channels)
        self.c16.setObjectName(u"c16")

        self.horizontalLayout_2.addWidget(self.c16)

        self.c32 = QRadioButton(self.channels)
        self.c32.setObjectName(u"c32")

        self.horizontalLayout_2.addWidget(self.c32)

        self.c64 = QRadioButton(self.channels)
        self.c64.setObjectName(u"c64")

        self.horizontalLayout_2.addWidget(self.c64)


        self.verticalLayout.addWidget(self.channels)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cancel = QPushButton(self.groupBox)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setMinimumSize(QSize(85, 43))
        self.cancel.setStyleSheet(u"background-color: rgb(57, 114, 224);")

        self.horizontalLayout_3.addWidget(self.cancel)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.start = QPushButton(self.groupBox)
        self.start.setObjectName(u"start")
        self.start.setMinimumSize(QSize(112, 43))
        self.start.setStyleSheet(u"background-color: rgb(48, 171, 195);")

        self.horizontalLayout_3.addWidget(self.start)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(config)

        QMetaObject.connectSlotsByName(config)
    # setupUi

    def retranslateUi(self, config):
        config.setWindowTitle(QCoreApplication.translate("config", u"Form", None))
        self.label.setText(QCoreApplication.translate("config", u"\u586b\u5199\u76f8\u5173\u914d\u7f6e", None))
        self.groupBox.setTitle("")
        self.label_2.setText(QCoreApplication.translate("config", u"\u56de\u8bdd\u65f6\u95f4", None))
        self.label_3.setText(QCoreApplication.translate("config", u"ip\u5730\u5740", None))
        self.label_4.setText(QCoreApplication.translate("config", u"\u9891\u7387\u9009\u62e9", None))
        self.frequency.setTitle("")
        self.h40.setText(QCoreApplication.translate("config", u"40Hz", None))
        self.h20.setText(QCoreApplication.translate("config", u"20Hz", None))
        self.label_5.setText(QCoreApplication.translate("config", u"\u901a\u9053\u9009\u62e9", None))
        self.channels.setTitle("")
        self.c8.setText(QCoreApplication.translate("config", u"8\u901a\u9053", None))
        self.c16.setText(QCoreApplication.translate("config", u"16\u901a\u9053", None))
        self.c32.setText(QCoreApplication.translate("config", u"32\u901a\u9053", None))
        self.c64.setText(QCoreApplication.translate("config", u"64\u901a\u9053", None))
        self.cancel.setText(QCoreApplication.translate("config", u"\u53d6\u6d88", None))
        self.start.setText(QCoreApplication.translate("config", u"\u8fdb\u5165\u5b9e\u9a8c", None))
    # retranslateUi

