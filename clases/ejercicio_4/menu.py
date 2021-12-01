
class menu():

    def login():
        print(' ')
        print('-'.center(84,'-'))
        email = input('ingrese su email: ')
        password = input('ingrese su password: ')
        print('-'.center(84,'-'))
        print(' ')
        usuarioActual=main.retornaUsuario(email,password)
        usuarioActual.print()
        if usuarioActual.level == 'cliente':
            usuarioActual.menuOpciones()
        elif usuarioActual.level == 'admin':
            usuarioActual.menuAdmin()
        elif usuarioActual.level == 'reporter':
            usuarioActual.menuReporter()
    
    
    def deslog():
        login()
    
    def registrarse():
        pass
    
    def salirSistema():
        exit()

    opcion = []

    while opcion != 0:
        print('-'.center(84,'-'))
        print("Para loguearse ingrese 1.")
        print("Para registrarse ingrese 2.")
        print("Para desloguearse ingrese 3.")
        print("Para salir ingrese 0.")
        print('-'.center(84,'-'))
        opcion = int(input("Ingrese su opción.")
        
        if (opcion == 1):
            login()
        elif opcion == 2:
            registrarse()
        elif opcion == 3:
            deslog()
        elif opcion == 4:
            salirSistema()
