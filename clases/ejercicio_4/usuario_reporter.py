from usuario import Usuario

class Reporter(Usuario):
    def __init__(self,email, nombre, apellido, password,sistema):
        Usuario.__init__(self, email, nombre, apellido, password, sistema)
        self.level = 'reporter'

    def verCarritos(self):
        todosLosCarritos = []
        total=0
        for usuario in self.sistema.listaUsuarios:
            if usuario.level == 'cliente':
                todosLosCarritos.extend(usuario.carrito.listaDeCompras)
        print('-'.center(84,'-'))
        print('Codigo'.ljust(10),' - ','Nombre'.rjust(30),' : ','Precio'.ljust(11),' - ','Cantidad'.rjust(15))
        for producto in todosLosCarritos:
            producto.print()
            total+=producto.precio*producto.cantidad
        print( ' ')
        print('El total vendido es ARS$ ',total)
        print('-'.center(84,'-'))



    def menuReporter(self):
        opcion=0
        while opcion != 99:
            print('-'.center(84,'-'))
            print(' 1  -  Ver Carritos de Compra')
            print(' 99 -  Terminar y Salir')
            print('-'.center(84,'-'))
            opcion=int(input('ingrese la opcipn deseada: '))

            if opcion == 1:
                print(' ')
                print('-'.center(84,'-'))
                self.verCarritos()
                print('-'.center(84,'-'))
                print(' ')
            else:
                print(' ')
                print(' hasta la proxima')
                opcion=99
                break
            
            print(' ')
            print('-'.center(84,'-'))
            tecla=input ('presione retorno (enter) para continuar...')
            print(' ')
            if tecla != None or tecla == None : 
                print('volviendo al menú...')
            print(' ')


     #Llamo al metodo del objeto que contiene la lista de carritos