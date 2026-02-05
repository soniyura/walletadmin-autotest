import re
from playwright.sync_api import Page, expect

class AssetsSortingMode:
    def __init__(self, page: Page): # создание конструктора класса
        self.page = page # инициализация страницы