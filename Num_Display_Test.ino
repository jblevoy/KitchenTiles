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

const uint8_t SEG_DONE[] = {
	SEG_B | SEG_C | SEG_D | SEG_E | SEG_G,           // d
	SEG_A | SEG_B | SEG_C | SEG_D | SEG_E | SEG_F,   // O
	SEG_C | SEG_E | SEG_G,                           // n
	SEG_A | SEG_D | SEG_E | SEG_F | SEG_G            // E
	};

TM1637Display display(CLK, DIO);


void setup()
{
}

void loop()
{

  display.setBrightness(0x0f);
  delay(TEST_DELAY_500);

  display.setSegments(all_on);
  delay(TEST_DELAY_2000);

  display.setSegments(all_off);
  delay(TEST_DELAY_500);
  
  display.showNumberDec(1, false, 1, 3);        // (153, false, 2, 2) = "display number 153, don't change anything to the left, 3 digits, starting position 1 out of 0,1,2,3) 
  delay(TEST_DELAY_500);
/*
  display.showNumberDec(2, false, 1, 3);
  delay(TEST_DELAY_500);

  display.showNumberDec(3, false, 1, 3);
  delay(TEST_DELAY_500);

  display.showNumberDec(9, false, 1, 3);
  delay(TEST_DELAY_500);

  all_on[0] = 0b01001001;

  display.showNumberDec(10, false, 2, 2);
  delay(TEST_DELAY_500);

  display.showNumberDec(153, false, 3, 1);
  delay(TEST_DELAY_500);

  display.showNumberDec(0, false, 4, 0);
  delay(TEST_DELAY_500);

  display.showNumberDec(154);  //you can also just use the single value for showNumberDec function call
  delay(TEST_DELAY_500);
*/
  // Run through all the dots
    display.showNumberDecEx(156, (0x80 >> 1), false);
    delay(TEST_DELAY_2000);
    display.showNumberDecEx(157, (0x80 >> 1), false);
    delay(TEST_DELAY_2000);
    display.showNumberDecEx(158, (0x80 >> 1), false);
    delay(TEST_DELAY_2000);
    display.showNumberDecEx(159, (0x80 >> 1), false);
    delay(TEST_DELAY_2000);
    display.showNumberDecEx(200, (0x80 >> 1), false);
    delay(TEST_DELAY_2000);




  
/*


    
  for(k = 0; k < 4; k++) {
    display.setBrightness(7, false);  // Turn off
    display.setSegments(data);
    delay(TEST_DELAY);
  }

  // Selectively set different digits
  data[0] = 0b01001001;
  data[1] = display.encodeDigit(1);
  data[2] = display.encodeDigit(2);
  data[3] = display.encodeDigit(3);

  // On/Off test
  for(k = 0; k < 4; k++) {
    display.setBrightness(7, false);  // Turn off
    display.setSegments(data);
    delay(TEST_DELAY);
    display.setBrightness(7, true); // Turn on
    display.setSegments(data);
    delay(TEST_DELAY);  
  }

  // Selectively set different digits
  data[0] = 0b01001001;
  data[1] = display.encodeDigit(1);
  data[2] = display.encodeDigit(2);
  data[3] = display.encodeDigit(3);

  for(k = 3; k >= 0; k--) {
	display.setSegments(data, 1, k);
	delay(TEST_DELAY);
	}

  display.setSegments(data+2, 2, 2);
  delay(TEST_DELAY);

  display.setSegments(data+2, 2, 1);
  delay(TEST_DELAY);

  display.setSegments(data+1, 3, 1);
  delay(TEST_DELAY);


  // Show decimal numbers with/without leading zeros
  bool lz = false;
  for (uint8_t z = 0; z < 2; z++) {
	for(k = 0; k < 10000; k += k*4 + 7) {
		display.showNumberDec(k, lz);
		delay(TEST_DELAY);
	}
	lz = true;
  }

  // Show decimal number whose length is smaller than 4
  for(k = 0; k < 4; k++)
	data[k] = 0;
  display.setSegments(data);

	// Run through all the dots
	for(k=0; k <= 4; k++) {
		display.showNumberDecEx(0, (0x80 >> k), true);
		delay(TEST_DELAY);
	}

  display.showNumberDec(153, false, 3, 1);
  delay(TEST_DELAY);
  display.showNumberDec(22, false, 2, 2);
  delay(TEST_DELAY);
  display.showNumberDec(0, true, 1, 3);
  delay(TEST_DELAY);
  display.showNumberDec(0, true, 1, 2);
  delay(TEST_DELAY);
  display.showNumberDec(0, true, 1, 1);
  delay(TEST_DELAY);
  display.showNumberDec(0, true, 1, 0);
  delay(TEST_DELAY);

  // Brightness Test
  for(k = 0; k < 4; k++)
	data[k] = 0xff;
  for(k = 0; k < 7; k++) {
    display.setBrightness(k);
    display.setSegments(data);
    delay(TEST_DELAY);
  }
  
  // On/Off test
  for(k = 0; k < 4; k++) {
    display.setBrightness(7, false);  // Turn off
    display.setSegments(data);
    delay(TEST_DELAY);
    display.setBrightness(7, true); // Turn on
    display.setSegments(data);
    delay(TEST_DELAY);  
  }

  // Done!
  display.setSegments(SEG_DONE);

  while(1);
**/
}
