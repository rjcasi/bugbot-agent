def map_surface():
    print('Mapping attack surface...')
    endpoints = ['/','/login','/api/test','/upload']
    for e in endpoints:
        print('Found endpoint:', e)