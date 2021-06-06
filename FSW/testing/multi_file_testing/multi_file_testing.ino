#include "Foo.h"
// using blink example to demonstrate splitting arduino code into multiple files
void setup() {
  // put your setup code here, to run once:
  Foo::setup();
}

void loop() {
  // put your main code here, to run repeatedly:
  Foo::loop(1000);
}
