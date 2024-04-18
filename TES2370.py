# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 12:48:05 2024

@author: Nicolas Torasso
"""
import serial

def getValue(code, debug = False):

    refs = {"0": "DCV 200 mV",
            "1": "DCV 2 V",
            "2": "DCV 20 V",
            "3": "DCV 200 V",
            "4": "DCV 1000 V",
            "5": "FREQ kHz/MHz",
            "6": "DIODE/CONTINUITY",
            "8": "Ohm 200 Ω",
            "9": "Ohm 2 kΩ",
            "10": "Ohm 20 kΩ",
            "12": "Ohm 200 kΩ",
            "16": "Ohm 2 MΩ",
            "17": "Ohm 20 MΩ",
            "18": "Capacitance 20 μF",
            "20": "Capacitance 2 μF",
            "24": "Capacitance 200 nF",
            "32": "Capacitance 2000 pF",
            "33": "DCA 20 A",
            "34": "DCA 200 mA",
            "36": "DCA 20 mA",
            "40": "DCA 2 mA",
            "48": "DCA 200 μA",
            "64": "TEMP 200 ªF",
            "65": "TEMP 2000 ªF",
            "66": "TEMP 200 ªC",
            "68": "TEMP 1370 ªC",
            "128": "ACV 200 mV",
            "129": "ACV 2 V",
            "130": "ACV 20 V",
            "131": "ACV 200 V",
            "132": "ACV 750 V",
            "161": "ACA 20 A",
            "162": "ACA 200 mA",
            "164": "ACA 20 mA",
            "168": "ACA 2 mA",
            "176": "ACA 200 μA",
            "225": "HOLD"}
    
    if len(code) != 5:
        print('Error 01')
        return None
    elif not isinstance(code, bytes):
        print('Error 02')
        return None
    
    # Funcion aux para convertir bits a num
    bits2num = lambda bits: str(int('0b'+bits[::-1], 2))
    
    print("Measurement type:", refs[str(code[1])]) if debug else None

    s = ""
    for byte in code[2:4][::-1]:
        s += format(byte, '08b')
    print(s) if debug else None
    
    # Reglas de decodificacion
    f = int(s[-1])
    d0 = s[-2]
    d1 = s[-6:-2]
    d2 = s[-10:-6]
    d3 = s[-14:-10]
    m = s[-16:-14][::-1]
    
    mult = 10**-(int('0b'+m, 2))
    num = int(d0+bits2num(d1)+bits2num(d2)+bits2num(d3))
    signo = (-1)**(f-1)**2 # 1 --> (+), 0 --> (-)
    return num*mult*signo
    
def main():
   
    # b = [b'\x02\x84\x11\x13\x03']
    # v = getValue(b)
    # print(v)
   
    with serial.Serial('COM3', timeout=0.5) as ser:
        ser.write(b' ')     # write a string
        a = ser.readline()
        print(a)
        print(getValue(a, debug=True))

if __name__ == "__main__":
    main()