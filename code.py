import os
from time import sleep


while (1):
    escolha = input("""Cancelar um timer já aberto [x]\n
iniciar um timer por minutos [1]\n
iniciar um timer por horas [2]\n
: """)

    if escolha == "1":
        tempo = int(input("\n\nDigite o tanto de minutos para o sleep timer executar: "))
        print("\n\n")
        tempo = tempo * 60
        os.system(f"shutdown -s -t {tempo}")
        print(f"\nO SLEEP TIMER FOI CONFIGURADO PARA DESLIGAR DAQUI {tempo / 60:.0f} MINUTOS.\n\n")
        sleep(5)


    elif escolha == "2":
        tempo = int(input("\n\nDigite o tanto de horas para o sleep timer executar:  "))
        print("\n\n")
        tempo = (tempo * 60) * 60
        os.system(f"shutdown -s -t {tempo}")
        print(f"\nO SLEEP TIMER FOI CONFIGURADO PARA DESLIGAR DAQUI {(tempo / 60) / 60:.0f} HORAS.\n\n")
        sleep(5)


    elif escolha == "x":
        os.system("shutdown -a")
        print("\n\nO SLEEP TIMER FOI CANCELADO.\n\n")
        sleep(5)

    else:
        print("\n\nERRO!\n\nDIGITE UMA DAS OPÇÕES DADAS.\n\n")
        sleep(5)