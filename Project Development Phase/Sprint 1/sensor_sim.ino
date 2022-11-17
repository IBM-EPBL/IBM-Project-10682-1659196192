#include"DHT.h"
#defineDHTPIN2
#defineDHTTYPEDHT22 //DHT22(AM2302),AM2321
DHTdht(DHTPIN,DHTTYPE);
voidsetup(){
Serial.begin(115200);
Serial.println(F("DHT22example!"));
dht.begin();
}
voidloop(){
floattemperature=dht.readTemperature();
floathumidity=dht.readHumidity();
//Checkifanyreadsfailedandexitearly(totryagain).
if(isnan(temperature)||isnan(humidity)){
Serial.println(F("FailedtoreadfromDHTsensor!"));
return;
}
Serial.print(F("Humidity:"));
Serial.print(humidity);
Serial.print(F("% Temperature:"));
Serial.print(temperature);
Serial.println(F("°C"));
//Waitafewsecondsbetweenmeasurements.
delay(2000);
