
int motorPin = 13;
int onButton = 12;
int offButton = 11;


void setup()
{
    pinMode(motorPin,OUTPUT);
    pinMode(onButton,INPUT);
    pinMode(offButton,INPUT);
}

void loop()
{
    if(digitalRead(onButton) == HIGH) digitalWrite(motorPin,HIGH);
    if(digitalRead(offButton) == HIGH) digitalWrite(motorPin,LOW);
}
