def polar_rz(input_digital_signal):
    digital_signal=list(input_digital_signal)
    digital_signal=[-1 if i==0 else 1 for i in digital_signal]
    output_digital_signal=[]
    for i in range(len(digital_signal)):
        output_digital_signal.append(digital_signal[i])
        output_digital_signal.append(0)
    return output_digital_signal