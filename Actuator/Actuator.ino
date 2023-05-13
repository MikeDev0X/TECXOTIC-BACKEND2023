#include <SoftwareSerial.h>
String a;
char dato;
// Arduino uno Ext Serial pins
int ext_rx_pin = 9;
int ext_tx_pin = 8;
SoftwareSerial ext(ext_rx_pin, ext_tx_pin); //RX, TX 

byte pin_1=4;
byte pin_2=5;
byte pin_3=6;
byte pin_4=3;

void setup() {
  Serial.begin(9600);
  ext.begin(9600);
  //Serial.setTimeout(1);
  pinMode(pin_1, OUTPUT);
  pinMode(pin_2, OUTPUT);
  pinMode(pin_3, OUTPUT);
  pinMode(pin_4, OUTPUT);

}

int command = 0;
const int OPENCLAW1 = 1;
const int CLOSECLAW1 = 2;
const int OPENCLAW2 = 3;
const int CLOSECLAW2 = 4;
const int NOTHING = 0;


void loop() {
    if (ext.available() > 0) {
    // Print message on ide console
    dato=ext.read();
    command = dato - '0';

    switch(command){
        case OPENCLAW1:
            digitalWrite(pin_1, HIGH);
            digitalWrite(pin_2, LOW);
            digitalWrite(pin_3, LOW);
            digitalWrite(pin_4, LOW);
            break;
        case CLOSECLAW1:
            digitalWrite(pin_1, LOW);
            digitalWrite(pin_2, HIGH);
            digitalWrite(pin_3, LOW);
            digitalWrite(pin_4, LOW);
            break;
        case OPENCLAW2:
            digitalWrite(pin_1, LOW);
            digitalWrite(pin_2, LOW);
            digitalWrite(pin_3, HIGH);
            digitalWrite(pin_4, LOW);
            break;
        case CLOSECLAW2:
            digitalWrite(pin_1, LOW);
            digitalWrite(pin_2, LOW);
            digitalWrite(pin_3, LOW);
            digitalWrite(pin_4, HIGH);
            break;
        case NOTHING:
            digitalWrite(pin_1, LOW);
            digitalWrite(pin_2, LOW);
            digitalWrite(pin_3, LOW);
            digitalWrite(pin_4, LOW);
            break;
      }
  }
}
