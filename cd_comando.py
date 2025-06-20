import os

def cd(ra, rp, comando, usuario, integrantes):
    if len(comando) != 2:
        total = len(comando)
        print(f'El comando cd debe tener un solo argumento.\nTiene {total} argumentos.\nArgumentos: {comando}')
        return

    if comando[1] == '-' and len(comando) == 2:
        lista = ra.split('/')
        lista.pop(-1)
        rn = '/'.join(lista)
        print(rn)
        if ra == rp:
            print('Devolver ruta padre')
            integrantes[usuario] = rp
        else:
            print(f'Nueva ubicación: {rn}')
            integrantes[usuario] = rn
            
    elif comando[1] == '~' and len(comando) == 2:
        rn = rp
        integrantes[usuario] = rn
        print(f'Nueva ubicación: {rn}')

    elif len(comando) == 2 and comando[1] != '-' and comando[1] != '/' and comando[1] != '~':
        print('else')
        concatenar = ra + '/' + comando[1]
        reemplazar = concatenar.replace('//', '/').replace('///', '/')

if name == 'main':
    rp = os.getcwd()
    dicionario = {153: '/storage/emulated/0'}
    ra = dicionario[153]
    comando = ['cd', 'ppp']  # Cambia aquí para probar diferentes comandos

    print(f'Ruta padre: {rp}')
    print(f'Ruta actual: {ra}')
        
    print('Método "cd"')
    cd(ra, rp, comando, 153, dicionario)
    print(f'Ruta padre: {rp}')
    print(f'Ruta actual: {ra}')
    print(dicionario)