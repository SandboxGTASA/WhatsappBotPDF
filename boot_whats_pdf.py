#Import referente ao windows 7 gui
import win32con
import win32gui
#Import referente ao Selenium e Webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
#Outros imports
import time
import pandas as pd
import logging
import os.path
from grava_status import grava_status



logging.basicConfig(filename='boot_whatsapp.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(funcName)s => %(message)s')


def abre_arquivo(dir):
    # Loop até que a caixa de diálogo Open seja exibida
    hdlg = 0
    while hdlg == 0:
        hdlg = win32gui.FindWindow(None, "Abrir")

    
    # Define o nome do arquivo e pressione a tecla Enter
    hwnd = win32gui.FindWindowEx(hdlg, 0, "ComboBoxEx32", None)
    hwnd = win32gui.FindWindowEx(hwnd, 0, "ComboBox", None)
    hwnd = win32gui.FindWindowEx(hwnd, 0, "Edit", None)
    win32gui.SendMessage(hwnd, win32con.WM_SETTEXT, None, dir)
    # Pressiona o botão Salvar
    hwnd = win32gui.FindWindowEx(hdlg, 0, "Button", "&Abrir")
    win32gui.SendMessage(hwnd, win32con.BM_CLICK, None, None)


    
def env_mensagem(texto):
    # Seleciona a caixa de mensagem da conversa
    div_class = "//*[@id='main']/footer/div/div[2]/div"
    chat_box = web_driver.find_elements_by_xpath(div_class)
    chat_box[0].click()
    time.sleep(3)
    #Envia texto
    chat_box[0].send_keys(texto)
    time.sleep(3)
    send = web_driver.find_element_by_xpath(f"//span[@data-icon='send']")
    send.click()

def env_boleto_massa(nome_cliente):
        if os.path.exists(f"boletos/{nome_cliente}.pdf"):
            # Pesquisa destino em caixa de pesquisa
            caixa = web_driver.find_element_by_xpath("//*[@id='side']/div/div/label/div/div[2]")
            caixa.click()
            time.sleep(1)
            caixa.send_keys(nome_cliente)
            time.sleep(5)
            
            # Acha o destino
            contato = web_driver.find_element_by_xpath(f"//span[@title='{nome_cliente}']")
            contato.click()
            caixa.clear()
            
            # Pressiona o botão de anexo
            button = web_driver.find_elements_by_xpath("//*[@id='main']/footer/div/div/div[2]/div/div/span")
            button[0].click()
            web_driver.implicitly_wait(3)

            # Pressiona o botão de documento
            inp_xpath = "//*[@id='main']/footer/div/div/div[2]/div/span/div/div/ul/li[3]/button/span"
            button = web_driver.find_elements_by_xpath(inp_xpath)
            button[0].click()
            time.sleep(10)   # segundo. Esta pausa é necessária
            #Abre diretório de boletos
            abre_arquivo(r'C:\Users\helpdesk\Desktop\BOOT_BOLETOS\boletos')
            time.sleep(1)
            #Abre diretório de boletos (inserido caso o primeiro envio da função não execute)
            abre_arquivo(r'C:\Users\helpdesk\Desktop\BOOT_BOLETOS\boletos')
            #Abre Arquivo nome do cliente . pdf
            abre_arquivo(f'{nome_cliente}.pdf')
            time.sleep(7)
            #Localiza e clica no Botão enviar
            send = web_driver.find_element_by_xpath(f"//span[@data-icon='send']")
            send.click()
            time.sleep(2)
            #Envia Mensagem 
            env_mensagem('Segue boleto')
            grava_status(nome_cliente,'ENVIADO')
        else:
            raise FileNotFoundError
        
    

    

# Lista que contém os contatos/nome do arquivo a serem enviados.
lista_cli = ['CAMP','AxYP[GS_','123456789654321654','CAMP']
# Usando o ChromeDriver webdriver 87.x
web_driver = webdriver.Chrome(executable_path=r"C:\Users\helpdesk\Desktop\BOOT_BOLETOS\chromedriver.exe")

# Abre WhatsApp Web
web_driver.get("http://web.whatsapp.com")
web_driver.implicitly_wait(100)   # Segundos (implicitly_wait aguarda até que uma requisição seja feita ou os 100 segundos passem)

#Looping para envio conforme a quantidade de clientes
for cliente in lista_cli:
    try:
        env_boleto_massa(cliente)
        logging.debug('paramethers: cliente = {} - OK'.format(cliente))
    except FileNotFoundError:
        grava_status(cliente,'ARQUIVO NAO ENCONTRADO')
        logging.exception('paramethers: cliente = {} - ARQUIVO NAO ENCONTRADO'.format(cliente))
    except NoSuchElementException:
        grava_status(cliente,'CLIENTE NAO LOCALIZADO')
        logging.exception('paramethers: cliente = {} - CLIENTE NAO LOCALIZADO'.format(cliente))
        # Limpa caixa de pesquisa
        caixa = web_driver.find_element_by_xpath("//*[@id='side']/div/div/label/div/div[2]")
        caixa.clear()
    except:
        grava_status(cliente,'CLIENTE NAO LOCALIZADO')
        logging.exception('paramethers: cliente = {} - ERRO DESCONHECIDO'.format(cliente))



