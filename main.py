from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/FirmwareIngelean115/ota_esp32/"
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "hilo_principal.py")
ota_updater.download_and_install_update_if_available()
from hilo_principal import hilo_principal
hilo_principal()