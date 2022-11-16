QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++11

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    allbox.cpp \
    arrowwidget.cpp \
    common.cpp \
    config.cpp \
    headsetting.cpp \
    hwselect.cpp \
    layout.cpp \
    lsl.cpp \
    main.cpp \
    mainwindow.cpp \
    signal.cpp \
    switchbutton.cpp

HEADERS += \
    allbox.h \
    arrowwidget.h \
    common.h \
    config.h \
    headsetting.h \
    hwselect.h \
    layout.h \
    lsl.h \
    mainwindow.h \
    signal.h \
    switchbutton.h \
    utils.h

FORMS += \
    allbox.ui \
    common.ui \
    config.ui \
    headsetting.ui \
    hwselect.ui \
    layout.ui \
    lsl.ui \
    mainwindow.ui \
    signal.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

RESOURCES += \
    res.qrc
