// This is the functions that reads the pin's values, 
// and outputs the pin number and analog value from the sensor.
void readPin(int pin){
  Serial.print(pin); 
  Serial.println(analogRead(pin));
}
// The setup of the Serial communication, on channel 9600.
void setup(){
  Serial.begin(9600);
}
// This is the code that repeats every 0.5 seconds.
void loop(){
  // This 'for' loop is used to see what pins are recieving a analog signal. 
  // If they are, they will output this signal to the serial communication with the "readPin(x)" function.
  for(int i = 0; i <= 7; i++) {
    if(analogRead(i) != 'None') {
      readPin(i);
    }
  }
  // A delay of 500 milliseconds (0.5 seconds) is used to stop python from reading the values too quickly. 
  // Change to 250 milliseconds if absolutely neccessary.
  delay(500);
}
