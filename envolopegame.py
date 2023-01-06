import numpy as np

# Settings
envelopelen = 100
valuerange = 100
percentage = 37

# Code
maxnum = 0
endvalue = 0
envelope = []
for i in range(envelopelen): envelope.append(np.random.randint(0, valuerange))
for i in range(len(envelope)):
    if (int((envelopelen/100)*percentage) >= i):
        if (maxnum < envelope[i]):
            maxnum = envelope[i]
    else:
        if(envelope[i] >= maxnum and endvalue < envelope[i]):
            endvalue = envelope[i]
        if (i == len(envelope)-1 and endvalue == 0):
            endvalue = envelope[i]

# Output
print("The envelope: \n" + str(envelope) + "\n\nThe first " + str(percentage) + "% part of the envelope: \n" + str(envelope[0:int((envelopelen/100)*percentage)]) + "\n\nThe second part of the envelope: \n" + str(envelope[int((envelopelen/100)*percentage):]))
print("\nThe maxium value from the " + str(percentage) + "% was: " + str(maxnum))
print("Our take from the envelope: " + str(endvalue))