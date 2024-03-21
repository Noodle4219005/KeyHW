from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import Transcribe
import os

account = 'MY'
password = 'PASSWORD'
#file = 'test'

print('working')
Transcribe.main()
print('Transcribe complete')
driver = webdriver.Chrome()
driver.get('http://school1.nssh.ntpc.edu.tw/modules/tad_web/aboutus.php?WebID=150')
time.sleep(.1)
driver.find_element_by_id('c-button--slide-right').click()
select = Select(driver.find_element_by_id('login_method'))
time.sleep(.1)
select.select_by_value("student_login")
element = driver.find_element_by_name('MemUname')
element.send_keys(account)
element = driver.find_element_by_name('MemPasswd')
element.send_keys(password)
driver.find_element_by_class_name('btn.btn-success.btn-block').click()
driver.get('http://school1.nssh.ntpc.edu.tw/modules/tad_web/homework.php?WebID=150&op=edit_form')

with open('output.txt','r', encoding='utf-8') as file:
    Keyin = ''
    for line in file.readlines():
        Keyin = Keyin + line
    print(Keyin)

#driver.find_element_by_id('cke_32').click()
driver.switch_to.default_content()
driver.switch_to.frame(0) 
#driver.find_element_by_tag_name("body").send_keys(file)
script = '''function getElementByXpath(path){
  return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}
getElementByXpath("/html/body").innerHTML = ''' + "'{}';".format(Keyin)
driver.execute_script(script)
driver.switch_to.default_content()
#time.sleep(10)
driver.find_element_by_class_name('btn.btn-primary').click()
driver.quit
os.system("exit")