# SuperStars - Proyecto SumoBot

¡Bienvenido al repositorio del equipo **SuperStars**!  
Participamos en la competencia SumoBot organizada por la Universidad Cenfotec y MakerFaire San José.

## 🤖 Sobre el proyecto

Este proyecto contiene el código y recursos utilizados para programar y competir con nuestro robot SumoBot.  
El objetivo del SumoBot es sacar al rival del ring (dojo) usando estrategias de movimiento autónomo, sensores y lógica programada en Python (CircuitPython).

## 🚀 ¿Cómo ejecutar el código?

1. **Requisitos:**
   - Placa IdeaBoard (ESP32) con CircuitPython instalado.
   - Sensores infrarrojos conectados a los pines IO36, IO39, IO34, IO35.
   - Sensor ultrasónico HCSR04 conectado a IO25 y IO26.
   - Librería `hcsr04.mpy` en la carpeta `lib` de tu IdeaBoard.

2. **Carga del programa:**
   - Copia el archivo `robotcode.py` al dispositivo (IdeaBoard) usando Thonny o cualquier editor compatible con CircuitPython.

3. **Ejecución:**
   - Al encender el robot, esperará 3 segundos antes de iniciar su rutina.
   - El robot se moverá usando los sensores para detectar bordes y oponentes, siguiendo la lógica definida en el script.

## 📦 Archivos principales

- `robotcode.py`: Código principal del robot.
- `img1.jpeg`, `img2.jpeg`: Imágenes de nuestro robot.

## 🏁 Ejemplos de uso del código (`robotcode.py`)

Debajo algunos ejemplos de cómo utilizar las funciones principales del script:

```python
from robotcode import forward, backward, left, right, stop, wiggle, lookForward, scan, forwardCheck

# Mover el robot hacia adelante durante 2 segundos a velocidad 0.5
forward(2, 0.5)

# Girar a la izquierda durante 1 segundo a velocidad 0.3
left(1, 0.3)

# Hacer que el robot oscile 3 veces con movimientos rápidos (función "wiggle")
wiggle(0.2, 3, 0.6)

# Detener el robot
stop()

# Leer distancia con el sensor ultrasónico
distancia = lookForward()
print("Distancia detectada:", distancia)

# Evitar que el robot salga del dojo usando sensores infrarrojos
forwardCheck(1, 0.5, 2950)

# Escanear a la búsqueda de oponente
encontrado = scan()
if encontrado:
    print("¡Oponente detectado!")
else:
    print("No se detectó oponente.")
```

## 🏆 Nuestra experiencia en SumoBot

- Aprendimos a trabajar en equipo, programar sensores y motores, y a resolver problemas de robótica real.
- Participamos con entusiasmo en el torneo y afinamos nuestra estrategia para lograr el mejor rendimiento posible.
- ¡Aquí algunas fotos de nuestro robot en acción!

![robot](img1.jpeg)
![algo más](img2.jpeg)

## 📝 Créditos y agradecimientos

- Organizado por Universidad Cenfotec y MakerFaire San José.
- Gracias a nuestros profesores, mentores y a todo el equipo SuperStars.

---

**Licencia:** MIT / Creative Commons (elige la que prefieras)

---

¡Esperamos que este proyecto inspire a otros a sumarse al mundo de la robótica!
