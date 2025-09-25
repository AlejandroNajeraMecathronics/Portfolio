#include <Servo.h>

Servo servo;
int botonPin = 7;
int potPin = A0;

bool activo = false;
bool ultimoEstadoBoton = LOW;

void setup() {
  servo.attach(9);
  pinMode(botonPin, INPUT_PULLUP); // pullup interno
  Serial.begin(9600);
}

void loop() {
  bool estadoBoton = !digitalRead(botonPin); // activo con LOW

  if (estadoBoton && !ultimoEstadoBoton) {
    activo = !activo;  // cambia estado al presionar
    delay(200); // anti-rebote
  }
  ultimoEstadoBoton = estadoBoton;

  if (activo) {
    int pot = analogRead(potPin); // 0–1023
    int velocidad = map(pot, 0, 1023, 0, 180); // mapa a señal servo

    // Opcional: limitar a solo una dirección
    if (velocidad < 90) velocidad = 90;

    servo.write(velocidad);
    Serial.print("Velocidad: ");
    Serial.println(velocidad);
  } else {
    servo.write(90); // neutro = detenido
  }
}
