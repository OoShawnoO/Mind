#include "signal.h"
#include "ui_signal.h"

signal::signal(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::signal)
{
    ui->setupUi(this);
}

signal::~signal()
{
    delete ui;
}
