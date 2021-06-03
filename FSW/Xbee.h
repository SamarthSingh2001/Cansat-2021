#ifndef Xbee_h
#define Xbee_h

#include "Arduino.h"
namespace PopTarts {
class Xbee {
    public:
    Xbee() {};
    bool setup();
    bool sendPacket(String packet, uint16_t destination); // destination is the source address of the recieving xbee, addr. should be string i think?
    String readPacket(int timeout);
    String readPacket();

}
}

 // NOTE: WIP don't use
#endif