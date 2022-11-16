#ifndef MENUBAR_H
#define MENUBAR_H

#include <QWidget>
#include <QMenuBar>

class menubar : public QMenuBar
{
    Q_OBJECT
public:
    explicit menubar(QWidget *parent = nullptr);

signals:

};

#endif // MENUBAR_H
