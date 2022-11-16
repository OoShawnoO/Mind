#ifndef HWSELECT_H
#define HWSELECT_H

#include <QWidget>
#include <arrowwidget.h>
#include <QPushButton>
#include <vector>
using namespace std;
namespace Ui {
class hwselect;
}

class hwselect : public QWidget
{
    Q_OBJECT

public:
    hwselect(QWidget *parent = nullptr);
    ~hwselect();
    vector<QPushButton*> get_btns();
private:
    Ui::hwselect *ui;
};

#endif // HWSELECT_H
