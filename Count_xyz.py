import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy

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


def exponential(x, a, b, c):
    return a*b**x + c


# scipy.optimize.curve_fit(f, xdata, ydata, p0=None, sigma=None, absolute_sigma=False, check_finite=True, bounds=(- inf, inf), method=None, jac=None, **kwargs)
# scipy.optimize.

XIc = curve_fit(exponential, temperature_XIc, molecules_XIc, p0=None, sigma=None, maxfev=20000)
YPrism = curve_fit(exponential, temperature_YPrism, molecules_YPrism, p0=None, sigma=None, maxfev=20000)
ZBasal = curve_fit(exponential, temperature_ZBasal, molecules_ZBasal, p0=None, sigma=None, maxfev=20000)

print(XIc, YPrism, ZBasal)

bestXIc = [exponential(t, XIc[0][0], XIc[0][1], XIc[0][2]) for t in np.linspace(min(temperature_XIc), max(temperature_XIc), 1000)]
bestYPrism = [exponential(t, YPrism[0][0], YPrism[0][1], YPrism[0][2]) for t in np.linspace(min(temperature_YPrism), max(temperature_YPrism), 1000)]
bestZBasal = [exponential(t, ZBasal[0][0], ZBasal[0][1], ZBasal[0][2]) for t in np.linspace(min(temperature_ZBasal), max(temperature_ZBasal), 1000)]

plt.rcParams['font.size'] = '16'
# Best fit X
plt.grid(linestyle="--", c="#000000")
plt.errorbar(temperature_XIc, molecules_XIc, std_molecules_XIc, fmt='o', color="#2C9A26", ecolor="#00F2A1", capthick=1, capsize=3, label="XIc")
plt.plot(np.linspace(min(temperature_XIc), max(temperature_XIc), 1000), bestXIc, '-', c="#2C9A26", label="XIc LoBF")
"""plt.xlabel("Temperature [K]")
plt.ylabel("Number of Water Molecules")
plt.legend()
plt.show()"""


# Best fit Y
plt.grid(linestyle="--", c="#000000")
plt.errorbar(temperature_YPrism, molecules_YPrism, std_molecules_YPrism, fmt='o', color="#AA00AA", ecolor="#FF00FF", capthick=1, capsize=3, label="YPrism")
plt.plot(np.linspace(min(temperature_YPrism), max(temperature_YPrism), 1000), bestYPrism, '-', c="#AA00AA", label="YPrism LoBF")
"""plt.xlabel("Temperature [K]")
plt.ylabel("Number of Water Molecules")
plt.legend()
plt.show()"""

# Best fit Z
plt.grid(linestyle="--", c="#000000")
plt.errorbar(temperature_ZBasal, molecules_ZBasal, std_molecules_ZBasal, fmt='o', color="#00AAAA", ecolor="#00FFFF", capthick=1, capsize=3, label="ZBasal")
plt.plot(np.linspace(min(temperature_ZBasal), max(temperature_ZBasal), 1000), bestZBasal, '-', c="#00AAAA", label="ZBasal LoBF")
plt.xlabel("Temperature [K]", fontweight="bold")
plt.ylabel("Number of Water Molecules", fontweight="bold")
plt.title("XIc, YPrism, ZBasal", fontweight="bold")
plt.legend()
plt.xlim([195, 275])
plt.ylim([0, 550])
plt.show()
print(temperature_XIc)
print(molecules_XIc)

# XIc - Temp
# colors_x = ["#7030A0", "#002060", "#0070C0", "#00B0F0", "#006600", "#92D050", "#FFC000", "#FF0000"]
colors_x = ["#FF0000", "#FF9900", "#F0F00F", "#007700", "#00CCFF", "#0000FF", "#9999FF", "#6600FF"]
for value, temperature, color in zip(flut_molecules_XIc[::-1], temperature_XIc[::-1], colors_x):
    plt.grid(linestyle="--", c="#000000")
    plt.plot(time, value[:401], '-', c=color, label=f"${temperature}K$")
    plt.xlabel("Time [ns]", fontweight="bold")
    plt.ylabel("Number of Water Molecules", fontweight="bold")
plt.title("XIc", fontweight="bold")
plt.legend(loc=1, prop={'size': 10})
plt.xlim([0, 100])
plt.ylim([0, 800])
plt.show()


# YPrism - Temp
# original colors_y = ["#e64a50", "#ddc7c9", "#3f60f5", "#030838", "#fc9802", "#f4dc76", "#d75a13", "#570f08"]
colors_y = ["#FF0000", "#990033", "#FF9900", "#995500", "#F0F00F", "#AAFF00", "#007700"]
for value, temperature, color in zip(flut_molecules_YPrism[::-1], temperature_YPrism[::-1], colors_y):
    plt.grid(linestyle="--", c="#000000")
    plt.plot(time, value[:401], '-', c=color, label=f"${temperature}K$")
    plt.xlabel("Time [ns]", fontweight="bold")
    plt.ylabel("Number of Water Molecules", fontweight="bold")
plt.title("YPrism", fontweight="bold")
plt.legend(loc=1, prop={'size': 10})
plt.xlim([0, 100])
plt.ylim([0, 800])
plt.show()

# ZBasal - Temp
# original colors_z = ["#e64a50", "#ddc7c9", "#3f60f5", "#030838", "#fc9802", "#f4dc76", "#d75a13", "#570f08"]
colors_z = ["#FF0000", "#990033", "#FF9900", "#995500", "#F0F00F", "#AAFF00", "#007700"]
for value, temperature, color in zip(flut_molecules_ZBasal[::-1], temperature_ZBasal[::-1], colors_z):
    plt.grid(linestyle="--", c="#000000")
    plt.plot(time, value[:401], '-', c=color, label=f"${temperature}K$")
    plt.xlabel("Time [ns]", fontweight="bold")
    plt.ylabel("Number of Water Molecules", fontweight="bold")
plt.title("ZBasal", fontweight="bold")
plt.legend(loc=1, prop={'size': 10})
plt.xlim([0, 100])
plt.ylim([0, 800])
plt.show()

