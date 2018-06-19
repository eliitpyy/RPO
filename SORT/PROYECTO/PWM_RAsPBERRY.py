import RPi.GPIO as GPIO # Cargamos la libreria RPi.GPIO  
from time import sleep  # cargamos la función sleep del módulo time 
  
GPIO.setmode(GPIO.BCM)  # Ponemos la Raspberry en modo BCM  
  
GPIO.setup(21, GPIO.OUT)  # Ponemos el pin GPIO nº25 como salida para el LED #1  

white = GPIO.PWM(21, 1000)   # Creamos el objeto 'white' en el pin 25 a 100 Hz
white.start(70)              # Iniciamos el objeto 'white' al 0% del ciclo de trabajo (completamente apagado)  

# A partir de ahora empezamos a modificar los valores del ciclo de trabajo
  
pause_time = 0.002           # Declaramos un lapso de tiempo para las pausas
  
try:                        # Abrimos un bloque 'Try...except KeyboardInterrupt'
    while True:             # Iniciamos un bucle 'while true'  
        for i in range(0,101,5):            # De i=0 hasta i=101 (101 porque el script se detiene al 100%)
            white.ChangeDutyCycle(20)      # LED #1 = i
##            sleep(pause_time)             # Pequeña pausa para no saturar el procesador
##        for i in range(100,-1,-5):        # Desde i=100 a i=0 en pasos de -1  
##            white.ChangeDutyCycle(i)      # LED #1 = i 
##            sleep(pause_time)             # Pequeña pausa para no saturar el procesador  
  
except KeyboardInterrupt:   # Se ha pulsado CTRL+C!!
    white.stop()            # Detenemos el objeto 'white'
    GPIO.cleanup()          # Limpiamos los pines GPIO y salimos
