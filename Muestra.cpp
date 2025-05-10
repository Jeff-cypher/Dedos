int ledPins[] = {2, 3, 4, 5, 6}; 
int dedoRecibido = 0;

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 5; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  if (Serial.available() > 0) {
    dedoRecibido = Serial.read() - '0'; 
    dedoRecibido = constrain(dedoRecibido, 0, 5);

    for (int i = 0; i < 5; i++) {
      digitalWrite(ledPins[i], i < dedoRecibido ? HIGH : LOW);
    }
  }
}
