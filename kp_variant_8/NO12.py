def f(n:str):
    while any(('01' in n, '02' in n, '03' in n)):
        n = n.replace('01', '302').replace('02', '3103').replace('03', '20')
