from Page_Object import YandexDisk
import logging


LOGGER = logging.getLogger(__name__)


def test_copying_files(driver):
    # Authorization
    LOGGER.info('Precondition - authorization')
    yandex_main_page = YandexDisk(driver)

    # Work with Yandex disk
    LOGGER.info('The yandex disk page opens')
    yandex_main_page.go_to_yandex_disk_page()

    # Здесь будет первое действие
