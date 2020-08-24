#define led 13 // светодиод
#define button 9 // кнопка
// переменные для кнопки 
bool push; // состояние в настоящий маомент времени
bool lastPush; // прошлый момент времени
bool permition; // итоговое значение

void setup() {
 pinMode(led,OUTPUT);
 pinMode(button,INPUT);

}

void loop() {
  push = digitalRead(button); //чтение кнопки 
  delay(5);

  if((push == true) && (lastPush == false)) //если кнопка нажата в настоящий момент времени
  {
    permition = !permition; // изменяем значение 
  }
  push = lastPush;
  
  if(permition == true) //если есть разрешение то включаем светодиод
  {
     digitalWrite(led,HIGH);
  }
  else
  {
    digitalWrite(led,LOW);
  }
  Serial.print("Znachenie knopki: ");
  Serial.println(permition);
}
