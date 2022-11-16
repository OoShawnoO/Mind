#include "hwselect.h"
#include "ui_hwselect.h"

hwselect::hwselect(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::hwselect)
{
    ui->setupUi(this);
}

hwselect::~hwselect()
{
    delete ui;
}

vector<QPushButton*> hwselect::get_btns(){
    vector<QPushButton*> btns;
    btns.push_back(ui->pushButton);
    btns.push_back(ui->pushButton_2);
    return btns;
}
