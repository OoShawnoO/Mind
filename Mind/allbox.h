#ifndef ALLBOX_H
#define ALLBOX_H

#include <QDialog>
#include <utils.h>
namespace Ui {
class allbox;
}

class allbox : public QDialog
{
    Q_OBJECT

public:
    explicit allbox(QWidget *parent = nullptr);
    ~allbox();
    allRet data();
private:
    Ui::allbox *ui;
    allRet* ret;
signals:
    void save();
    void load();
    void reset();
};

#endif // ALLBOX_H
