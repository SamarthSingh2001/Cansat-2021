#include "Radio.h"

#define nss Serial
namespace Radio {

    XBee xbeeGS = XBee();
    void setup(){
        Serial1.begin(9600);
        xbeeGS.setSerial(Serial1);

    }
    bool packetReceived(){

    }
    void send(String packet){

    }

    void loop(){
        xbeeGS.readPacket(50);
        if(xbeeGS.getResponse().isAvailable()){
            if(xbeeGS.getResponse().getApiId() == RX_16_RESPONSE)
                xbeeGS.getResponse().getRx16Response(rx16);

            for (int i = 0; i < rx.getDataLength(); i++) { 
                nss.print(rx.getData(i), BYTE); 
            }     
        }
    }
}