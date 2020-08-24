int melody[] = {262 , 196 , 196 , 220 , 196 , 0, 247 , 262};
int noteDurations[] = {4, 8, 8, 4, 4, 4, 4, 4};

int buttonPin = 12;
int buzz = 8;

void setup(){
 
 pinMode(buttonPin, INPUT);
 pinMode(buzz, OUTPUT);

}
void loop(){
 
 bool buttonState = digitalRead(buttonPin);

 if (buttonState == true){
   for (int thisNote=0; thisNote <8; thisNote++){
     int noteDuration = 1000 / noteDurations [thisNote];
     tone(buzz, melody [thisNote], noteDuration);
     int pauseBetweenNotes = noteDuration * 1.30;
     delay(pauseBetweenNotes);
   }
 }
}
