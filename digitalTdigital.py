from D2D.unipolar import unipolar
from D2D.polar_nrz_l import polar_nrz_l
from D2D.polar_nrz_i import polar_nrz_i
from D2D.polar_rz import polar_rz
from D2D.biphase_manchester import Biphase_manchester
from D2D.differential_manchester import Differential_manchester
from D2D.ami import AMI

import matplotlib.pyplot as plt

def plot(li):
    plt.subplot(7,1,1)
    plt.ylabel("Unipolar-NRZ")
    plt.plot(unipolar(li),color='red',drawstyle='steps-pre',marker='>')
    plt.subplot(7,1,2)
    plt.ylabel("P-NRZ-L")
    plt.plot(polar_nrz_l(li),color='blue',drawstyle='steps-pre',marker='>')
    plt.subplot(7,1,3)
    plt.ylabel("P-NRZ-I")
    plt.plot(polar_nrz_i(li),color='green',drawstyle='steps-pre',marker='>')
    plt.subplot(7,1,4)
    plt.ylabel("Polar-RZ")
    plt.plot(polar_rz(li),color='red',drawstyle='steps-pre',marker='>')
    plt.subplot(7,1,5)
    plt.ylabel("B_Man")
    plt.plot(Biphase_manchester(li),color='violet',drawstyle='steps-pre',marker='>')
    plt.subplot(7,1,6)
    plt.ylabel("Dif_Man")
    plt.plot(Differential_manchester(li),color='red',drawstyle='steps-pre',marker='>')
    plt.subplot(7,1,7)
    plt.ylabel("A-M-I")
    plt.plot(AMI(li),color='blue',drawstyle='steps-pre',marker='>')
    plt.show()