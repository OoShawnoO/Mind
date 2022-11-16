#include "layout.h"
#include "ui_layout.h"
#include <lsl.h>
#include <signal.h>
Layout::Layout(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Layout)
{
    ui->setupUi(this);
    contentNum = 0;
    widgets[0] = ui->w1;
    widgets[1] = ui->w2;
    widgets[2] = ui->w3;
    widgets[3] = ui->w4;

    ParentToWidget[ui->w1] = nullptr;
    ParentToWidget[ui->w2] = nullptr;
    ParentToWidget[ui->w3] = nullptr;
    ParentToWidget[ui->w4] = nullptr;
    ParentToVbox[ui->w1] = ui->v1;
    ParentToVbox[ui->w2] = ui->v2;
    ParentToVbox[ui->w3] = ui->v3;
    ParentToVbox[ui->w4] = ui->v4;

    ui->w1->hide();
    ui->w2->hide();
    ui->w3->hide();
    ui->w4->hide();
}
Layout::~Layout()
{
    delete ui;
}

bool Layout::AddWidget(QWidget* widget){
    if(contentNum == 0){
        widget->setParent(ui->w1);
        ParentToWidget[ui->w1] = widget;
        ui->v1->addWidget(widget);
        ui->w1->show();
        adjustSize();
    }else if(contentNum == 1){
        widget->setParent(ui->w2);
        ParentToWidget[ui->w2] = widget;
        ui->v2->addWidget(widget);
        ui->w2->show();
    }else if(contentNum == 2){
        widget->setParent(ui->w3);
        ParentToWidget[ui->w3] = widget;
        ui->v3->addWidget(widget);
        ui->w3->show();
    }else if(contentNum == 3){
        widget->setParent(ui->w4);
        ParentToWidget[ui->w4] = widget;
        ui->v4->addWidget(widget);
        ui->w4->show();
    }else{
        return false;
    }
    contentNum++;
    return true;
}

bool Layout::RemoveWidget(QWidget* widget){
//    QWidget* parent = dynamic_cast<QWidget*>(widget->parent());
    int i,x;
    if(ParentToWidget[ui->w1] == widget){
        i = 0;x = 0;
    }else if(ParentToWidget[ui->w2] == widget){
        i = 1;x = 1;
    }else if(ParentToWidget[ui->w3] == widget){
        i = 2;x = 2;
    }else if(ParentToWidget[ui->w4] == widget){
        i = 3;x = 3;
    }else{
        return false;
    }
    widget->setParent(nullptr);
    for(;i<contentNum-1;i++){
        ParentToVbox[widgets[i]]->removeWidget(ParentToWidget[widgets[i]]);
        ParentToVbox[widgets[i]]->addWidget(ParentToWidget[widgets[i+1]]);
        ParentToWidget[widgets[i+1]]->setParent(widgets[i]);
        ParentToWidget[widgets[i]] = ParentToWidget[widgets[i+1]];
    }
    if(contentNum>=x+1){
        widgets[contentNum-1]->hide();
        ParentToWidget[widgets[contentNum-1]] = nullptr;
    }
    contentNum--;
    adjustSize();
    return true;
}
