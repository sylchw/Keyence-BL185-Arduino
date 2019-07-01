#define read_interval 10 //in milliseconds (min 10ms max 2550ms)

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   
  delay(read_interval);                       
  int data, out;
  
  Serial.print("Characters received: ");
  Serial.println(Serial.available());
  
  while (Serial.available()){
     
     char c = Serial.read();
     byte mask = B01111111;
     
     char d = c&mask;
     
     Serial.print(d);
     Serial.flush();
     delay(1);
  }
  
  Serial.println();
  Serial.println();
  
  digitalWrite(LED_BUILTIN, LOW);    
  delay(100);                       
}
