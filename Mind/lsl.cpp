#include "lsl.h"
#include "ui_lsl.h"

lsl::lsl(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::lsl)
{
    ui->setupUi(this);
}

lsl::~lsl()
{
    delete ui;
}
