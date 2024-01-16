from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
while 1:
        driver.get("https://web.whatsapp.com")
        time.sleep(3)
        print("FAÇA LOGIN NO WPP WEB")
        input("Aperte Enter apos estar logado: ")
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/header/div[1]/div')
        
        print("Iniciando a Verificação dos contatos")

        with open("contatos.txt") as file:
            for line in file:
                print(line)
                numero = line
                url = "https://web.whatsapp.com/send?phone={}".format(numero)
                driver.get(url)
                time.sleep(20)
                print("Validando numero...")
                try:
                    #driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
                    j1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]').text
                    if 'inválido' in j1:
                        print("Numero invalido")

                        f = open("invalidos.txt", "a")
                        f.write(numero)
                        f.close()
                    else:
                        f = open("validos.txt", "a")
                        f.write(numero)
                        f.close()
                    

                except:
                    None
                        
        break