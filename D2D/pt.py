def pt(input_digital_signal):
    digital_signal=list(input_digital_signal)
    digital_signal.insert(0,0)
    lock=False
    for i in range(len(digital_signal)):
        if digital_signal[i]==0 and not lock:
            digital_signal[i]=1
            lock=True
        elif lock and digital_signal[i]==0:
            digital_signal[i]=-1
            lock=False
        elif digital_signal[i]==1:
            digital_signal[i]=0
    return digital_signal