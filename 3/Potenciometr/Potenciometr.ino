/*
 * Суть программы это перевод значения полученого с потенциометра в шим
 */
  
  
  #define led    11 // светодиод
  #define pot    A0 // потенциометр

  int rotat; // значение потенциомтера
  int ledVal; // значение шим
 
void setup(){
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  pinMode(pot, INPUT);
}
 
void loop(){
  rotat = analogRead(pot);
 
  // Преобразуем значение в яркость. Для этого делим rotat на 4, что с учетом округления даст нам число от 0 до 255. Именно это число мы подадим на шим-выход, с помощью которого можно управлять яркостью.
  ledVal = rotat / 4;

  Serial.print("Znachenie potenciometra :");
  Serial.println(rotat);
  Serial.print("yarkost");
  Serial.println(ledVal);
  analogWrite(led, ledVal);
}
