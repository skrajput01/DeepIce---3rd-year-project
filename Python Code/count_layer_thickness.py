import os
import numpy as np
import matplotlib.pyplot as plt

temperature_XIc = []
temperature_YPrism = []
temperature_ZBasal = []

molecules_XIc = []
molecules_YPrism = []
molecules_ZBasal = []

std_molecules_XIc = []
std_molecules_YPrism = []
std_molecules_ZBasal = []

flut_molecules_XIc = []
flut_molecules_YPrism = []
flut_molecules_ZBasal = []

# list of file names

filename = []

for object in os.listdir(os.getcwdb()):
    string_object = object.decode('utf-8')
    if ".dat" in string_object:
        filename.append(string_object)
print(filename)

for file in filename:

    results = []

    with open(file, "r") as f:

        for line in f:
            liner = str(line)
            elements = liner.split(",")
            elements = np.array([int(i) for i in elements])
            elements = abs(elements-1)
            results.append(sum(elements))

        value, deviation = np.mean(results), np.std(results)

        if "XIc" in file:
            temperature_XIc.append(int(file[-8:-5]))
            std_molecules_XIc.append(deviation)
            molecules_XIc.append(value)
            flut_molecules_XIc.append(results)
        elif "Yprism1" in file:
            temperature_YPrism.append(int(file[-8:-5]))
            std_molecules_YPrism.append(deviation)
            molecules_YPrism.append(value)
            flut_molecules_YPrism.append(results)
        elif "Zbasal" in file:
            temperature_ZBasal.append(int(file[-8:-5]))
            std_molecules_ZBasal.append(deviation)
            molecules_ZBasal.append(value)
            flut_molecules_ZBasal.append(results)
        else:
            "There is a bug!!"

def order(x, y):
    xnew = x.copy()
    xnew.sort()
    ynew = []
    for element in xnew:
        for index, value in enumerate(x):
            if value == element:
                ynew.append(y[index])
    return xnew, ynew


from scipy.optimize import curve_fit

xict, ypt, zbt = temperature_XIc.copy(), temperature_YPrism.copy(), temperature_ZBasal.copy()
time = [i/4 for i in range(401)]
temperature_XIc, molecules_XIc = order(xict, molecules_XIc)
temperature_XIc, std_molecules_XIc = order(xict, std_molecules_XIc)
temperature_XIc, flut_molecules_XIc = order(xict, flut_molecules_XIc)
temperature_YPrism, molecules_YPrism = order(ypt, molecules_YPrism)
temperature_YPrism, std_molecules_YPrism = order(ypt, std_molecules_YPrism)
temperature_YPrism, flut_molecules_YPrism = order(ypt, flut_molecules_YPrism)
temperature_ZBasal, molecules_ZBasal = order(zbt, molecules_ZBasal)
temperature_ZBasal, std_molecules_ZBasal = order(zbt, std_molecules_ZBasal)
temperature_ZBasal, flut_molecules_ZBasal = order(zbt, flut_molecules_ZBasal)

n = 1/2*2.989*10

fXIc, fYPrism, fZBasal = n/1721, n/1828, n/1705
molecules_XIc, std_molecules_XIc = fXIc*np.array(molecules_XIc), fXIc*np.array(std_molecules_XIc)
molecules_YPrism, std_molecules_YPrism = fYPrism*np.array(molecules_YPrism), fYPrism*np.array(std_molecules_YPrism)
molecules_ZBasal, std_molecules_ZBasal = fZBasal*np.array(molecules_ZBasal), fZBasal*np.array(std_molecules_ZBasal)

def exponential(x, a, b, c):
    return a*b**x + c

from scipy.optimize import curve_fit

XIc = curve_fit(exponential, temperature_XIc, molecules_XIc, maxfev = 20000)
YPrism = curve_fit(exponential, temperature_YPrism, molecules_YPrism, maxfev = 20000)
ZBasal = curve_fit(exponential, temperature_ZBasal, molecules_ZBasal, maxfev = 20000)

print(XIc, YPrism, ZBasal)

bestXIc = [exponential(t, XIc[0][0], XIc[0][1],XIc[0][2]) for t in np.linspace(min(temperature_XIc), max(temperature_XIc), 1000)]
bestYPrism = [exponential(t, YPrism[0][0], YPrism[0][1],YPrism[0][2]) for t in np.linspace(min(temperature_YPrism), max(temperature_YPrism), 1000)]
bestZBasal = [exponential(t, ZBasal[0][0], ZBasal[0][1],ZBasal[0][2]) for t in np.linspace(min(temperature_ZBasal), max(temperature_ZBasal), 1000)]

fig, ax = plt.subplots(1,3)
ax=ax.flatten()

ax[0].grid(linestyle="--", c="#ddc7c9")
ax[0].errorbar(temperature_XIc, molecules_XIc, std_molecules_XIc,\
    fmt= 'o', color = "k", ecolor="#fc9802", capthick=1, capsize=3)
ax[0].plot(np.linspace(min(temperature_XIc), max(temperature_XIc), 1000), bestXIc, '-', c="#570f08", label="MolC Method")
ax[0].set_xlabel("Temperature ($K$)")
ax[0].set_ylabel("QLL Thickness ($\AA$)")
#ax[0].set_yticks(np.arange(0, 10, 1))
#ax[0].legend()
#plt.show()

ax[1].grid(linestyle="--", c="#ddc7c9")
ax[1].errorbar(temperature_YPrism, molecules_YPrism, std_molecules_YPrism,\
    fmt= 'o', color = "k", ecolor="#fc9802", capthick=1, capsize=3)
ax[1].plot(np.linspace(min(temperature_YPrism), max(temperature_YPrism), 1000), bestYPrism, '-', c="#570f08")
ax[1].set_xlabel("Temperature ($K$)")
ax[1].set_ylabel("QLL Thickness ($\AA$)")
#ax[1].set_yticks(np.arange(0, 10, 1))
#ax[1].legend()
#plt.show()

ax[2].grid(linestyle="--", c="#ddc7c9")
ax[2].errorbar(temperature_ZBasal, molecules_ZBasal, std_molecules_ZBasal,\
    fmt= 'o', color = "k", ecolor="#fc9802", capthick=1, capsize=3)
ax[2].plot(np.linspace(min(temperature_ZBasal), max(temperature_ZBasal), 1000), bestZBasal, '-', c="#570f08")
ax[2].set_xlabel("Temperature ($K$)")
ax[2].set_ylabel("QLL Thickness ($\AA$)")
#ax[2].set_yticks(np.arange(0, 10, 1))
#ax[2].legend()
#plt.show()


n = 1

fXIc, fYPrism, fZBasal = 87.422500/5488/fXIc,86.925000/5760/fYPrism, 88.335/5760/fZBasal
molecules_XIc, std_molecules_XIc = fXIc*np.array(molecules_XIc), fXIc*np.array(std_molecules_XIc)
molecules_YPrism, std_molecules_YPrism = fYPrism*np.array(molecules_YPrism), fYPrism*np.array(std_molecules_YPrism)
molecules_ZBasal, std_molecules_ZBasal = fZBasal*np.array(molecules_ZBasal), fZBasal*np.array(std_molecules_ZBasal)

def exponential(x, a, b, c):
    return a*b**x + c

from scipy.optimize import curve_fit

XIc = curve_fit(exponential, temperature_XIc, molecules_XIc, maxfev = 20000)
YPrism = curve_fit(exponential, temperature_YPrism, molecules_YPrism, maxfev = 20000)
ZBasal = curve_fit(exponential, temperature_ZBasal, molecules_ZBasal, maxfev = 20000)

print(XIc, YPrism, ZBasal)

bestXIc = [exponential(t, XIc[0][0], XIc[0][1],XIc[0][2]) for t in np.linspace(min(temperature_XIc), max(temperature_XIc), 1000)]
bestYPrism = [exponential(t, YPrism[0][0], YPrism[0][1],YPrism[0][2]) for t in np.linspace(min(temperature_YPrism), max(temperature_YPrism), 1000)]
bestZBasal = [exponential(t, ZBasal[0][0], ZBasal[0][1],ZBasal[0][2]) for t in np.linspace(min(temperature_ZBasal), max(temperature_ZBasal), 1000)]


#ax[0].grid(linestyle="--", c="#ddc7c9")
ax[0].errorbar(temperature_XIc, molecules_XIc, std_molecules_XIc,\
    fmt= 'o', color = "k", ecolor="#3f60f5", capthick=1, capsize=3)
ax[0].plot(np.linspace(min(temperature_XIc), max(temperature_XIc), 1000), bestXIc, '-', c="#3f60f5", label="MC Method")
ax[0].set_xlabel("Temperature ($K$)")
ax[0].set_ylabel("QLL Thickness ($\AA$)")
ax[0].set_yticks(np.arange(0, 10, 1))
ax[0].legend()
#plt.show()

#ax[1].grid(linestyle="--", c="#ddc7c9")
ax[1].errorbar(temperature_YPrism, molecules_YPrism, std_molecules_YPrism,\
    fmt= 'o', color = "k", ecolor="#3f60f5", capthick=1, capsize=3)
ax[1].plot(np.linspace(min(temperature_YPrism), max(temperature_YPrism), 1000), bestYPrism, '-', c="#3f60f5")
ax[1].set_xlabel("Temperature ($K$)")
ax[1].set_ylabel("QLL Thickness ($\AA$)")
ax[1].set_yticks(np.arange(0, 10, 1))
#ax[1].legend()
#plt.show()

#ax[2].grid(linestyle="--", c="#ddc7c9")
ax[2].errorbar(temperature_ZBasal, molecules_ZBasal, std_molecules_ZBasal,\
    fmt= 'o', color = "k", ecolor="#3f60f5", capthick=1, capsize=3)
ax[2].plot(np.linspace(min(temperature_ZBasal), max(temperature_ZBasal), 1000), bestZBasal, '-', c="#3f60f5")
ax[2].set_xlabel("Temperature ($K$)")
ax[2].set_ylabel("QLL Thickness ($\AA$)")
ax[2].set_yticks(np.arange(0, 10, 1))
#ax[2].legend()

ax[0].set_title("$I_c$ (100)")
ax[1].set_title("$I_h$ (1$\overline{1}$00)")
ax[2].set_title("$I_h$ (0001)")
plt.show()