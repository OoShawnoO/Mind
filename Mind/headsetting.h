#ifndef HEADSETTING_H
#define HEADSETTING_H
#include <utils.h>
#include <QDialog>
#include <QComboBox>
#include <QPushButton>
namespace Ui {
class headsetting;
}

class headsetting : public QDialog
{
    Q_OBJECT

public:
    explicit headsetting(QWidget *parent = nullptr);
    ~headsetting();
    headsettingRet data();

private:
    Ui::headsetting *ui;
    headsettingRet* ret;
    QComboBox* pga[8];
    QComboBox* input[8];
    QComboBox* bias[8];
    QComboBox* srb2[8];
    QComboBox* srb1[8];
    QPushButton* changeBtns[8];
    int currentIdx;
    bool saved;
signals:
    void save();
    void load();
    void reset();
};

#endif // HEADSETTING_H
