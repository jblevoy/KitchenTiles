void setup()
{
 Serial.begin(9600);
 for(byte i = 0; i < 7; i++){
   pinMode(i+13,OUTPUT);
 }

 byte someValue = 20; //For this example, lets convert the number 20
 
 
 char binary[9] = {0}; //This is where the binary representation will be stored
 someValue += 128; //Adding 128 so that there will always be 8 digits in the string
 itoa(someValue,binary,2); //Conver someValue to a string using base 2 and save it in the array named binary
 char* string = binary + 1; //get rid of the most significant digit as you only want 7 bits


 Serial.println(string); //print out our string.
 for(byte i = 0; i < 7; i++){
   digitalWrite(i+13,string[i] - '0'); //write to the pin (the - '0' converts the bit of the string to HIGH or LOW)
 }
}

void loop()
{
}
