from app.interface.console.console import menu_principal, menu_administrativo, menu_funcionario
from app.utils.utilitarios_global import limpar_console

def inicializar_cafeteria():
    limpar_console()
    print('\n' + '☕👥 BEM-VINDO À CAFÉ VOYAGE  👥☕'.center(50, '='))
    print('=' * 50)
    print('Você é:')
    print('1️⃣  Cliente')
    print('2️⃣  Garçom')
    print('3️⃣  Gerente')
    print('0️⃣  Sair')
    print('=' * 50)

    while True:
        try:
            opcao = int(input('👉 Digite sua opção: '))
            if opcao in (0, 1, 2, 3):
                break
            else:
                print('❌ Opção inválida! Digite um número entre (0, 1, 2)')
        except ValueError:
            print('❌ Opção inválida! Digite um número.')
            
    if opcao == 1:
        menu_principal()
    elif opcao == 2:
        menu_funcionario()
    elif opcao == 3:
        menu_administrativo()
    elif opcao == 0:
        print('\n👋 Até logo! Obrigado por visitar o Café Voyage.\n')
    else:
        print('⚠️ Opção inválida. Tente novamente.')
    
if __name__ == "__main__":
    inicializar_cafeteria()
    
        