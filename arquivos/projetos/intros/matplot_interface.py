import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,10)

plt.style.use("ggplot")
print(plt.style.available)

fig = plt.figure()
ax = fig.add_axes([0,0,0.48,1])
ax_two = fig.add_axes([0.5,0,0.5,1])
ax.plot()
ax_two.plot()

ax = fig.add_axes([0,0,1,1])
ax_two = fig.add_axes([0.15,0.7,0.25,0.25])
ax.plot(x,x**2,color="r")
ax_two.plot(x,np.log(x),ls="--")

fig.suptitle("Major Title")
ax = fig.add_axes([0,0,0.45,0.9])
ax.set_title("x raised to a power")
ax.set_xlabel("x values")
ax.set_ylabel("y values")
ax_two = fig.add_axes([0.5,0,0.45,0.9])
ax_two.set_title("x square")
ax_two.set_xlabel("x values")
ax_two.set_yticks([0,1,2])
ax.plot(x,x**2, color="blue",label="x squared")
ax.plot(x,x**3, color="black",label="x cubed")
ax_two.plot(x,np.log(x),color="r")
ax.legend(loc="best")

fig,(ax_one,ax_two,ax_three,ax_four) = plt.subplots(nrows=4,ncols=1,sharex=True)
ax_one.plot(x,x**2)
ax_two.plot(x,x**3)
ax_three.plot(x,4*x)
ax_four.plot(x,x**(1/2))

fig,(ax_one,ax_two,ax_three,ax_four) = plt.subplots(nrows=2,ncols=2,sharex=True)
ax_one = plt.subplot(221)
ax_two = plt.subplot(222)
ax_three = plt.subplot(223)
ax_four = plt.subplot(224)
ax_one.plot(x,x**2)
ax_two.plot(x,x**3)
ax_three.plot(x,4*x)
ax_four.plot(x,x**(1/2))
