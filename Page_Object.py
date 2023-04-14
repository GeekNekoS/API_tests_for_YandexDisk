import time
from Base_Page import BaseClass

import logging


LOGGER = logging.getLogger(__name__)


class Locators:
    pass


class YandexDisk(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.window_handles = None

    pass
