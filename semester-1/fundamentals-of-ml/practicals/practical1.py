import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = np.array([10, 20, 30, 40, 50])

print(a)

df = pd.DataFrame({
    "Student": ["A", "B", "C", "D"],
    "Marks":[70, 80, 90, 85]
})

print(df)

plt.plot(df["Marks"])
plt.title("Marks")
plt.show()
