#include "allbox.h"
#include "ui_allbox.h"

allbox::allbox(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::allbox)
{
    ui->setupUi(this);
    ret = new allRet;
    connect(ui->save,&QPushButton::clicked,[=](){
        ret->filter = ui->filter->currentText().toStdString();
        ret->notch = ui->notch->currentText().toStdString();
        ret->start = ui->start->text().toDouble();
        ret->stop = ui->stop->text().toDouble();
        ret->type = ui->type->currentText().toStdString();
        ret->order = ui->order->currentText().toInt();
        emit save();
    });
    connect(ui->load,&QPushButton::clicked,[=](){
        ret->filter = ui->filter->currentText().toStdString();
        ret->notch = ui->notch->currentText().toStdString();
        ret->start = ui->start->text().toDouble();
        ret->stop = ui->stop->text().toDouble();
        ret->type = ui->type->currentText().toStdString();
        ret->order = ui->order->currentText().toInt();
        emit load();
        this->hide();
    });
    connect(ui->reset,&QPushButton::clicked,[=](){
        ui->filter->setCurrentIndex(0);
        ui->notch->setCurrentIndex(0);
        ui->start->setText("5.0");
        ui->stop->setText("50.0");
        ui->type->setCurrentIndex(0);
        ui->order->setCurrentIndex(0);
        emit reset();
    });
}

allbox::~allbox()
{
    delete ui;
}

allRet allbox::data()
{
    return *ret;
}
