class BasePage():
    def __init__(self, browser, url):
        #инициализация объекта с параметрами self.browser и self.url
        self.browser = browser
        self.url = url
        
    def open(self):
        #открываем нужную страницу в браузере
        self.browser.get(self.url)