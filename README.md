# TES-multimeter
A Python module to communicate with TES 2730 multimeter.

The function getValue decodes the incoming bytes from the multimeter and returns the numerical value. The communication should be performed separately, for example using pyserial.

Simple example:

    with serial.Serial('COM3', timeout=0.5) as ser:
        ser.write(b' ')     # ask for data
        a = ser.readline()
        print(a)
        print(getValue(a, debug=True))
