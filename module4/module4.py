# %%
import matplotlib.pyplot as plt
import numpy as np

# %%
def step_function(s):
    return np.array(s > 0).astype(int)

# %%
x = np.arange(-10, 10, 0.1)
y = step_function(x)

# %%
plt.plot(x, y)
plt.show()


