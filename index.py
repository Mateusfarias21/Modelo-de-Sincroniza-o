from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

navegador = webdriver.Chrome(executable_path=r"C:\Program Files\Driver\chromedriver_win32\chromedriver.exe")
navegador.get("http://integrasoc.proocupacional.com.br/?CodigoSoc=&CodigoUnidadeSoc=&CodigoFuncionarioSoc=")
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="CodigoSoc"]').send_keys("847895")
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="DataResultadoInicial"]').send_keys("04/12/2021")
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="dataResultadoFinal"]').send_keys("04/12/2021")
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="btnExecutar"]').click()

