from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options

def main():
    options = Options()
    options.add_experimental_option("detach", True)# добавлено чтобы не закрывать браузер

    driver = webdriver.Chrome(executable_path="C://Users/sib-coder/PycharmProjects/pythonProject2/chromedriver.exe", options=options)

    driver.get("https://www.google.com/")
    #делаем ввод с клавиатуры
    input_google = driver.find_element("xpath",'//textarea[@name="q"]') #поиск поля для ввода
    #ввод информации
    input_google.send_keys("CTF")
    input_google.send_keys(Keys.RETURN)
    #проверка заголовка
    assert "CTF - Поиск в Google" in driver.title

if __name__ == "__main__":
	main()