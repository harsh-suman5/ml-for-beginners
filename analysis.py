import pandas as pd
import matplotlib.pyplot as plt
data  = pd.DataFrame({"cigrates":[0,10,20,30],
                     "CVD": [572,802,892,1025],
"lung": [14,105,208,355]});
plt.ylabel("CVD deaths")
data.plot("cigarettes", "CVD", kind="scatter")
plt.title("Deaths for different smoking intensities")
plt.xlabel("Cigarettes smoked per day")