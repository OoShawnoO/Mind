#ifndef LSL_H
#define LSL_H

#include <QWidget>

namespace Ui {
class lsl;
}

class lsl : public QWidget
{
    Q_OBJECT

public:
    explicit lsl(QWidget *parent = nullptr);
    ~lsl();

private:
    Ui::lsl *ui;
};

#endif // LSL_H
