import csv
import datetime

#Inicio do nome do arquivo (data_mes_ano_hora_minuto_segundo)
inicio = datetime.datetime.now()
inicio = inicio.strftime("%d%m%Y_%H_%M_%S")

#Abre e grava Cliente, Status e Hora em um arquivo .csv
def grava_status(cli, status,):
        with open(f'{inicio}_LOG_STATUS.csv', 'a', newline='') as arquivo_csv:
            colunas = ['CLIENTE', 'STATUS','HORA']
            escrever = csv.DictWriter(arquivo_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
            escrever.writeheader()
            escrever.writerow({'CLIENTE': cli, 'STATUS': status, 'HORA':datetime.datetime.now().strftime("%H:%M:%S")})
