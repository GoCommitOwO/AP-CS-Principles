#calculate the parallel resistance of
#three loads (1st 3 inputs from user)
#placed across a voltage source (4th and final input)

#equal to voltage divided by resistance
#or I = V/R

#given in amperes, volts, and ohms.

#for example, if we have a 5V battery and an LED
#with a resistence of 1000 ohms, the resulting
#current through the LED is 5/1000 (V/Ohms) =
#0.005 Amps.

R1 = int(input("Resistance 1: "))
R2 = int(input("Resistance 2: "))
R3 = int(input("Resistance 3: "))

V = float(input("Voltage: "))

Current1 = V / R1
Current2 = V / R2
Current3 = V / R3

CurrentSum = Current1 + Current2 + Current3

ParallelResistance = V / CurrentSum



print("The parallel resistance is: " + str(round(ParallelResistance, 2)) + " ohms.")