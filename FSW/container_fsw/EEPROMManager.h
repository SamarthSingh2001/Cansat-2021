#ifndef EEPROMManager_h
#define EEPROMManager_h

#include "Arduino.h"
#include <EEPROM.h>
#include "Library.h"

namespace EEPROM {
    void setup();
    
    void writeEEPROM_time();
    void writeEEPROM_pkt();
    void writeEEPROM_state();
    
    void readEEPROM_pkt();
    void readEEPROM_state();
    void readEEPROM_time();

}
#endif