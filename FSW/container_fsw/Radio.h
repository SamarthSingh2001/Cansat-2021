#ifndef Xbee_h
#define Xbee_h

#include <XBee.h>
#include "Arduino.h"
#include "Library.h"

namespace Radio{
    void setup();
    bool packetReceived();
    void send(String packet);
    void loop();
} // end namespace

#endif