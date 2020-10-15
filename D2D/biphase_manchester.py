def Biphase_manchester(input_digital_signal):
    digital_signal=list(input_digital_signal)
    output_digital_signal,init=[],False
    for i in range(len(digital_signal)):
        if digital_signal[i]==0:
            output_digital_signal.append(-1)
            if not init:
                output_digital_signal.append(-1)
                init=True
            output_digital_signal.append(1)
        elif digital_signal[i]==1 :
            output_digital_signal.append(1)
            output_digital_signal.append(-1)
    # output_digital_signal.insert(0,0)
    return output_digital_signal 