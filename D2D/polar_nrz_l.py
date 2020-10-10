def polar_nrz_l(input_digital_signal):
    digital_signal = list(input_digital_signal)
    digital_signal.insert(0,0)
    digital_signal = [-1 if i==0 else 1 for i in digital_signal]
    return digital_signal
    