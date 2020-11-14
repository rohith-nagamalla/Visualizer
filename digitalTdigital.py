from D2D.unipolar import unipolar
from D2D.polar_nrz_l import polar_nrz_l
from D2D.polar_nrz_i import polar_nrz_i
from D2D.polar_rz import polar_rz
from D2D.biphase_manchester import Biphase_manchester
from D2D.differential_manchester import Differential_manchester
from D2D.ami import AMI
from D2D.pt import pt

import matplotlib.pyplot as plt

def plot(li,option):
    display = list(li)
    display.insert(0,0)
    display = [0 if i==0 else 1 for i in display]
    plt.subplot(2,1,1)
    plt.ylabel("INPUT")
    plt.plot(display,drawstyle='steps-pre',marker='>')
    plt.grid(True)
    if option==1:
        plt.subplot(2,1,2)
        plt.ylabel("Unipolar-NRZ")
        plt.plot(unipolar(li),drawstyle='steps-pre',marker='>')
        plt.grid(True)
        plt.show()
    elif option==2:
        plt.subplot(2,1,2)
        plt.ylabel("P-NRZ-L")
        plt.plot(polar_nrz_l(li),drawstyle='steps-pre',marker='>')
        plt.grid(True)
        plt.show()
    elif option==3:
        plt.subplot(2,1,2)
        plt.ylabel("P-NRZ-I")
        plt.plot(polar_nrz_i(li),drawstyle='steps-pre',marker='>')
        plt.grid(True)
        plt.show()
    elif option==4:
        plt.subplot(2,1,2)
        plt.ylabel("Polar-RZ")
        plt.plot(polar_rz(li),drawstyle='steps-pre',marker='>')
        plt.grid(True)
        plt.show()
    elif option==5:
        plt.subplot(2,1,2)
        plt.ylabel("B_Man")
        plt.plot(Biphase_manchester(li),drawstyle='steps-pre',marker='>')
        plt.grid(True)
        plt.show()
    elif option==6:
        plt.subplot(2,1,2)
        plt.ylabel("Dif_Man")
        plt.plot(Differential_manchester(li),drawstyle='steps-pre',marker='>')
        plt.grid(True)
        plt.show()
    elif option==7:
        plt.subplot(2,1,2)
        plt.ylabel("A-M-I")
        plt.plot(AMI(li),drawstyle='steps-pre',marker='>')
        plt.grid(True)
        plt.show()
    else:
        plt.subplot(2,1,2)
        plt.ylabel("Pseudoternary")
        plt.plot(pt(li),drawstyle='steps-pre',marker='>')
        plt.grid(True)
        plt.show()