#ifndef Xbee_h
#define Xbee_h

#include "Arduino.h"

class Xbee {
    public:
    Xbee() {};
    bool setup();
    bool sendPacket(String packet);


}

#endif