#include "headsetting.h"
#include "ui_headsetting.h"

headsetting::headsetting(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::headsetting)
{
    ui->setupUi(this);
    ret = new headsettingRet;
    currentIdx = 0;
    changeBtns[0] = ui->b1t8;
    changeBtns[1] = ui->b9t16;
    changeBtns[2] = ui->b17t24;
    changeBtns[3] = ui->b25t32;
    changeBtns[4] = ui->b33t40;
    changeBtns[5] = ui->b41t48;
    changeBtns[6] = ui->b49t56;
    changeBtns[7] = ui->b57t64;

    pga[0] = ui->pga1;
    pga[1] = ui->pga2;
    pga[2] = ui->pga3;
    pga[3] = ui->pga4;
    pga[4] = ui->pga5;
    pga[5] = ui->pga6;
    pga[6] = ui->pga7;
    pga[7] = ui->pga8;

    input[0] = ui->input1;
    input[1] = ui->input2;
    input[2] = ui->input3;
    input[3] = ui->input4;
    input[4] = ui->input5;
    input[5] = ui->input6;
    input[6] = ui->input7;
    input[7] = ui->input8;

    bias[0] = ui->bias1;
    bias[1] = ui->bias2;
    bias[2] = ui->bias3;
    bias[3] = ui->bias4;
    bias[4] = ui->bias5;
    bias[5] = ui->bias6;
    bias[6] = ui->bias7;
    bias[7] = ui->bias8;

    srb2[0] = ui->srb21;
    srb2[1] = ui->srb22;
    srb2[2] = ui->srb23;
    srb2[3] = ui->srb24;
    srb2[4] = ui->srb25;
    srb2[5] = ui->srb26;
    srb2[6] = ui->srb27;
    srb2[7] = ui->srb28;

    srb1[0] = ui->srb11;
    srb1[1] = ui->srb12;
    srb1[2] = ui->srb13;
    srb1[3] = ui->srb14;
    srb1[4] = ui->srb15;
    srb1[5] = ui->srb16;
    srb1[6] = ui->srb17;
    srb1[7] = ui->srb18;

    saved = false;

    connect(ui->save,&QPushButton::clicked,[=](){
        for(int i=0;i<8;i++){
            ret->pga[i+currentIdx*8] = pga[i]->currentText().toStdString();
            ret->bias[i+currentIdx*8] = bias[i]->currentText() == "Yes" ? true : false;
            ret->input[i+currentIdx*8] = input[i]->currentText().toStdString();
            ret->srb2[i+currentIdx*8] = srb2[i]->currentText() == "On" ? true : false;
            ret->srb1[i+currentIdx*8] = srb1[i]->currentText() == "On" ? true : false;
        }
        saved = true;
        emit save();
    });
    connect(ui->load,&QPushButton::clicked,[=](){
        if(!saved){
            for(int i=0;i<8;i++){
                ret->pga[i+currentIdx*8] = pga[i]->currentText().toStdString();
                ret->bias[i+currentIdx*8] = bias[i]->currentText() == "Yes" ? true : false;
                ret->input[i+currentIdx*8] = input[i]->currentText().toStdString();
                ret->srb2[i+currentIdx*8] = srb2[i]->currentText() == "On" ? true : false;
                ret->srb1[i+currentIdx*8] = srb1[i]->currentText() == "On" ? true : false;
            }
        }
        this->hide();
        emit load();
    });
    connect(ui->reset,&QPushButton::clicked,[=](){
        for(auto combo:ui->groupBox->findChildren<QComboBox*>()){
            combo->setCurrentIndex(0);
        }
        saved = false;
        emit reset();
    });

    for(int i=0;i<8;i++){
        connect(changeBtns[i],&QPushButton::clicked,[=](){
            ui->l1->setText(to_string(i*8+1).c_str());
            ui->l2->setText(to_string(i*8+2).c_str());
            ui->l3->setText(to_string(i*8+3).c_str());
            ui->l4->setText(to_string(i*8+4).c_str());
            ui->l5->setText(to_string(i*8+5).c_str());
            ui->l6->setText(to_string(i*8+6).c_str());
            ui->l7->setText(to_string(i*8+7).c_str());
            ui->l8->setText(to_string(i*8+8).c_str());
            currentIdx = i;
        });
    }
}

headsetting::~headsetting()
{
    delete ui;
}
