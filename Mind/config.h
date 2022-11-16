#ifndef CONFIG_H
#define CONFIG_H

#include <QWidget>
#include <utils.h>
using namespace std;
namespace Ui {
class config;
}

class config : public QWidget
{
    Q_OBJECT

public:
    explicit config(QWidget *parent = nullptr);
    ~config();
    configure data();
private:
    Ui::config *ui;
    configure* con;
signals:
    void start();
    void cancel();
};

#endif // CONFIG_H
