import socket
import os
import subprocess

def portscan(dominio):
    portas = [21, 23, 80, 8080, 443, 22, 3306, 5432]
    for porta in portas:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.settimeout(2)
        cod = cliente.connect_ex((dominio, porta))
        if cod == 0:
            print(f'A porta {porta} está aberta.')
        else:
            print(f'A porta {porta} está fechada.')
        cliente.close()
    rf = int(input('Gostaria de voltar ao menu? (0 para sim, 1 para não.)'))

def enumerador_de_DNS(dominio, subdominio):
    endereco = f"{dominio}.{subdominio}"
    try:
        socket.gethostbyname(endereco)
        print(f"O subdomínio {endereco} existe.")
    except socket.gaierror:
        print(f"O subdomínio {endereco} não existe.")

def whois(dominio):
    info = whois(dominio)
    print("Informações de registro para o domínio", dominio)
    print("===============================================")
    print("f{dominio})

def menu():
    p = int(input('Selecione uma opcao do menu: '))
    if p == 1:
        dominio = input("Digite o domínio para realizar o portscan: ")
        portscan(dominio)
    elif p == 2:
        dominio = input("Digite a URL do site: ")
        subdominios = ['robots.txt', "sitemap.xml"]
        for subdominio in subdominios:
            enumerador_de_DNS(subdominio, dominio)
    elif p == 3:
        dominio = input("Digite a URL do site para fazer o gathering do whois: ")
        whois(dominio)
    else:
        return

print('Ola! Seja bem-vindo(a) a ferramenta all-in-one. ')
print('Codada por: @Coffee')
print('1 - Portscan para identificar portas abertas na aplicacao web: ')
print('2 - Enumerador de DNS (identificador de subdominios): ')
print('3 - whois (descobrir informações rápidas sobre a url): ')

menu()
