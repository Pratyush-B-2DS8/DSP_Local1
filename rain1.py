import numpy as np

file = "ds_practice/all-india-monthly-rainfall.csv"


x = np.genfromtxt(file, dtype=float, delimiter=",", skip_header=1)[:, 1:]

#Yearly
y_max = np.max(x, axis=1)
y_min = np.min(x, axis=1)
y_mean= np.mean(x, axis=1)

#Monthly
m_max = np.max(x, axis=0)
m_min = np.min(x, axis=0)
m_mean= np.mean(x, axis=0)

#Overall
o_mean = np.mean(x)
o_std = np.std(x)

#Months with avg + 0.5 std
my_high = np.where(x[x>(o_mean+(0.5*o_std))])
print(my_high)



#np.savetxt
#np.save
#np.savez