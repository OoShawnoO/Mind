#ifndef UTILS_H
#define UTILS_H

#include <string>
using namespace std;

#define CONFIG_BACKGROUNDCOLOR 11, 28, 84

struct configure{
    string hardwareName;
    string retTime;
    string ipAddress;
    int frequency;
    int channel;
    void operator=(const configure& conf){
        hardwareName = conf.hardwareName;
        retTime = conf.retTime;
        ipAddress = conf.ipAddress;
        frequency = conf.frequency;
        channel = conf.channel;
    };
};

struct commonRet{
    bool channel[64];
    int maxFrequency;
    string model;
    int windows;
    int timeLength;
    int scale;
    commonRet(){
        for(int i=0;i<64;i++){
            channel[i] = false;
        }
    };
    void operator=(const commonRet& com){
        for(int i=0;i<64;i++){
            channel[i] = com.channel[i];
        }
        maxFrequency = com.maxFrequency;
        model = com.model;
        windows = com.windows;
        timeLength = com.timeLength;
        scale = com.scale;
    }
};

struct allRet{
    string filter;
    string notch;
    double start;
    double stop;
    string type;
    int order;
    void operator=(const allRet& all){
        filter = all.filter;
        notch = all.notch;
        start = all.start;
        stop = all.stop;
        type = all.type;
        order = all.order;
    }
};

struct headsettingRet{
    string pga[64];
    string input[64];
    bool bias[64];
    bool srb2[64];
    bool srb1[64];
    void operator=(const headsettingRet& head){
        for(int i=0;i<8;i++){
            pga[i] = head.pga[i];
            input[i] = head.input[i];
            bias[i] = head.bias[i];
            srb2[i] = head.srb2[i];
            srb1[i] = head.srb1[i];
        }
    }
};

#endif // UTILS_H
