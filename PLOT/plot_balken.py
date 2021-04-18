import matplotlib.pyplot as plt
import numpy as np
f = plt.figure()
production_level = [54, 83, 21, 3] #list_of_prod
periods = [x+1 for x in range(len(production_level))] #list_of_order

plt.bar(periods, production_level, color="orange")

plt.title("Dynamic lot-size problem chart")
plt.ylabel("Units")
plt.xlabel("Periods")
plt.grid(True)

plt.show()
#f.savefig("bar.png", bbox_inches="tight")