def detect():
    values = [10, 12, 11, 50, 13]
    avg = sum(values)/len(values)
    for v in values:
        if abs(v - avg) > 20:
            print('Anomaly:', v)
        else:
            print('Normal:', v)