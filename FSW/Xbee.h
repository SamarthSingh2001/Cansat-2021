#ifndef Xbee_h
#define Xbee_h

#include "Arduino.h"

class Xbee {
    public:
    Xbee() {};
    bool setup();
    bool sendPacket(String packet, String destination); // destination is the source address of the recieving xbee, addr. should be string i think?
    String readPacket(int timeout);
    String readPacket();

}

#endif