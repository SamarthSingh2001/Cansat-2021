#include <XBee.h>
#define nss Serial

XBee xbee = XBee();
Rx16Response rx16 = Rx16Response();
void setup(){
    Serial.begin(9600);
    Serial1.begin(9600);
    xbee.setSerial(Serial1);

}

void loop(){
    xbee.readPacket(100);
    if(xbee.getResponse().isAvailable()){
        Serial.println("getting data from gcs");
        if(xbee.getResponse().getApiId() == RX_16_RESPONSE){
            xbee.getResponse().getRx16Response(rx16);
            for (int i = 0; i < rx.getDataLength(); i++) { 
                nss.print(rx.getData(i), BYTE); 
            } 
        }
    }
}