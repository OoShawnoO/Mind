#ifndef SIGNAL_H
#define SIGNAL_H

#include <QWidget>

namespace Ui {
class signal;
}

class signal : public QWidget
{
    Q_OBJECT

public:
    explicit signal(QWidget *parent = nullptr);
    ~signal();

private:
    Ui::signal *ui;
};

#endif // SIGNAL_H
