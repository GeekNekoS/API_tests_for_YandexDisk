import requests
import logging


LOGGER = logging.getLogger(__name__)


def test_creating_a_folder():
    LOGGER.info("Authorization using a token obtained during the operation of the function 'get_token.py'")
    headers = {"Authorization": f"OAuth {'[your token]'}"}  # <== [!]

    params = {"path": "API_test"}

    LOGGER.info("Request to create and name a new folder")
    requests.put("https://cloud-api.yandex.net/v1/disk/resources", headers=headers, params=params)

    response = requests.get("https://cloud-api.yandex.net/v1/disk/resources", headers=headers, params=params)
    assert response.json()['path'] == "disk:/API_test"
    assert response.status_code == 200

    LOGGER.info("Deleting this folder")
    requests.delete("https://cloud-api.yandex.net/v1/disk/resources", headers=headers, params=params)
