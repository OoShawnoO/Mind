// ArrowWidget.cpp
#include "arrowwidget.h"

#include <QWidget>
#include <QHBoxLayout>
#include <QPoint>
#include <QPainter>
#include <QImage>
#include <QVariant>


ArrowWidget::ArrowWidget(QWidget *parent,QColor _color):
    QWidget(parent),
    m_offset(50),
    m_triangleWidth(TRIANGLE_WIDTH),
    m_triangleHeight(TRIANGLE_HEIGHT)
{
    color = _color;
    setWindowFlags(Qt::FramelessWindowHint);
    setAttribute(Qt::WA_TranslucentBackground);
}

void ArrowWidget::setWidget(config* w){
    QVBoxLayout* hMainLayout = new QVBoxLayout;
    setLayout(hMainLayout);
    connect(w,&config::cancel,[=](){this->hide();});
    widget = w;
    hMainLayout->addWidget(widget);
    adjustSize();
}

void ArrowWidget::setWidget(QWidget* w){
    QVBoxLayout* hMainLayout = new QVBoxLayout;
    setLayout(hMainLayout);
    widget = w;
    hMainLayout->addWidget(widget);
    adjustSize();
}


// 设置小三角显示的起始位置;
void ArrowWidget::setStartPos(int startX)
{
    m_offset = startX;
    repaint();
}
void ArrowWidget::setTriangleInfo(int width, int height)
{
    m_triangleWidth = width;
    m_triangleHeight = height;
}

void ArrowWidget::setDerection(ArrowWidget::Derection d)
{
    derect = d;
}


void ArrowWidget::paintEvent(QPaintEvent*)
{

    QPainter painter(this);
    painter.setRenderHint(QPainter::Antialiasing, true);
    painter.setPen(Qt::NoPen);
    painter.setBrush(color);

    QPainterPath drawPath;
    // 小三角区域;
    QPolygon trianglePolygon;

    QRect myRect(widget->x(), widget->y(), widget->width(), widget->height());

    // 设置小三的具体位置
    int tri_pos_x, tri_pos_y;
    switch (derect)
    {
    case up:{
        // 小三角左边的点的位置
        tri_pos_x = myRect.x() + m_offset;
        tri_pos_y = myRect.y();
        trianglePolygon << QPoint(tri_pos_x, tri_pos_y);
        trianglePolygon << QPoint(tri_pos_x + m_triangleWidth, tri_pos_y);
        trianglePolygon << QPoint(tri_pos_x + m_triangleWidth / 2, tri_pos_y - m_triangleHeight);
    }
        break;
    case left:{
        // 小三上边点的位置
        tri_pos_x = myRect.x();
        tri_pos_y = myRect.y() + m_offset;
        trianglePolygon << QPoint(tri_pos_x, tri_pos_y);
        trianglePolygon << QPoint(tri_pos_x - m_triangleHeight, tri_pos_y + m_triangleWidth / 2);
        trianglePolygon << QPoint(tri_pos_x, tri_pos_y + m_triangleWidth);
    }
        break;
    case right:{
        // 小三上边点的位置
        tri_pos_x = myRect.x() + myRect.width();
        tri_pos_y = myRect.y() + m_offset;
        trianglePolygon << QPoint(tri_pos_x, tri_pos_y);
        trianglePolygon << QPoint(tri_pos_x + m_triangleHeight, tri_pos_y + m_triangleWidth / 2);
        trianglePolygon << QPoint(tri_pos_x, tri_pos_y + m_triangleWidth);
    }

        break;
    case down:{
        // 小三左边点的位置
        tri_pos_x = myRect.x() + m_offset;
        tri_pos_y = myRect.y() + myRect.height();
        trianglePolygon << QPoint(tri_pos_x, tri_pos_y);
        trianglePolygon << QPoint(tri_pos_x + m_triangleWidth / 2, tri_pos_y + m_triangleHeight);
        trianglePolygon << QPoint(tri_pos_x + m_triangleWidth, tri_pos_y);
    }
        break;
    default:
        break;
    }
    drawPath.addRoundedRect(myRect, BORDER_RADIUS, BORDER_RADIUS);
    drawPath.addPolygon(trianglePolygon);
    painter.drawPath(drawPath);
}


void ArrowWidget::mousePressEvent(QMouseEvent *)
{
    // this->close ();
}

