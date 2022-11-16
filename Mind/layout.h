#ifndef LAYOUT_H
#define LAYOUT_H

#include <QWidget>
#include <vector>
#include <QVBoxLayout>
#include <unordered_map>
using namespace std;
namespace Ui {
class Layout;
}

class Layout : public QWidget
{
    Q_OBJECT

public:
    explicit Layout(QWidget *parent = nullptr);
    ~Layout();
    bool AddWidget(QWidget* widget);
    bool RemoveWidget(QWidget* widget);
private:
    Ui::Layout *ui;
    int contentNum;
    QWidget* widgets[4];
    unordered_map<QWidget*,QWidget*>    ParentToWidget;
    unordered_map<QWidget*,QVBoxLayout*> ParentToVbox;
};

#endif // LAYOUT_H
