import board
from ideaboard import IdeaBoard
from time import sleep
from hcsr04 import HCSR04
import random

sonar = HCSR04(board.IO25, board.IO26)
ib = IdeaBoard()

sen1 = ib.AnalogIn(board.IO36)
sen2 = ib.AnalogIn(board.IO39)
sen3 = ib.AnalogIn(board.IO34)
sen4 = ib.AnalogIn(board.IO35)

infrarrojos = [sen1, sen2, sen3, sen4]

def arreglo_a_entero(bits):
    valor = 0
    for bit in bits:
        valor = (valor << 1) | bit
    return valor

def leer_sensores(infrarrojos,valor_critico=10000):
    return [int(sen.value < valor_critico) for sen in infrarrojos]

def on_white(infrarrojos,valor_critico=10000):
    sensores = leer_sensores(infrarrojos,valor_critico)
    return arreglo_a_entero(sensores) > 0

def line_status(infrarrojos,valor_critico=10000):
    sensores = leer_sensores(infrarrojos,valor_critico)
    return arreglo_a_entero(sensores)

def wiggle(t,n,speed):
    for i in range(n):
        ib.pixel = (0,0,255)
        ib.motor_1.throttle = -speed
        ib.motor_2.throttle = speed
        sleep(t)
        ib.motor_1.throttle = speed
        ib.motor_2.throttle = -speed
        sleep(t)
        stop()
        sleep(t)
        ib.pixel = (0,0,255)
        ib.motor_1.throttle = speed
        ib.motor_2.throttle = -speed
        sleep(t)
        ib.motor_1.throttle = -speed
        ib.motor_2.throttle = speed
        sleep(t)

def forward(t,speed):
    ib.pixel = (0,255,0)
    ib.motor_1.throttle = speed
    ib.motor_2.throttle = speed
    sleep(t)

def backward(t,speed):
    ib.pixel = (150,255,0)
    ib.motor_1.throttle = -speed
    ib.motor_2.throttle = -speed
    sleep(t)

def left(t,speed):
    ib.pixel = (50,55,100)
    ib.motor_1.throttle = -speed
    ib.motor_2.throttle = speed
    sleep(t)

def right(t,speed):
    ib.pixel = (50,55,100)
    ib.motor_1.throttle = speed
    ib.motor_2.throttle = -speed
    sleep(t)

def stop():
    ib.pixel = (0,0,0)
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0

def randomTurn(t,speed):
    dir = random.choice([-1,1])
    ib.pixel = (255,0,0)
    ib.motor_1.throttle = dir*-speed
    ib.motor_2.throttle = dir*speed
    sleep(t)

def lookForward():
    stop()
    dist = sonar.dist_cm()
    sleep(0.2)
    return dist

def scan():
    stop()
    maxCount=10
    count = 0
    dist= lookForward()
    while count <maxCount and (dist>30 or dist==-1):
        left(0.2,0.2)
        count+=1
        dist= lookForward()
    stop()
    if count==maxCount:
        return False
    else:
        return True

def forwardCheck(t, speed,th):
     d = int(t / 0.01)
     for i in range(d):
         status = line_status(infrarrojos, th)
         print(status)
         if status == 0:
             forward(0.1,speed)
         elif (status >= 1 and status <= 3):
             forward(0.5,1)
         else:
             stop()
             sleep(0.3)
             backward(1,0.3)
             randomTurn(1,0.3)

sleep(3)
th = 2950
while True:
    forwardCheck(0.1,0.5,th)
