#include <LiquidCrystal.h>

LiquidCrystal lcd(7, 8, 9, 10, 11, 12); // RS E D4 D5 D6 D7

int pot = A0;
int ldr = A1;

void setup() {
  lcd.begin(16, 2);
  
  pinMode(pot,INPUT);
  pinMode(ldr,INPUT);
}

void loop() {
  
  lcd.setCursor(0, 0);
  lcd.print("Znachenie1:");
  
  lcd.setCursor(11, 0);
  lcd.print(analogRead(pot));
  
  lcd.setCursor(0, 1);
  lcd.print("Znachenie2:");
  
  lcd.setCursor(11, 1);
  lcd.print(analogRead(ldr));

  lcd.clear();
  
}
 
