
#include "EEPROMManager.h"

namespace EEPROM {
    void writeEEPROM_state() {
        EEPROM.update(address, mission_state);
        /*
        address = address + 1;
        if(address == EEPROM.length()) {
        address = 0;
        }
        */
    }

    void writeEEPROM_time() {
        if(mission_time < 255) {
            EEPROM.update(address, mission_time/1000); // writes seconds value
        } else {
            count++;
            EEPROM.update(address + count, mission_time/1000); // writes seconds value
        }
        
    }

    void writeEEPROM_pkt() {
        EEPROM.update(1, packetCount);
    }

    void readEEPROM_pkt() {
        packetCount = EEPROM.read(1);
    }

    void readEEPROM_state() {
        mission_state = EEPROM.read(0);
    }

    void readEEPROM_time() {
        mission_time = EEPROM.read(2 + count);
    } 
}