from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from ui.components.box import createGroupBox
from ui.components.device_card import DeviceCard
from models.device_info import DeviceInfo, DeviceType

class BootUsbPassthroughGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Configura il layout principale
        layout = QVBoxLayout(self)

        # Aggiungi la prima box
        box1 = createGroupBox("USB devices", [
            DeviceCard(DeviceInfo(DeviceType.USB_STORAGE, devname="UpBloHuVpGQGMF", id_fs_size="32GB", id_vendor="KinkgStone")),
            DeviceCard(DeviceInfo(DeviceType.PHONE, devname="duJgt4o1WrHDs", id_vendor="Honor")),
            DeviceCard(DeviceInfo(DeviceType.PCI, devname="kOcHzlow", id_vendor="Nvidia"))
        ], False)
        layout.addWidget(box1)

        # Aggiungi la seconda box
        box2 = createGroupBox("PCI devices", [QLabel("Contenuto Box 2")], True, "Mostra tutto")
        layout.addWidget(box2)

        # Imposta il layout principale della finestra
        self.setLayout(layout)
    
