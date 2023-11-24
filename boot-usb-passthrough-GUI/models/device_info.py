from enum import Enum

class DeviceType(Enum):
    USB_STORAGE = 1
    PHONE = 2
    PCI = 3


class DeviceInfo:
    def __init__(self, device_type, devname="", hostbus="", hostaddr="", id_model="", id_vendor="", id_vendor_id="", id_fs_size="", id_path=""):
        self._device_type = device_type
        self._devname = devname
        self._hostbus = hostbus
        self._hostaddr = hostaddr
        self._id_model = id_model
        self._id_vendor = id_vendor
        self._id_vendor_id = id_vendor_id
        self._id_fs_size = id_fs_size
        self._id_path = id_path

    @property
    def device_type(self):
        return self._device_type

    @property
    def devname(self):
        return self._devname

    @property
    def hostbus(self):
        return self._hostbus

    @property
    def hostaddr(self):
        return self._hostaddr

    @property
    def id_model(self):
        return self._id_model

    @property
    def id_vendor(self):
        return self._id_vendor

    @property
    def id_vendor_id(self):
        return self._id_vendor_id

    @property
    def id_fs_size(self):
        return self._id_fs_size

    @property
    def id_path(self):
        return self._id_path
