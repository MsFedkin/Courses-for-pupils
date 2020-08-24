#include <Servo.h>

Servo servo;  

int servoPin = 9;
int zeroDegree = 12;
int nintyDegree = 11;
int oneEightyDegree = 10;

void setup()
{
  servo.attach(servoPin);
  pinMode(zeroDegree,INPUT);
  pinMode(nintyDegree,INPUT);
  pinMode(oneEightyDegree,INPUT);
}

void loop()
{
  if(digitalRead(zeroDegree) == HIGH) servo.write(0);
  if(digitalRead(nintyDegree) == HIGH) servo.write(90);
  if(digitalRead(oneEightyDegree) == HIGH) servo.write(180);
    
}
