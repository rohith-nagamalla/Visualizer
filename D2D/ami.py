def AMI(input_digital_signal):
    digital_signal=list(input_digital_signal)
    digital_signal.insert(0,0)
    lock=False
    for i in range(len(digital_signal)):
        if digital_signal[i]==1 and not lock:
            lock=True
            continue
        elif lock and digital_signal[i]==1:
            digital_signal[i]=-1
            lock=False
    return digital_signal