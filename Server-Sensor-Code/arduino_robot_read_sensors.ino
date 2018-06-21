#include <SoftwareSerial.h>
#include <Wire.h>
#include <Adafruit_MLX90614.h>

SoftwareSerial co2Serial(10, 11); // RX, TX
unsigned char hexdata[9] = {0xFF,0x01,0x86,0x00,0x00,0x00,0x00,0x00,0x79};
char CO2 = true;
char temp = true;

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

// This is the functions that reads the pin's values, 
// and outputs the pin number and analog value from the sensor.
void readPin(int pin){Serial.print(pin); Serial.println(analogRead(pin));}

void readTEMP(){int t = mlx.readObjectTempC() ;Serial.print("1"); Serial.println(t);
  }
  
void readCO2() {
    co2Serial.write(hexdata,9);
    for(int i=0;i<9;i++)  {
      if (co2Serial.available()>0) {
        long hi,lo,CO2;
        int ch=co2Serial.read();
    
        if(i==2){
          hi=ch; //High concentration
        }   
        if(i==3){
          lo=ch;   
        }   //Low concentration
        if(i==8) {
          CO2=hi*256+lo;  //CO2 concentration
          Serial.print("0");
          Serial.println(CO2);
        }
      }
    } 
  }
// The setup of the Serial communication, on channel 9600.
void setup(){
  mlx.begin();  
  Serial.begin(9600);
  co2Serial.begin(9600);
}
// This is the code that repeats every 0.5 seconds.
void loop(){
  // This 'for' loop is used to see what pins are recieving a analog signal. 
  // If they are, they will output this signal to the serial communication with the "readPin(x)" function.
  //for(int i = 2; i <= 7; i++) {if(i != 4 || i != 5) {if(analogRead(i) != 'None') {readPin(i);}}}

  // IF Statements
  
  if (temp == true) {readTEMP();}
  if (CO2 == true) {readCO2();}
  
  // A delay of 500 milliseconds (0.5 seconds) is used to stop python from reading the values too quickly. 
  // Change to 250 milliseconds if absolutely neccessary.
  delay(500);
}
