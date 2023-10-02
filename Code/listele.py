from selenium import webdriver
from selenium.webdriver.common.by import By
from username import ad,sifre
from time import sleep

login = webdriver.Chrome()
link = "https://www.instagram.com"
login.get(link)


login.maximize_window()
sleep(3)

def _init_(self,ad,sifre):
    self.login = webdriver.Chrome()
    self.username = ad
    self.userpassword = sifre

adet =1

def log(ad,sifre):
    usernameInput = login.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input").send_keys(ad)
    usernameInput2 = login.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input").send_keys(sifre)
    sleep(2)
    login.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]").click()
    sleep(3)
    login.get(link + "/"+ ad)
    sleep(3)
    login.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a").click()
    sleep(4)


#Bulduğumuz takipleri ekrana yazdırmak için fonksiyon oluşturduk.
def yazdir():

    takipler = login.find_elements(By.CSS_SELECTOR, "._aacl._aaco._aacw._aacx._aad7._aade")
    sayac = 1
    for takip in takipler:
        sayac +=1
        print(str(sayac) +" --> "+ takip.text)  


#Bütün kişileri alabilmek için bir fonksiyon ile scroll bar inşaa ettik.
def scroll():

    #js kodu ekledik.

    """
    sayfa = document.querySelecter("._aano"); --> İle Takiplerin olduğu bölümü gösterdik.
    sayfa.scrollto(0,sayfa.scrollHeight); --> İle scroll bar2 in kendi uzunlluğu kadar aşaği inmesini sağladik.
    var syfsonu = sayfa.scrollHeight; --> ile sayfasonu uzunluğunu atadik.
    return syfsonu; --> İle syfsonu 'nu döndürdük.
    
    """

    jskod = """

    sayfa = document.querySelector("._aano");      
    sayfa.scrollTo(0,sayfa.scrollHeight);
    var syfsonu = sayfa.scrollHeight;
    return syfsonu;
    
    """
    syfsonu = login.execute_script(jskod)

    while True:
        son =syfsonu
        sleep(2)
        syfsonu = login.execute_script(jskod)
        if son == syfsonu:
            break

log(ad,sifre)
scroll()
yazdir()

sleep(4)
login.close
