from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGroupBox, QTextEdit
from PyQt5.QtCore import Qt
from ui.components.box import createFlexGroupBox, createGroupBoxSingleChild
from ui.components.device_card import DeviceCard
from models.device_info import DeviceInfo, DeviceType
import consts.app_settings as AppSettings

class BootUsbPassthroughGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Configura il layout principale
        layout = QVBoxLayout(self)

        # Aggiungi la prima box
        box1 = createFlexGroupBox("USB devices", [
            DeviceCard(DeviceInfo(DeviceType.USB_STORAGE, devname="UpBloHuVpGQGMF", id_fs_size="32GB", id_vendor="KinkgStone")),
            DeviceCard(DeviceInfo(DeviceType.PHONE, devname="duJgt4o1WrHDs", id_vendor="Honor")),
            DeviceCard(DeviceInfo(DeviceType.PCI, devname="kOcHzlow", id_vendor="Nvidia"))
        ], False)
        layout.addWidget(box1)

        # Aggiungi la seconda box
        box2 = createFlexGroupBox("PCI devices", [QLabel("Contenuto Box 2")], True, "Mostra tutto")
        layout.addWidget(box2)

        # Aggiungi il bottone per avviare macOS
        start_macos_button = QPushButton("Avvia macOS")
        start_macos_button.setStyleSheet(f"margin: {AppSettings.margin}; padding: {AppSettings.padding_value * 0.7}{AppSettings.metrix} {AppSettings.padding_value * 3}{AppSettings.metrix};")
        start_macos_button.clicked.connect(self.start_macos)
        layout.addWidget(start_macos_button, alignment=Qt.AlignCenter)

        logTextBox = QTextEdit()
        logTextBox.setReadOnly(True)
        logTexBoxstyle_sheet = f"QTextEdit {{ border: none; margin-top: 0.5em; }} "
        logTextBox.setStyleSheet(logTexBoxstyle_sheet)

        # Aggiungi la terza box con la textbox per i log
        log_box = createGroupBoxSingleChild("QEMU Log", logTextBox)
        layout.addWidget(log_box)

        # Imposta il layout principale della finestra
        self.setLayout(layout)

    def start_macos(self):
        # Aggiungi qui la logica per avviare macOS e aggiornare i log nella textbox
        pass
