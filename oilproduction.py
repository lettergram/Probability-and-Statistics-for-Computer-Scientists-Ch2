import numpy as np
import matplotlib.pyplot as plt

dates = [1880, 1890, 1900, 1905, 1910, 1915,\
         1920, 1925, 1930, 1935, 1940, 1945,\
         1950, 1955, 1960, 1962, 1964, 1966,\
         1968, 1970, 1972, 1974, 1976, 1978,\
         1980, 1982, 1984]

Mbbl = [30, 77, 149, 215, 328, 432, 689, 1069,\
        1412, 1655, 2150, 2595, 3804, 5626, 7674,\
        8882, 10310, 12016, 14104, 16690, 18584,\
        20389, 20188, 21922, 21732, 19403, 19608]

mean = np.mean(Mbbl)

plt.plot(dates, Mbbl, 'ro')
plt.axhline(mean)
plt.ylabel('Millions of Barrels of Crude Oil')
plt.xlabel('Year')
plt.title('Mbbl per Year')
plt.axis([1870, 1990, 0, 25000])
plt.show()
