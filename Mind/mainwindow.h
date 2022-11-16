#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QDebug>
#include <arrowwidget.h>
#include <utils.h>
#include <allbox.h>
#include <lsl.h>
#include <common.h>
#include <signal.h>
#include <QMdiSubWindow>
#include <QScreen>
#include <headsetting.h>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    friend class scalerlabel;
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    void connectCheckBox(QCheckBox* checkbox,QWidget* widget);
private:
    Ui::MainWindow *ui;
    configure* conf;
    allbox* allBox;
    lsl* Lsl;
    class signal* Signal;
    headsetting* headSetting;
    vector<ArrowWidget*> arrows;
};
#endif // MAINWINDOW_H
