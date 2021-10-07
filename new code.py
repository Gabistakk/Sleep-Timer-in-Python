import os
from sys import exit
from time import sleep


while (1):
    escolha = input("""Cancelar um timer já aberto [x]\n
iniciar um timer por minutos [1]\n
iniciar um timer por horas [2]\n
iniciar um timer por horas e minutos [3]\n
: """)

    if escolha == "1":
        tempo = int(input("\n\nDigite o tanto de minutos para o sleep timer executar: "))
        if tempo == 0:
            print("\n\nERRO! NÃO É POSSIVEL CONFIGURAR 0 MINUTOS, POIS O COMPUTADOR DESLIGARA NA HORA.\nO PROGRAMA SERÁ ENCERRADO.")
            sleep(5)
            exit()
        print("\n\n")
        os.system(f"shutdown -s -t {tempo * 60}")
        print(f"\nO SLEEP TIMER FOI CONFIGURADO PARA DESLIGAR DAQUI {tempo:.0f} MINUTOS.\n\n")
        sleep(2)


    elif escolha == "2":
        tempo = int(input("\n\nDigite o tanto de horas para o sleep timer executar:  "))
        if tempo == 0:
            print("\n\nERRO! NÃO É POSSIVEL CONFIGURAR 0 HORAS, POIS O COMPUTADOR DESLIGARA NA HORA.\nO PROGRAMA SERÁ ENCERRADO.")
            sleep(5)
            exit()
        print("\n\n")
        os.system(f"shutdown -s -t {(tempo * 60) * 60}")
        print(f"\nO SLEEP TIMER FOI CONFIGURADO PARA DESLIGAR DAQUI {tempo:.0f} HORAS.\n\n")
        sleep(2)


    elif escolha == 'x':
        os.system("shutdown -a")
        print("\n\nO SLEEP TIMER FOI CANCELADO.\n\n")
        sleep(2)
    
    elif escolha == '3':
        tempo1 = int(input("\n\nDigite o tanto de horas para o sleep timer executar: "))
        if tempo1 == 0:
            print("\n\nERRO! NÃO É POSSIVEL CONFIGURAR 0 HORAS/MINUTOS, POIS O COMPUTADOR DESLIGARA NA HORA.\nO PROGRAMA SERÁ ENCERRADO.")
            sleep(5)
            exit()
        tempo2 = int(input("\nDigite o tanto de minutos para o sleep timer executar: "))
        os.system(f"shutdown -s -t {(tempo1 * 60) * 60 + tempo2 * 60}")
        print(f"\n O SLEEP TIMER FOI CONFIGURADO PARA DESLIGAR DAQUI {tempo1} HORAS\nE {tempo2} MINUTOS.")
        sleep(2)

    else:
        print("\n\nERRO!\n\nDIGITE UMA DAS OPÇÕES DADAS.\n\n")
        sleep(2)
