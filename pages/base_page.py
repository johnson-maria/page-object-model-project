class BasePage():
    # добавим конструктор — метод, который вызывается, когда мы создаем объект. Конструктор объявляется ключевым словом __init__
    # browser прилетает из conftest.py, а url из файлов с тестами
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    # метод open. Он должен открывать нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)