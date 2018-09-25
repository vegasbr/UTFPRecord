# -*- coding: utf-8 -*-

from selenium import webdriver

'''Antes de tudo, deve-se ter o chrome webdriver baixado e especificado nas
variaveis de ambiente

tutorial:
import UploadRecord as up
up.GetRec('SEU_RA','SUA_SENHA')
Acontece a magica !
'''

options = webdriver.ChromeOptions()
options.add_argument('--headless') # Desabilitando a tab do chrome
options.add_argument('--disable-gpu') # Desablitando o GPU para renderizar o Chrome


def GetRec(ra, password):
    driver = webdriver.Chrome(options=options)
    url = 'https://' + ra + ':' + password + '@utfws.utfpr.edu.br/aluno02/sistema/mpmenu.inicio'
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="div_CarregaAjaxMenu"]/center/table/tbody/tr/td[10]').click()
    frame = driver.find_element_by_tag_name('iframe')
    driver.switch_to.frame(frame)

    subj_sem = []
    cod = []
    subj = []
    cred = []
    med = []
    freq = []
    per = []

    # Abaixo estou especificando a tabela do historico curricular e salvando nas listas os parametros

    hist = driver.find_element_by_xpath('//*[@id="tbl_hist"]/tbody/tr/td/div/center[1]/table/tbody/tr/td/table[1]/tbody')
    for row in hist.find_elements_by_xpath(".//tr"):
        table = [td.text for td in row.find_elements_by_tag_name('td')]
        subj_sem.append(table[0])
        cod.append(table[1])
        subj.append(table[2])
        cred.append(table[7])
        med.append(table[8])
        freq.append(table[9])
        per.append(table[10])

    driver.switch_to_default_content() # saindo do frame
    driver.find_element_by_xpath('//*[@id="div_fsInterno"]/table/tbody/tr[1]/td[3]').click() # disconectando do portal
    driver.close() # encerrando o drive

    return subj_sem, subj, cod, cred, med, freq, per
