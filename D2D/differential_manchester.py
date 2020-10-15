def Differential_manchester(input_digital_signal):
    digital_signal=list(input_digital_signal)
    output_digital_signal,lock,pre=[],False,'S'
    for i in range(len(digital_signal)):
        # if digital_signal[i]==0 and not lock:
        #     output_digital_signal.append(-1)
        #     output_digital_signal.append(-1)
        #     output_digital_signal.append(1)
        #     lock=True
        #     pre='S'
        # elif digital_signal[i]==1 and not lock :
        #     output_digital_signal.append(1)
        #     output_digital_signal.append(1)
        #     output_digital_signal.append(-1)
        #     lock=True
        #     pre='Z'
        # else:
        #     if digital_signal[i]==1:
        #         if pre=='S':
        #             output_digital_signal.append(-1);output_digital_signal.append(1)
        #         else:
        #             output_digital_signal.append(1);output_digital_signal.append(-1)
        #     else:
        #         if pre=='Z':
        #             pre='S'
        #             output_digital_signal.append(-1);output_digital_signal.append(1)
        #         else:
        #             pre='Z'
        #             output_digital_signal.append(1);output_digital_signal.append(-1)
        if digital_signal[i]==0:
            if pre=='S':
                output_digital_signal.append(-1);output_digital_signal.append(1)
            else:
                output_digital_signal.append(1);output_digital_signal.append(-1)
        else:
            if pre=='Z':
                pre='S'
                output_digital_signal.append(-1);output_digital_signal.append(1)
            else:
                pre='Z'
                output_digital_signal.append(1);output_digital_signal.append(-1)
    output_digital_signal.insert(0,1)
                         
    return output_digital_signal  