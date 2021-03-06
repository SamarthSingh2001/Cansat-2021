/**
 * saving/reading from eeprom
 */
#ifndef EEPROMManager_h
#define EEPROMManager_h

#include "Arduino.h"
#include "Library.h"
#include <EEPROM.h>
namespace EEPROM{

    void setup();
    void writeEEPROM_state();
    void writeEEPROM_time();
    void writeEEPROM_pkt();
    
    void readEEPROM_pkt();
    void readEEPROM_state();
    void readEEPROM_time();
}// end namespace
#endif