#include "Arduino.h"
#include "Foo.h"

namespace Foo {
    void setup(){
        pinMode(LED_BUILTIN, OUTPUT);
    }

    void loop(int time){
        digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(time);                       // wait for a second
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    delay(time);
    }
}
