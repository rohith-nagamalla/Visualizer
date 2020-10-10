def polar_nrz_i(input_digital_signal):
    digital_signal=list(input_digital_signal)
    lock=False
    for i in range(len(digital_signal)):
        if digital_signal[i]==1 and not lock:
            lock=True
            continue
        if lock and digital_signal[i]==1:
            if digital_signal[i-1]==0:
                digital_signal[i]=1
                continue
            else :
                digital_signal[i]=0
                continue
        if lock:
            digital_signal[i]=digital_signal[i-1]
    digital_signal=[-1 if i==0 else 1 for i in digital_signal]        
    return digital_signal