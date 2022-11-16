// ArrowWidget.h
#ifndef ARROWWIDGET_H
#define ARROWWIDGET_H

#include <QWidget>
#include <QGraphicsDropShadowEffect>
#include <QPainterPath>
#include <hwselect.h>
#include <config.h>
#include <QPushButton>
const int SHADOW_WIDTH = 30;                 // 窗口阴影宽度;
const int TRIANGLE_WIDTH = 30;               // 小三角的宽度;
const int TRIANGLE_HEIGHT = 10;              // 小三角的高度;
const int BORDER_RADIUS = 15;                 // 窗口边角的弧度;


class ArrowWidget : public QWidget
{
    Q_OBJECT
public:
    ArrowWidget(QWidget* parent = 0,QColor _color = QColor(37, 74, 146));

    enum Derection{
        left,
        right,
        up,
        down
    };
    // 设置小三角起始位置;
    void setStartPos(int startX);
    // 设置小三角宽和高;
    void setTriangleInfo(int width, int height);
    // 设置展示文本
    void setText(QString s);
    // 设置小三角的位置
    void setDerection(Derection d);
    //
    QString text();
    // 比起左上角的位置  用户更关心小三角的尖尖的位置 重载move以便用户更容易定位气泡框的位置
    // x,y 是气泡窗口小贱贱的坐标
    void myMove(int x, int y);
    void setWidget(config* w);
    void setWidget(QWidget* w);
//    void setWidget(config* w);
protected:

    void paintEvent(QPaintEvent *);
    void mousePressEvent (QMouseEvent *);
private:
    // 小三角的偏移量;
    int m_offset;
    // 小三角的宽度;
    int m_triangleWidth;
    // 小三角高度;
    int m_triangleHeight;
    Derection derect;
    QWidget* widget;
    QColor color;
};

#endif // ARROWWIDGET_H

