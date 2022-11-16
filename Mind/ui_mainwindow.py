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

from common import common
from layout import Layout

import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1174, 785)
        MainWindow.setStyleSheet(u"#centralwidget{background-color:rgb(11,28,84)}\n"
"\n"
"*{color:rgb(255,255,255)}\n"
"\n"
"#groupBox_3{background-color:rgb(14, 49, 117)}\n"
"#groupBox{background-color: rgb(14, 49, 117)}\n"
"#groupBox_2{\n"
"}\n"
"#configtable{\n"
"	background-color:rgb(14, 49, 117);\n"
"}\n"
"QPushButton{\n"
"	border:none;\n"
"}\n"
"QGroupBox{\n"
"	border:none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"#groupBox_4 {background-color: rgb(37, 74, 146)}\n"
"#groupBox_4>QPushButton{background-color: rgb(37, 74, 146)}")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.hwselect = QPushButton(self.groupBox_4)
        self.hwselect.setObjectName(u"hwselect")
        self.hwselect.setMinimumSize(QSize(100, 45))
        self.hwselect.setMaximumSize(QSize(100, 45))
        self.hwselect.setStyleSheet(u"background-color: rgb(37, 74, 146);\n"
"border:1px solid rgb(0,0,0);\n"
"margin-left:10px;")
        self.hwselect.setFlat(False)

        self.horizontalLayout_6.addWidget(self.hwselect)

        self.horizontalSpacer = QSpacerItem(372, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.hardwaresetting = QPushButton(self.groupBox_4)
        self.hardwaresetting.setObjectName(u"hardwaresetting")
        self.hardwaresetting.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/res/hardwaresetting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hardwaresetting.setIcon(icon)
        self.hardwaresetting.setIconSize(QSize(182, 45))
        self.hardwaresetting.setFlat(True)

        self.horizontalLayout_6.addWidget(self.hardwaresetting)

        self.pushButton_2 = QPushButton(self.groupBox_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/res/update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(108, 45))
        self.pushButton_2.setFlat(True)

        self.horizontalLayout_6.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.groupBox_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/res/shop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(92, 45))
        self.pushButton_3.setFlat(True)

        self.horizontalLayout_6.addWidget(self.pushButton_3)

        self.pushButton_8 = QPushButton(self.groupBox_4)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/res/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QSize(87, 45))
        self.pushButton_8.setFlat(True)

        self.horizontalLayout_6.addWidget(self.pushButton_8)

        self.label_12 = QLabel(self.groupBox_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setPixmap(QPixmap(u":/res/rectangle.png"))

        self.horizontalLayout_6.addWidget(self.label_12)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)


        self.verticalLayout_5.addWidget(self.groupBox_4)

        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        self.horizontalLayout = QHBoxLayout(self.main)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(self.main)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(43, 0))
        self.label.setMaximumSize(QSize(82, 16777215))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(90, 0))
        self.comboBox.setMaximumSize(QSize(90, 16777215))
        self.comboBox.setStyleSheet(u"color:rgb(112, 112, 112);\n"
"")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.all = QPushButton(self.groupBox)
        self.all.setObjectName(u"all")
        self.all.setMinimumSize(QSize(90, 0))
        self.all.setMaximumSize(QSize(90, 16777215))
        self.all.setStyleSheet(u"background-color: rgb(48, 171, 195);\n"
"padding:4px;")

        self.gridLayout.addWidget(self.all, 0, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setMinimumSize(QSize(43, 0))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(90, 0))
        self.lineEdit.setMaximumSize(QSize(90, 16777215))
        self.lineEdit.setStyleSheet(u"color:rgb(94, 94, 94)")

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(90, 0))
        self.lineEdit_2.setMaximumSize(QSize(90, 16777215))
        self.lineEdit_2.setStyleSheet(u"color:rgb(94, 94, 94)")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.configs = QPushButton(self.groupBox)
        self.configs.setObjectName(u"configs")
        self.configs.setMinimumSize(QSize(0, 27))
        self.configs.setStyleSheet(u"padding-right:150px;")
        self.configs.setFlat(True)

        self.horizontalLayout_13.addWidget(self.configs, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(15, 15))
        self.label_13.setPixmap(QPixmap(u":/res/right.png"))
        self.label_13.setScaledContents(True)

        self.horizontalLayout_13.addWidget(self.label_13, 0, Qt.AlignRight)

        self.horizontalLayout_13.setStretch(0, 10)
        self.horizontalLayout_13.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.pushButton_6 = QPushButton(self.groupBox)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 40))
        self.pushButton_6.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton_6.setStyleSheet(u"background-color: rgb(57,114,224);")
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton_6)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)

        self.verticalLayout_4.addWidget(self.groupBox)

        self.configtable = QGroupBox(self.widget)
        self.configtable.setObjectName(u"configtable")
        self.configtable.setStyleSheet(u"QCheckBox::indicator:unchecked{\n"
"	background-color:rgb(255, 255, 255);\n"
"}\n"
"QCheckBox::indicator{\n"
"	margin:4px\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.configtable)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.configtable)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMinimumSize(QSize(360, 0))
        self.scrollArea.setStyleSheet(u"background-color:rgb(14,49,117);")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 358, 564))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.timeserise = QCheckBox(self.scrollAreaWidgetContents)
        self.timeserise.setObjectName(u"timeserise")
        sizePolicy1.setHeightForWidth(self.timeserise.sizePolicy().hasHeightForWidth())
        self.timeserise.setSizePolicy(sizePolicy1)
        self.timeserise.setMinimumSize(QSize(256, 48))
        self.timeserise.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.timeserise, 0, Qt.AlignLeft)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(16)
        sizePolicy2.setVerticalStretch(16)
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMinimumSize(QSize(14, 14))
        self.label_5.setMaximumSize(QSize(14, 14))
        self.label_5.setPixmap(QPixmap(u":/res/right.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_5, 0, Qt.AlignRight)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.timeserieswid = common(self.scrollAreaWidgetContents)
        self.timeserieswid.setObjectName(u"timeserieswid")

        self.verticalLayout_2.addWidget(self.timeserieswid)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777214, 1))
        self.line.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.fft = QCheckBox(self.scrollAreaWidgetContents)
        self.fft.setObjectName(u"fft")
        sizePolicy1.setHeightForWidth(self.fft.sizePolicy().hasHeightForWidth())
        self.fft.setSizePolicy(sizePolicy1)
        self.fft.setMinimumSize(QSize(256, 48))
        self.fft.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.fft, 0, Qt.AlignLeft)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setMinimumSize(QSize(14, 14))
        self.label_6.setMaximumSize(QSize(14, 14))
        self.label_6.setPixmap(QPixmap(u":/res/right.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_6, 0, Qt.AlignRight)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.fftwid = common(self.scrollAreaWidgetContents)
        self.fftwid.setObjectName(u"fftwid")

        self.verticalLayout_2.addWidget(self.fftwid)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMaximumSize(QSize(16777215, 1))
        self.line_2.setStyleSheet(u"background-color:rgb(255,255,255);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.headplot = QCheckBox(self.scrollAreaWidgetContents)
        self.headplot.setObjectName(u"headplot")
        sizePolicy1.setHeightForWidth(self.headplot.sizePolicy().hasHeightForWidth())
        self.headplot.setSizePolicy(sizePolicy1)
        self.headplot.setMinimumSize(QSize(256, 48))
        self.headplot.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.headplot, 0, Qt.AlignLeft)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setMinimumSize(QSize(14, 14))
        self.label_7.setMaximumSize(QSize(14, 14))
        self.label_7.setPixmap(QPixmap(u":/res/right.png"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_7, 0, Qt.AlignRight)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.headplotwid = QWidget(self.scrollAreaWidgetContents)
        self.headplotwid.setObjectName(u"headplotwid")

        self.verticalLayout_2.addWidget(self.headplotwid)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMaximumSize(QSize(16777215, 1))
        self.line_3.setStyleSheet(u"background-color:rgb(255,255,255);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.sepectom = QCheckBox(self.scrollAreaWidgetContents)
        self.sepectom.setObjectName(u"sepectom")
        sizePolicy1.setHeightForWidth(self.sepectom.sizePolicy().hasHeightForWidth())
        self.sepectom.setSizePolicy(sizePolicy1)
        self.sepectom.setMinimumSize(QSize(256, 48))
        self.sepectom.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.sepectom, 0, Qt.AlignLeft)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setMinimumSize(QSize(14, 14))
        self.label_10.setMaximumSize(QSize(14, 14))
        self.label_10.setPixmap(QPixmap(u":/res/right.png"))
        self.label_10.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_10, 0, Qt.AlignRight)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.sepectomwid = common(self.scrollAreaWidgetContents)
        self.sepectomwid.setObjectName(u"sepectomwid")

        self.verticalLayout_2.addWidget(self.sepectomwid)

        self.line_5 = QFrame(self.scrollAreaWidgetContents)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMaximumSize(QSize(16777215, 1))
        self.line_5.setStyleSheet(u"background-color:rgb(255,255,255);")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.signal = QCheckBox(self.scrollAreaWidgetContents)
        self.signal.setObjectName(u"signal")
        sizePolicy1.setHeightForWidth(self.signal.sizePolicy().hasHeightForWidth())
        self.signal.setSizePolicy(sizePolicy1)
        self.signal.setMinimumSize(QSize(256, 48))
        self.signal.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.signal, 0, Qt.AlignLeft)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setMinimumSize(QSize(14, 14))
        self.label_9.setMaximumSize(QSize(14, 14))
        self.label_9.setPixmap(QPixmap(u":/res/right.png"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_9, 0, Qt.AlignRight)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.signalwid = QWidget(self.scrollAreaWidgetContents)
        self.signalwid.setObjectName(u"signalwid")

        self.verticalLayout_2.addWidget(self.signalwid)

        self.line_6 = QFrame(self.scrollAreaWidgetContents)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setMaximumSize(QSize(16777215, 1))
        self.line_6.setStyleSheet(u"background-color:rgb(255,255,255);")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.networking = QCheckBox(self.scrollAreaWidgetContents)
        self.networking.setObjectName(u"networking")
        sizePolicy1.setHeightForWidth(self.networking.sizePolicy().hasHeightForWidth())
        self.networking.setSizePolicy(sizePolicy1)
        self.networking.setMinimumSize(QSize(256, 48))
        self.networking.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.networking, 0, Qt.AlignLeft)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setMinimumSize(QSize(14, 14))
        self.label_8.setMaximumSize(QSize(14, 14))
        self.label_8.setPixmap(QPixmap(u":/res/right.png"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_8, 0, Qt.AlignRight)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.networkingwid = QWidget(self.scrollAreaWidgetContents)
        self.networkingwid.setObjectName(u"networkingwid")

        self.verticalLayout_2.addWidget(self.networkingwid)

        self.line_7 = QFrame(self.scrollAreaWidgetContents)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setMaximumSize(QSize(16777215, 1))
        self.line_7.setStyleSheet(u"background-color:rgb(255,255,255);")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_7)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.custom = QCheckBox(self.scrollAreaWidgetContents)
        self.custom.setObjectName(u"custom")
        sizePolicy1.setHeightForWidth(self.custom.sizePolicy().hasHeightForWidth())
        self.custom.setSizePolicy(sizePolicy1)
        self.custom.setMinimumSize(QSize(256, 48))
        self.custom.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.custom, 0, Qt.AlignLeft)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setMinimumSize(QSize(14, 14))
        self.label_11.setMaximumSize(QSize(14, 14))
        self.label_11.setPixmap(QPixmap(u":/res/right.png"))
        self.label_11.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_11, 0, Qt.AlignRight)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.customwid = QWidget(self.scrollAreaWidgetContents)
        self.customwid.setObjectName(u"customwid")

        self.verticalLayout_2.addWidget(self.customwid)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)

        self.close = QPushButton(self.configtable)
        self.close.setObjectName(u"close")
        self.close.setMinimumSize(QSize(0, 50))
        self.close.setStyleSheet(u"background-color: rgb(57,114,224);")

        self.verticalLayout_6.addWidget(self.close)


        self.verticalLayout_4.addWidget(self.configtable)

        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 8)

        self.horizontalLayout.addWidget(self.widget)

        self.groupBox_5 = QGroupBox(self.main)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.mindbridge = QGroupBox(self.groupBox_5)
        self.mindbridge.setObjectName(u"mindbridge")
        self.mindbridge.setMinimumSize(QSize(0, 58))
        self.mindbridge.setMaximumSize(QSize(16777215, 58))
        self.mindbridge.setStyleSheet(u"background-color: rgb(14, 49, 117);")
        self.mindbridge.setFlat(False)
        self.horizontalLayout_5 = QHBoxLayout(self.mindbridge)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 9)
        self.label_3 = QLabel(self.mindbridge)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.mindbridge)

        self.chart = Layout(self.groupBox_5)
        self.chart.setObjectName(u"chart")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.chart.sizePolicy().hasHeightForWidth())
        self.chart.setSizePolicy(sizePolicy3)
        self.chart.setMinimumSize(QSize(816, 600))

        self.verticalLayout_3.addWidget(self.chart)


        self.horizontalLayout.addWidget(self.groupBox_5)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 6)

        self.verticalLayout_5.addWidget(self.main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_6.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_4.setTitle("")
        self.hwselect.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u786c\u4ef6", None))
        self.hardwaresetting.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_8.setText("")
        self.label_12.setText("")
        self.label_4.setText("")
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"filter:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"50Hz", None))

        self.all.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.label_2.setText("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"5Hz", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"10Hz", None))
        self.configs.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u9879", None))
        self.label_13.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb/\u7ed3\u675f", None))
        self.configtable.setTitle("")
        self.timeserise.setText(QCoreApplication.translate("MainWindow", u"timeserise                      ", None))
        self.label_5.setText("")
        self.fft.setText(QCoreApplication.translate("MainWindow", u"fft                                     ", None))
        self.label_6.setText("")
        self.headplot.setText(QCoreApplication.translate("MainWindow", u"headplot                            ", None))
        self.label_7.setText("")
        self.sepectom.setText(QCoreApplication.translate("MainWindow", u"sepectom                        ", None))
        self.label_10.setText("")
        self.signal.setText(QCoreApplication.translate("MainWindow", u"signal                               ", None))
        self.label_9.setText("")
        self.networking.setText(QCoreApplication.translate("MainWindow", u"networking                      ", None))
        self.label_8.setText("")
        self.custom.setText(QCoreApplication.translate("MainWindow", u"custom                           ", None))
        self.label_11.setText("")
        self.close.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u5b9e\u9a8c", None))
        self.groupBox_5.setTitle("")
        self.mindbridge.setTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Mindbrige brain stream chart", None))
    # retranslateUi

