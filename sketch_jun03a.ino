
int x,y;
int pin=2;


void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(pin,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available()){
   int data=Serial.read();
    if(data=='X')
    {
     
      digitalWrite(pin,HIGH);
      
    
    }
     else if(data=='Y'){
      
        digitalWrite(pin,LOW);
        }
    
      
      
  }
}
