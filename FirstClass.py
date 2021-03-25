
def outer_fun(msg):
    '''Función nulita, solamenta probando algo de First-class'''
    message=msg

    def inner_fun():
        print(message)
    
    return inner_fun


fun= outer_fun('Chola')

'''En este caso se observa que la función de afuera usa los parámetros de la función
de adentro. 
'''

'''Ahhh'''