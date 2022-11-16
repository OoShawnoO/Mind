#include "common.h"
#include "ui_common.h"
#include <QDebug>

common::common(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::common)
{
    ui->setupUi(this);
    channelBox[0] = ui->c1t8;
    channelBox[1] = ui->c9t16;
    channelBox[2] = ui->c17t24;
    channelBox[3] = ui->c25t32;
    channelBox[4] = ui->c33t40;
    channelBox[5] = ui->c41t48;
    channelBox[6] = ui->c49t56;
    channelBox[7] = ui->c57t64;

    channelSelectBox[0] = ui->c1;
    channelSelectBox[1] = ui->c2;
    channelSelectBox[2] = ui->c3;
    channelSelectBox[3] = ui->c4;
    channelSelectBox[4] = ui->c5;
    channelSelectBox[5] = ui->c6;
    channelSelectBox[6] = ui->c7;
    channelSelectBox[7] = ui->c8;
    ret = new commonRet;
    for(int i=0;i<8;i++){
        connect(channelBox[i],&QCheckBox::toggled,this,[=](){
            for(int j=0;j<8;j++){
                channelSelectBox[j]->setText((string("channel ")+to_string(8*i+j+1)).c_str());
                if(!ret->channel[8*i+j]){
                    channelSelectBox[j]->setCheckState(Qt::Unchecked);
                }else{
                    channelSelectBox[j]->setCheckState(Qt::Checked);
                }
            }
        });
    }

    for(int i=0;i<8;i++){
        connect(channelSelectBox[i],&QCheckBox::toggled,this,[=](){
           ret->channel[atoi(channelSelectBox[i]->text().split(" ")[1].toUtf8())-1] = true;
        });
        connect(channelSelectBox[i],&QCheckBox::stateChanged,this,[=](int state){
            if(state == Qt::Unchecked){
                ret->channel[atoi(channelSelectBox[i]->text().split(" ")[1].toUtf8())-1] = false;
            }
        });
    }

    connect(ui->done,&QPushButton::clicked,this,[=](){
        if(ui->maxfrequency->isVisible()){
            if(ui->h20->isChecked()) ret->maxFrequency=20;
            else if(ui->h40->isChecked()) ret->maxFrequency=40;
            else if(ui->h60->isChecked()) ret->maxFrequency=60;
            else if(ui->h100->isChecked()) ret->maxFrequency=100;
            else if(ui->h200->isChecked()) ret->maxFrequency=200;
            else if(ui->h500->isChecked()) ret->maxFrequency=500;
            else{ret->maxFrequency = 20;}
        }
        if(ui->window->isVisible()){
            if(ui->min1->isChecked()) ret->windows = 1;
            else if(ui->min3->isChecked()) ret->windows =3 ;
            else if(ui->min6->isChecked()) ret->windows =6 ;
            else if(ui->min15->isChecked()) ret->windows =15 ;
            else if(ui->min30->isChecked()) ret->windows =30 ;
            else{
                ret->windows = 1;
            }
        }
        if(ui->model->isVisible()){
            if(ui->line->isChecked()) ret->model = "line";
            else if(ui->log->isChecked()) ret->model = "log";
            else{
                ret->model = "line";
            }
        }
        if(ui->timelength->isVisible()){
            if(ui->s1->isChecked()) ret->timeLength = 1;
            else if(ui->s3->isChecked()) ret->timeLength = 3;
            else if(ui->s5->isChecked()) ret->timeLength = 5;
            else if(ui->s10->isChecked()) ret->timeLength = 10;
            else if(ui->s20->isChecked()) ret->timeLength = 20;
            else{
                ret->timeLength = 1;
            }
        }
        if(ui->scale->isVisible()){
            if(ui->uvauto->isChecked()) ret->scale = 0;
            else if(ui->uv50->isChecked()) ret->scale = 50;
            else if(ui->uv100->isChecked()) ret->scale = 100;
            else if(ui->uv200->isChecked()) ret->scale = 200;
            else if(ui->uv1000->isChecked()) ret->scale = 1000;
            else if(ui->uv10000->isChecked()) ret->scale = 10000;
            else{
                ret->scale = 0;
            }
        }
        emit done();
    });
    connect(ui->cancel,&QPushButton::clicked,this,[=](){
        delete ret;
        ret = new commonRet();
        this->hide();
        emit cancel();
    });
}

void common::setType(WidType type){
    switch(type){
    case SPECTROGRAM:{
        ui->scale->setVisible(false);
        ui->timelength->setVisible(false);
        ui->label->setText("spectrogram");
        break;
    }
    case FFT:{
        ui->scale->setVisible(false);
        ui->timelength->setVisible(false);
        ui->window->setVisible(false);
        ui->label->setText("fft");
        break;
    }
    case TIMESRISE:{
        ui->window->setVisible(false);
        ui->maxfrequency->setVisible(false);
        ui->model->setVisible(false);
        ui->label->setText("timeseries");
        break;
    }
    case BANDPOW:{}
        ui->window->setVisible(false);
        ui->maxfrequency->setVisible(false);
        ui->scale->setVisible(false);
        ui->timelength->setVisible(false);
        ui->label->setText("bandpow");
        break;
    }
}

/*
struct configure{
    string retTime;
    string ipAddress;
    int frequency;
    int channel;
};
*/
void common::setConfig(configure *con){
    switch(con->channel){
        case 8 : {
            ui->channelselect->setVisible(true);
            ui->channel1to64->setVisible(false);
            break;
        }
        case 16 : {
            ui->channel1to64->setVisible(true);
            ui->c1t8->setEnabled(true);
            ui->c9t16->setEnabled(true);
            ui->c17t24->setDisabled(true);
            ui->c25t32->setDisabled(true);
            ui->c33t40->setDisabled(true);
            ui->c41t48->setDisabled(true);
            ui->c49t56->setDisabled(true);
            ui->c57t64->setDisabled(true);
            ui->label_2->setText("(16/64)");
            break;
        }
        case 32 : {
            ui->channel1to64->setVisible(true);
            ui->c1t8->setEnabled(true);
            ui->c9t16->setEnabled(true);
            ui->c17t24->setEnabled(true);
            ui->c25t32->setEnabled(true);
            ui->c9t16->setEnabled(true);
            ui->c9t16->setEnabled(true);
            ui->c33t40->setDisabled(true);
            ui->c41t48->setDisabled(true);
            ui->c49t56->setDisabled(true);
            ui->c57t64->setDisabled(true);
            ui->label_2->setText("(32/64)");
            break;
        }
        case 64 : {
            ui->channel1to64->setVisible(true);
            ui->c1t8->setEnabled(true);
            ui->c9t16->setEnabled(true);
            ui->c17t24->setEnabled(true);
            ui->c25t32->setEnabled(true);
            ui->c33t40->setEnabled(true);
            ui->c41t48->setEnabled(true);
            ui->c49t56->setEnabled(true);
            ui->c57t64->setEnabled(true);
            ui->label_2->setText("(64/64)");
            break;
        }
        default : {
            ui->channelselect->setVisible(true);
            ui->channel1to64->setVisible(false);
            break;
        }
    }
}

common::~common()
{
    delete ui;
}

commonRet common::data(){
    return *ret;
}
