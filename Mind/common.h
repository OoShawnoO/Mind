#ifndef COMMON_H
#define COMMON_H

#include <QWidget>
#include <QCheckBox>
#include <utils.h>

enum WidType{
    SPECTROGRAM,
    FFT,
    TIMESRISE,
    BANDPOW
};

namespace Ui {
class common;
}

class common : public QWidget
{
    Q_OBJECT

public:
    explicit common(QWidget *parent = nullptr);
    ~common();
    void setType(WidType type);
    void setConfig(configure* con);
    commonRet data();
signals:
    void done();
    void cancel();

private:
    Ui::common *ui;
    commonRet* ret;
    QCheckBox* channelBox[8];
    QCheckBox* channelSelectBox[8];
};

#endif // COMMON_H
