int red = 12;
int green = 11;
int blue = 10;

void Red(int r,int g,int b)// красный цвет
{
  digitalWrite (r,HIGH);
  digitalWrite (b,LOW);
  digitalWrite (g,LOW);
  Serial.println("RED");
}

void Green(int r,int g,int b)// зеленый цвет
{
  digitalWrite (g,HIGH);
  digitalWrite (r,LOW);
  digitalWrite (b,LOW);
  Serial.println("GREEN");
}
void Blue(int r,int g,int b)// синий цвет 
{
  digitalWrite (b,HIGH);
  digitalWrite (g,LOW);
  digitalWrite (r,LOW);
  Serial.println("BLUE"); 
}

void Yellow(int r,int g,int b) // желтый цвет
{
  digitalWrite (r,HIGH);
  digitalWrite (g,HIGH);
  digitalWrite (b,LOW);
  Serial.println("YELLOW");

}

void Purpule (int r,int g,int b) // фиолетовый цвет
{
  digitalWrite (b,HIGH);
  digitalWrite (r,HIGH);
  digitalWrite (g,LOW);
  Serial.println("PURPLE");
}

void Indigo(int r,int g,int b) // голубой цвет
{
  digitalWrite (b,HIGH);
  digitalWrite (g,HIGH);
  digitalWrite (r,LOW);
  Serial.println("INDIGO");
}

void Orange(int r,int g,int b)
{
  digitalWrite (b,LOW);
  digitalWrite (g,HIGH);
  digitalWrite (r,HIGH);
  Serial.println("ORANGE");
}

void White(int r,int g,int b)// белый цвет 
{
  digitalWrite (r,HIGH);
  digitalWrite (g,HIGH);
  digitalWrite (b,HIGH);
  Serial.println("WHITE");
}

void Clear(int r,int g,int b)
{
  digitalWrite (r,LOW);
  digitalWrite (g,LOW);
  digitalWrite (b,LOW);
  Serial.println("CLEAR");
}

void setup() {
  Serial.begin(9600);
  
  pinMode(red,OUTPUT);
  pinMode(green,OUTPUT);
  pinMode(blue,OUTPUT);

}

void loop() {
  
  Red(red,green,blue);
  delay(3000);
  Orange(red,green,blue);
  delay(3000);
  Yellow(red,green,blue);
  delay(3000);
  Green(red,green,blue);
  delay(3000);
  Indigo(red,green,blue);
  delay(3000);
  Blue(red,green,blue);
  delay(3000);
  Purpule(red,green,blue);
  delay(3000);

}
