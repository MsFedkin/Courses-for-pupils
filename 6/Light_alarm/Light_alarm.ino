int ldr = A0; //фоторезистор
int led = 13; // светодиод
int buzz = 8;
int lightness; // значение с фоторезистора

void setup() {
  pinMode(led,OUTPUT);
  pinMode(buzz,OUTPUT);
  pinMode(ldr,INPUT);
  Serial.begin(9600);

}

void loop() {
  lightness = analogRead (ldr); // считывание значения фоторезистора

  if(lightness < 400)
  {
    digitalWrite(buzz,HIGH);
    digitalWrite(led,HIGH);    
  }
  else
  {
    digitalWrite(buzz,LOW);
    digitalWrite(led,LOW); 
  }

}
