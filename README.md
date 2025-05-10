Este código en Python utiliza OpenCV y MediaPipe para contar los dedos levantados frente a la cámara en tiempo real. Primero, se configura la comunicación con un Arduino a través de un puerto serial (USB). Luego, se captura el video desde la cámara y se procesa cada fotograma con MediaPipe para detectar la mano. Para cada mano detectada, se analizan las posiciones de los puntos clave de los dedos, y si un dedo está levantado, se cuenta como tal.

Cuando el número de dedos detectados cambia, ese número se envía al Arduino por medio de la conexión serial. El Arduino puede usar esta información para controlar LEDs, displays u otros dispositivos en el hardware, según se haya configurado previamente.

El código facilita la integración de visión por computadora con microcontroladores, proporcionando una forma simple de interactuar con el hardware mediante gestos de la mano.
