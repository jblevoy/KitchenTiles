#include <Arduino.h>
#include <TM1637Display.h>

// Module connection pins (Digital Pins)
#define CLK 3
#define DIO 4

// The amount of time (in milliseconds) between tests
#define TEST_DELAY_2000   2000
#define TEST_DELAY_500   500
#define TEST_DELAY_250   250

int k;
uint8_t all_on[] = { 0xff, 0xff, 0xff, 0xff };
uint8_t all_off[] = { 0x0, 0x0, 0x0, 0x0 };
TM1637Display display(CLK, DIO);



void setup() {
Serial.begin(9600);
display.setBrightness(0x0f);
}

void loop() {
    for (k = 0; k < 100; k++){
        Serial.println(analogRead(A5));
        int angle_of_day = analogRead(A5);
        display.showNumberDecEx(angle_of_day, (0x80 >> 1), false);
        delay(100);  
}
/*
  display.setBrightness(0x0f);
  delay(TEST_DELAY_500);
  
    display.setBrightness(0x0f);
    delay(TEST_DELAY_500);
    display.showNumberDecEx(200, (0x80 >> 1), false);
    delay(TEST_DELAY_2000);
    display.showNumberDecEx(201, (0x80 >> 1), false);
    delay(TEST_DELAY_2000);
    display.showNumberDecEx(202, (0x80 >> 1), false);
    delay(TEST_DELAY_2000);
    */
}
