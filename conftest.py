from selenium import webdriver
from Page_Object import YandexDisk
from settings import *
import logging
import pytest
import time


LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()

    # Предусловие

    LOGGER.info('Running autotests')
    yield driver

    # Постусловие
