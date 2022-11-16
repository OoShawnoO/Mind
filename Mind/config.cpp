#include "config.h"
#include "ui_config.h"

config::config(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::config)
{
    ui->setupUi(this);
    con = nullptr;
    connect(ui->start,&QPushButton::clicked,this,[=](){
        con = new configure;
        con->retTime = ui->retTime->text().toStdString();
        con->ipAddress = ui->ipAddress->text().toStdString();
        if(ui->c8->isChecked()){
            con->channel = 8;
        }else if(ui->c16->isChecked()){
            con->channel = 16;
        }else if(ui->c32->isChecked()){
            con->channel = 32;
        }else if(ui->c64->isChecked()){
            con->channel = 65;
        }else{

        }
        if(ui->h20->isChecked()){
            con->frequency = 20;
        }else if(ui->h20->isChecked()){
            con->frequency = 40;
        }else{

        }
        emit start();
    });
    connect(ui->cancel,&QPushButton::clicked,this,[=](){
        emit cancel();
    });
}

config::~config()
{
    delete ui;
}

configure config::data(){
    return *con;
}
