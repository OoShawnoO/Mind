# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'common.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_common(object):
    def setupUi(self, common):
        if not common.objectName():
            common.setObjectName(u"common")
        common.resize(360, 600)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(common.sizePolicy().hasHeightForWidth())
        common.setSizePolicy(sizePolicy)
        common.setStyleSheet(u"*{\n"
"	background-color:rgb(0, 10, 117);\n"
"	color:rgb(255,255,255);\n"
"}\n"
"\n"
"QGroupBox{\n"
"	border:none;\n"
"}\n"
"QScrollArea{\n"
"	border:none;\n"
"}\n"
"QRadioButton::indicator{\n"
"	width:15px;\n"
"	height:15px;\n"
"	border-radius:8px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: black;\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"	background-color:rgb(255, 255, 255);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	background-color:rgb(255, 170, 127);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	background-color:rgb(255, 170, 127);\n"
"}\n"
"QRadioButton::indicator:unchecked {\n"
"	background-color:rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(common)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.groupBox_8 = QGroupBox(common)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.groupBox_8)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.groupBox_8)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_15.addLayout(self.horizontalLayout)


        self.verticalLayout_9.addWidget(self.groupBox_8)

        self.scrollArea = QScrollArea(common)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 360, 1188))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.channel = QGroupBox(self.scrollAreaWidgetContents)
        self.channel.setObjectName(u"channel")
        self.verticalLayout_8 = QVBoxLayout(self.channel)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.channel)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_4, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.channel1to64 = QGroupBox(self.channel)
        self.channel1to64.setObjectName(u"channel1to64")
        self.channel1to64.setMaximumSize(QSize(166, 16777215))
        self.verticalLayout = QVBoxLayout(self.channel1to64)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.c1t8 = QCheckBox(self.channel1to64)
        self.c1t8.setObjectName(u"c1t8")
        self.c1t8.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.c1t8)

        self.c9t16 = QCheckBox(self.channel1to64)
        self.c9t16.setObjectName(u"c9t16")
        self.c9t16.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.c9t16)

        self.c17t24 = QCheckBox(self.channel1to64)
        self.c17t24.setObjectName(u"c17t24")
        self.c17t24.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.c17t24)

        self.c25t32 = QCheckBox(self.channel1to64)
        self.c25t32.setObjectName(u"c25t32")
        self.c25t32.setMaximumSize(QSize(16777215, 16777215))
        self.c25t32.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.c25t32)

        self.c33t40 = QCheckBox(self.channel1to64)
        self.c33t40.setObjectName(u"c33t40")
        self.c33t40.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.c33t40)

        self.c41t48 = QCheckBox(self.channel1to64)
        self.c41t48.setObjectName(u"c41t48")
        self.c41t48.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.c41t48)

        self.c49t56 = QCheckBox(self.channel1to64)
        self.c49t56.setObjectName(u"c49t56")
        self.c49t56.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.c49t56)

        self.c57t64 = QCheckBox(self.channel1to64)
        self.c57t64.setObjectName(u"c57t64")
        self.c57t64.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.c57t64)


        self.horizontalLayout_3.addWidget(self.channel1to64)

        self.channelselect = QGroupBox(self.channel)
        self.channelselect.setObjectName(u"channelselect")
        self.verticalLayout_2 = QVBoxLayout(self.channelselect)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.c1 = QCheckBox(self.channelselect)
        self.c1.setObjectName(u"c1")
        self.c1.setTristate(False)

        self.verticalLayout_2.addWidget(self.c1)

        self.c2 = QCheckBox(self.channelselect)
        self.c2.setObjectName(u"c2")

        self.verticalLayout_2.addWidget(self.c2)

        self.c3 = QCheckBox(self.channelselect)
        self.c3.setObjectName(u"c3")

        self.verticalLayout_2.addWidget(self.c3)

        self.c4 = QCheckBox(self.channelselect)
        self.c4.setObjectName(u"c4")

        self.verticalLayout_2.addWidget(self.c4)

        self.c5 = QCheckBox(self.channelselect)
        self.c5.setObjectName(u"c5")

        self.verticalLayout_2.addWidget(self.c5)

        self.c6 = QCheckBox(self.channelselect)
        self.c6.setObjectName(u"c6")

        self.verticalLayout_2.addWidget(self.c6)

        self.c7 = QCheckBox(self.channelselect)
        self.c7.setObjectName(u"c7")

        self.verticalLayout_2.addWidget(self.c7)

        self.c8 = QCheckBox(self.channelselect)
        self.c8.setObjectName(u"c8")

        self.verticalLayout_2.addWidget(self.c8)


        self.horizontalLayout_3.addWidget(self.channelselect, 0, Qt.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)


        self.verticalLayout_15.addWidget(self.channel)

        self.maxfrequency = QGroupBox(self.scrollAreaWidgetContents)
        self.maxfrequency.setObjectName(u"maxfrequency")
        self.verticalLayout_10 = QVBoxLayout(self.maxfrequency)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.maxfrequency)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.maxfrequency_box = QGroupBox(self.maxfrequency)
        self.maxfrequency_box.setObjectName(u"maxfrequency_box")
        self.verticalLayout_3 = QVBoxLayout(self.maxfrequency_box)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.h20 = QRadioButton(self.maxfrequency_box)
        self.h20.setObjectName(u"h20")

        self.verticalLayout_3.addWidget(self.h20)

        self.h40 = QRadioButton(self.maxfrequency_box)
        self.h40.setObjectName(u"h40")

        self.verticalLayout_3.addWidget(self.h40)

        self.h60 = QRadioButton(self.maxfrequency_box)
        self.h60.setObjectName(u"h60")

        self.verticalLayout_3.addWidget(self.h60)

        self.h100 = QRadioButton(self.maxfrequency_box)
        self.h100.setObjectName(u"h100")

        self.verticalLayout_3.addWidget(self.h100)

        self.h200 = QRadioButton(self.maxfrequency_box)
        self.h200.setObjectName(u"h200")

        self.verticalLayout_3.addWidget(self.h200)

        self.h500 = QRadioButton(self.maxfrequency_box)
        self.h500.setObjectName(u"h500")

        self.verticalLayout_3.addWidget(self.h500)


        self.verticalLayout_16.addWidget(self.maxfrequency_box)


        self.verticalLayout_10.addLayout(self.verticalLayout_16)


        self.verticalLayout_15.addWidget(self.maxfrequency)

        self.model = QGroupBox(self.scrollAreaWidgetContents)
        self.model.setObjectName(u"model")
        self.verticalLayout_11 = QVBoxLayout(self.model)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.model)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.modelbox = QGroupBox(self.model)
        self.modelbox.setObjectName(u"modelbox")
        self.verticalLayout_4 = QVBoxLayout(self.modelbox)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.line = QRadioButton(self.modelbox)
        self.line.setObjectName(u"line")

        self.verticalLayout_4.addWidget(self.line)

        self.log = QRadioButton(self.modelbox)
        self.log.setObjectName(u"log")

        self.verticalLayout_4.addWidget(self.log)


        self.verticalLayout_17.addWidget(self.modelbox)

        self.verticalLayout_17.setStretch(0, 2)

        self.verticalLayout_11.addLayout(self.verticalLayout_17)


        self.verticalLayout_15.addWidget(self.model)

        self.window = QGroupBox(self.scrollAreaWidgetContents)
        self.window.setObjectName(u"window")
        self.verticalLayout_12 = QVBoxLayout(self.window)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.window)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_18.addLayout(self.horizontalLayout_9)

        self.windowbox = QGroupBox(self.window)
        self.windowbox.setObjectName(u"windowbox")
        self.verticalLayout_5 = QVBoxLayout(self.windowbox)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.min1 = QRadioButton(self.windowbox)
        self.min1.setObjectName(u"min1")

        self.verticalLayout_5.addWidget(self.min1)

        self.min3 = QRadioButton(self.windowbox)
        self.min3.setObjectName(u"min3")

        self.verticalLayout_5.addWidget(self.min3)

        self.min6 = QRadioButton(self.windowbox)
        self.min6.setObjectName(u"min6")

        self.verticalLayout_5.addWidget(self.min6)

        self.min15 = QRadioButton(self.windowbox)
        self.min15.setObjectName(u"min15")

        self.verticalLayout_5.addWidget(self.min15)

        self.min30 = QRadioButton(self.windowbox)
        self.min30.setObjectName(u"min30")

        self.verticalLayout_5.addWidget(self.min30)


        self.verticalLayout_18.addWidget(self.windowbox)

        self.verticalLayout_18.setStretch(1, 2)

        self.verticalLayout_12.addLayout(self.verticalLayout_18)


        self.verticalLayout_15.addWidget(self.window)

        self.timelength = QGroupBox(self.scrollAreaWidgetContents)
        self.timelength.setObjectName(u"timelength")
        self.verticalLayout_13 = QVBoxLayout(self.timelength)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.timelength)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_11.addWidget(self.label_12)


        self.verticalLayout_13.addLayout(self.horizontalLayout_11)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.timelengthbox = QGroupBox(self.timelength)
        self.timelengthbox.setObjectName(u"timelengthbox")
        self.verticalLayout_6 = QVBoxLayout(self.timelengthbox)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.s1 = QRadioButton(self.timelengthbox)
        self.s1.setObjectName(u"s1")

        self.verticalLayout_6.addWidget(self.s1)

        self.s3 = QRadioButton(self.timelengthbox)
        self.s3.setObjectName(u"s3")

        self.verticalLayout_6.addWidget(self.s3)

        self.s5 = QRadioButton(self.timelengthbox)
        self.s5.setObjectName(u"s5")

        self.verticalLayout_6.addWidget(self.s5)

        self.s10 = QRadioButton(self.timelengthbox)
        self.s10.setObjectName(u"s10")

        self.verticalLayout_6.addWidget(self.s10)

        self.s20 = QRadioButton(self.timelengthbox)
        self.s20.setObjectName(u"s20")

        self.verticalLayout_6.addWidget(self.s20)


        self.verticalLayout_19.addWidget(self.timelengthbox)

        self.verticalLayout_19.setStretch(0, 2)

        self.verticalLayout_13.addLayout(self.verticalLayout_19)


        self.verticalLayout_15.addWidget(self.timelength)

        self.scale = QGroupBox(self.scrollAreaWidgetContents)
        self.scale.setObjectName(u"scale")
        self.verticalLayout_14 = QVBoxLayout(self.scale)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_14 = QLabel(self.scale)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_13.addWidget(self.label_14, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_14.addLayout(self.horizontalLayout_13)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.scalebox = QGroupBox(self.scale)
        self.scalebox.setObjectName(u"scalebox")
        self.verticalLayout_7 = QVBoxLayout(self.scalebox)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.uvauto = QRadioButton(self.scalebox)
        self.uvauto.setObjectName(u"uvauto")

        self.verticalLayout_7.addWidget(self.uvauto)

        self.uv50 = QRadioButton(self.scalebox)
        self.uv50.setObjectName(u"uv50")

        self.verticalLayout_7.addWidget(self.uv50)

        self.uv100 = QRadioButton(self.scalebox)
        self.uv100.setObjectName(u"uv100")

        self.verticalLayout_7.addWidget(self.uv100)

        self.uv200 = QRadioButton(self.scalebox)
        self.uv200.setObjectName(u"uv200")

        self.verticalLayout_7.addWidget(self.uv200)

        self.uv1000 = QRadioButton(self.scalebox)
        self.uv1000.setObjectName(u"uv1000")

        self.verticalLayout_7.addWidget(self.uv1000)

        self.uv10000 = QRadioButton(self.scalebox)
        self.uv10000.setObjectName(u"uv10000")

        self.verticalLayout_7.addWidget(self.uv10000)


        self.verticalLayout_20.addWidget(self.scalebox)

        self.verticalLayout_20.setStretch(0, 2)

        self.verticalLayout_14.addLayout(self.verticalLayout_20)


        self.verticalLayout_15.addWidget(self.scale)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_9.addWidget(self.scrollArea)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.cancel = QPushButton(common)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setMinimumSize(QSize(85, 43))
        self.cancel.setStyleSheet(u"background-color: rgb(61, 127, 255);")

        self.horizontalLayout_14.addWidget(self.cancel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)

        self.done = QPushButton(common)
        self.done.setObjectName(u"done")
        self.done.setMinimumSize(QSize(85, 43))
        self.done.setStyleSheet(u"background-color: rgb(48, 171, 195);")

        self.horizontalLayout_14.addWidget(self.done)


        self.verticalLayout_9.addLayout(self.horizontalLayout_14)


        self.retranslateUi(common)

        QMetaObject.connectSlotsByName(common)
    # setupUi

    def retranslateUi(self, common):
        common.setWindowTitle(QCoreApplication.translate("common", u"Form", None))
        self.groupBox_8.setTitle("")
        self.label.setText("")
        self.label_2.setText("")
        self.channel.setTitle("")
        self.label_4.setText(QCoreApplication.translate("common", u"channel:", None))
        self.channel1to64.setTitle("")
        self.c1t8.setText(QCoreApplication.translate("common", u"channel 1-8", None))
        self.c9t16.setText(QCoreApplication.translate("common", u"channel 9-16", None))
        self.c17t24.setText(QCoreApplication.translate("common", u"channel 17-24", None))
        self.c25t32.setText(QCoreApplication.translate("common", u"channel 25-32", None))
        self.c33t40.setText(QCoreApplication.translate("common", u"channel 33-40", None))
        self.c41t48.setText(QCoreApplication.translate("common", u"channel 41-48", None))
        self.c49t56.setText(QCoreApplication.translate("common", u"channel 49-56", None))
        self.c57t64.setText(QCoreApplication.translate("common", u"channel 57-64", None))
        self.channelselect.setTitle("")
        self.c1.setText(QCoreApplication.translate("common", u"channel 1", None))
        self.c2.setText(QCoreApplication.translate("common", u"channel 2", None))
        self.c3.setText(QCoreApplication.translate("common", u"channel 3", None))
        self.c4.setText(QCoreApplication.translate("common", u"channel 4", None))
        self.c5.setText(QCoreApplication.translate("common", u"channel 5", None))
        self.c6.setText(QCoreApplication.translate("common", u"channel 6", None))
        self.c7.setText(QCoreApplication.translate("common", u"channel 7", None))
        self.c8.setText(QCoreApplication.translate("common", u"channel 8", None))
        self.maxfrequency.setTitle("")
        self.label_6.setText(QCoreApplication.translate("common", u"maxfrequency:", None))
        self.maxfrequency_box.setTitle("")
        self.h20.setText(QCoreApplication.translate("common", u"20Hz", None))
        self.h40.setText(QCoreApplication.translate("common", u"40Hz", None))
        self.h60.setText(QCoreApplication.translate("common", u"60Hz", None))
        self.h100.setText(QCoreApplication.translate("common", u"100Hz", None))
        self.h200.setText(QCoreApplication.translate("common", u"200Hz", None))
        self.h500.setText(QCoreApplication.translate("common", u"500Hz", None))
        self.model.setTitle("")
        self.label_8.setText(QCoreApplication.translate("common", u"model:", None))
        self.modelbox.setTitle("")
        self.line.setText(QCoreApplication.translate("common", u"line", None))
        self.log.setText(QCoreApplication.translate("common", u"log", None))
        self.window.setTitle("")
        self.label_10.setText(QCoreApplication.translate("common", u"window:", None))
        self.windowbox.setTitle("")
        self.min1.setText(QCoreApplication.translate("common", u"1 min", None))
        self.min3.setText(QCoreApplication.translate("common", u"3 min", None))
        self.min6.setText(QCoreApplication.translate("common", u"6 min", None))
        self.min15.setText(QCoreApplication.translate("common", u"15 min", None))
        self.min30.setText(QCoreApplication.translate("common", u"30 min", None))
        self.timelength.setTitle("")
        self.label_12.setText(QCoreApplication.translate("common", u"timelength:", None))
        self.timelengthbox.setTitle("")
        self.s1.setText(QCoreApplication.translate("common", u"1 s", None))
        self.s3.setText(QCoreApplication.translate("common", u"3 s", None))
        self.s5.setText(QCoreApplication.translate("common", u"5 s", None))
        self.s10.setText(QCoreApplication.translate("common", u"10 s", None))
        self.s20.setText(QCoreApplication.translate("common", u"20 s", None))
        self.scale.setTitle("")
        self.label_14.setText(QCoreApplication.translate("common", u"scale:", None))
        self.scalebox.setTitle("")
        self.uvauto.setText(QCoreApplication.translate("common", u"auto", None))
        self.uv50.setText(QCoreApplication.translate("common", u"50 uv", None))
        self.uv100.setText(QCoreApplication.translate("common", u"100 uv", None))
        self.uv200.setText(QCoreApplication.translate("common", u"200 uv", None))
        self.uv1000.setText(QCoreApplication.translate("common", u"1000 uv", None))
        self.uv10000.setText(QCoreApplication.translate("common", u"10000 uv", None))
        self.cancel.setText(QCoreApplication.translate("common", u"\u53d6\u6d88", None))
        self.done.setText(QCoreApplication.translate("common", u"\u786e\u5b9a", None))
    # retranslateUi

