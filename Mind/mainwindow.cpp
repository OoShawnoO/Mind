#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDebug>



/*


* Title           /
                    headsetting.cpp
                    arrowwidget.cpp

* Body            /

                    * Filter          /
                                        allbox.cpp

                    * ConfigureTable  /
                                        common.cpp
                                        config.cpp

                    * Chart           /
                                        layout.cpp
                                        * lsl.cpp     /
                                                        switchbutton.cpp
                                        signal.cpp
                                        layout.cpp
*/


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent),
      ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    conf = new configure;
    allBox = nullptr;
    headSetting = nullptr;
    Lsl = new lsl();

//    ui->chart->AddWidget(dynamic_cast<QWidget*>(Lsl));
    Signal = new class signal();
    /* 屏幕0.8x*/
    QScreen *screen = qApp->primaryScreen();
    int nWidth = screen->size().width();
    int nHeight = screen->size().height();
    this->setGeometry(nWidth*0.1,nHeight*0.1,nWidth*0.8,nHeight*0.8);


    /* Title */

    connect(ui->hardwaresetting,&QPushButton::clicked,[=](){
        if(!headSetting){
            headSetting = new headsetting(this);
        }
        headSetting->show();
    });
    /* Title hardware select */
    /* 硬件选择 */
    ArrowWidget* hardwareWid = new ArrowWidget(this);
    class hwselect* hws = new class hwselect();
    hardwareWid->setWidget(hws);
    hardwareWid->setStartPos(20);
    hardwareWid->setTriangleInfo(30,10);
    hardwareWid->setDerection(ArrowWidget::up);
    hardwareWid->setGeometry(ui->hwselect->x(),30+ui->hwselect->y()+(int)(ui->hwselect->height()),hardwareWid->width(),hardwareWid->height());
    hardwareWid->hide();
    connect(ui->hwselect,&QPushButton::clicked,[=](){
        if(hardwareWid->isHidden()){
            hardwareWid->show();
        }else{
            hardwareWid->hide();
        }
    });
    /* Title config */
    /* 不同硬件对应config */
    for(auto btn : hws->get_btns()){
        ArrowWidget* configWid = new ArrowWidget(this,QColor(CONFIG_BACKGROUNDCOLOR));
        arrows.push_back(configWid);
        config* con = new class config();
        /* 绑定用户进入实验按钮,数据处理完成发送的start信号 */
        connect(con,&config::start,[=](){
            /* 接收config 用户选择的数据 */
            *conf = con->data();
            conf->hardwareName = btn->text().toStdString();
            hardwareWid->hide();
            emit con->cancel();
            ui->sepectomwid->setConfig(conf);
            ui->fftwid->setConfig(conf);
            ui->timeserieswid->setConfig(conf);
            ui->main->show();
        });
        configWid->setWidget(con);
        configWid->setStartPos(90);
        configWid->setTriangleInfo(30,10);
        configWid->setDerection(ArrowWidget::left);
        configWid->hide();
        connect(btn,&QPushButton::clicked,[=](){
            if(configWid->isHidden()){
                for(auto arrow : arrows){arrow->hide();}
                configWid->setGeometry(btn->x()+btn->width()+30,btn->y(),configWid->width(),configWid->height());
                configWid->show();
                configWid->raise();
            }else{
                configWid->hide();
            }
        });
    }

    /* Body */
    /* 设置主界面隐藏占位 */
    QSizePolicy qp = ui->main->sizePolicy();
    qp.setRetainSizeWhenHidden(true);
    ui->main->setSizePolicy(qp);
    ui->main->hide();

    /* Body Filter */
    /* 绑定all按钮 */
    connect(ui->all,&QPushButton::clicked,[=](){
        if(!allBox){
            allBox = new allbox(this);
        }
        allBox->show();
    });

    /* Body ConfigureTable */
    /* 设置配置项菜单栏隐藏占位 */
    QSizePolicy q = ui->configtable->sizePolicy();
    q.setRetainSizeWhenHidden(true);
    ui->configtable->setSizePolicy(q);
    ui->configtable->hide();

    /* 绑定配置项显示配置项菜单栏*/
    connect(ui->configs,&QPushButton::clicked,[=](){
       if(ui->configtable->isHidden()){
           ui->configtable->show();
       }else{
           ui->configtable->hide();
       }
    });

    /* Body Chart */
    /* 设置窗口平铺 */
    widNum = 0;
    QWidget* test1 = new lsl();
    QWidget* test2 = new signal();
    QWidget* test3 = new lsl();
    QWidget* test4 = new lsl();
    QWidget* test5 = new signal();
    connectCheckBox(ui->signal,Signal);
    connectCheckBox(ui->fft,test1);
    connectCheckBox(ui->headplot,test2);
    connectCheckBox(ui->networking,Lsl);
    connectCheckBox(ui->timeserise,test3);
    connectCheckBox(ui->sepectom,test4);
    connectCheckBox(ui->custom,test5);



    /* 侧边菜单栏的抽屉式widget初始化 */
    ui->sepectomwid->setType(SPECTROGRAM);
    ui->sepectomwid->hide();
    ui->fftwid->setType(FFT);
    ui->fftwid->hide();
    ui->timeserieswid->setType(TIMESRISE);
    ui->timeserieswid->hide();

    /* sepectom按钮展开widget */
    connect(ui->sepectomBtn,&QPushButton::clicked,ui->configtable,[=](){
        if(ui->sepectomwid->isHidden()){
            ui->sepectomwid->show();
        }else{
            ui->sepectomwid->hide();
        }
    });
    /* fft按钮展开widget*/
    connect(ui->fftBtn,&QPushButton::clicked,ui->configtable,[=](){
        if(ui->fftwid->isHidden()){
            ui->fftwid->show();
        }else{
            ui->fftwid->hide();
        }
    });
    /* timseries按钮展开widget*/
    connect(ui->timeseriseBtn,&QPushButton::clicked,ui->configtable,[=](){
        if(ui->timeserieswid->isHidden()){
            ui->timeserieswid->show();
        }else{
            ui->timeserieswid->hide();
        }
    });
    /* custom按钮展开widget */


    /* 绑定退出实验 */
    connect(ui->close,&QPushButton::clicked,[=](){exit(0);});
    ui->customwid->hide();
    ui->sepectomwid->hide();
    ui->networkingwid->hide();
    ui->signalwid->hide();
    ui->timeserieswid->hide();
    ui->fftwid->hide();
    ui->headplotwid->hide();

}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::connectCheckBox(QCheckBox *checkbox, QWidget *widget)
{
    connect(checkbox,&QCheckBox::stateChanged,this,[=](int state){
       checkbox->setCheckable(true);
       if(state == Qt::Checked){
           if(ui->chart->AddWidget(widget)){
              checkbox->setChecked(true);
           }else{
               checkbox->setCheckable(false);
               checkbox->setChecked(false);

           }
       }else if(state == Qt::Unchecked){
           ui->chart->RemoveWidget(widget);
           checkbox->setChecked(false);
       }else{
           checkbox->setChecked(false);
       }
    });
}

