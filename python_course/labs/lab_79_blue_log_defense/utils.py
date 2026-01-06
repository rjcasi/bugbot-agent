def analyze():
    logs = ['OK','OK','FAILED LOGIN','OK']
    for l in logs:
        if 'FAILED' in l:
            print('Alert:', l)
        else:
            print('Normal:', l)