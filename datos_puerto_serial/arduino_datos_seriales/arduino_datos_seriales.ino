void setup()
{
   Serial.begin(9600);
}
 
 
void loop()
{
   if (Serial.available())
   {
      String data = Serial.readStringUntil('\n');
      if (data == "enviar"){
        for (int a = 0; a < 10; a++)
        Serial.println(random(100));
        Serial.println("");
      }
   }
}
