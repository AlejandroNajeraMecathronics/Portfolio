#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2); 

void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Esperando...");
}

void loop() {
  if (Serial.available()) {
    String mensaje = Serial.readStringUntil('\n');
    lcd.clear();

    int separador = mensaje.indexOf('|');

    String linea1, linea2;
    if (separador != -1) {
      linea1 = mensaje.substring(0, separador);
      linea2 = mensaje.substring(separador + 1);
    } else {
      linea1 = "Producto:";
      linea2 = mensaje;
    }

    mostrarTextoScroll(0, linea1);
    mostrarTextoScroll(1, linea2);

    delay(6000);
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Esperando...");
  }
}

void mostrarTextoScroll(int fila, String texto) {
  int longitud = texto.length();

  if (longitud <= 16) {
    lcd.setCursor(0, fila);
    lcd.print(texto);
    delay(2000);
  } else {
    for (int i = 0; i <= longitud - 16; i++) {
      lcd.setCursor(0, fila);
      lcd.print(texto.substring(i, i + 16));
      delay(700);
    }
    delay(1000);  // Pausa al final del scroll
  }
}


