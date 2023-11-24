from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QLabel,
    QComboBox, QPushButton, QGraphicsDropShadowEffect
)
from PyQt5.QtGui import QPixmap, QPainter, QColor, QPalette
from PyQt5.QtCore import Qt, QSize
from models.device_info import DeviceInfo, DeviceType
import consts.app_settings as AppSettings
import consts.style as Style
from ui.utils.icon_util import get_image_from_url
import ui.utils.style_util as StyleUtil

class DeviceCard(QWidget):
    def __init__(self, device_info):
        super().__init__()

        self._device_info = device_info
        self._icon_column_layout = None
        self._icon_label = None

        # Impostazioni generali della card
        self.setObjectName("deviceCard")
        self.setStyleSheet(f"""
            #deviceCard {{
                background-color: {Style.dark_background};
                border-radius: {AppSettings.border_radius};
                border: 1px solid {Style.border_light};
            }}
        """)
        self.setMinimumWidth(300)

        # Applica un'ombreggiatura alla card
        self.apply_shadow()
        
        # Layout principale
        self.create_main_layout()

    def apply_shadow(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(10)
        shadow.setColor(QColor(0, 0, 0, 150))
        shadow.setOffset(5, 5)
        self.setGraphicsEffect(shadow)

    def create_details_label(self):
        details_label_values = filter(None, [self._device_info.devname, self._device_info.id_fs_size, self._device_info.id_vendor])
        details_label = QLabel(f"<b>{' | '.join(details_label_values)}</b>")

        # Set the attribute for a translucent background
        details_label.setAttribute(Qt.WA_TranslucentBackground)

        # Set the background color with an alpha value for transparency
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255, 100))  # Adjust the alpha value (100) for transparency
        details_label.setPalette(palette)
        return details_label

    def create_passthrough_layout(self):
        passthrough_layout = QHBoxLayout()

        passthrough_combobox = QComboBox()
        passthrough_combobox.addItems([device_type.name for device_type in DeviceType])
        passthrough_combobox.setCurrentText(self._device_info.device_type.name)
        passthrough_combobox.currentIndexChanged.connect(lambda index: self.update_device_type(index + 1))
        passthrough_combobox.currentIndexChanged.connect(self.update_icon)  # Connessione per l'aggiornamento dell'icona
        StyleUtil.setFontSize(passthrough_combobox, AppSettings.font_size_small)

        connect_button = QPushButton("Collega")
        StyleUtil.setFontSize(connect_button, AppSettings.font_size_small)
        connect_button.clicked.connect(self.connect_button_clicked)

        passthrough_layout.addWidget(passthrough_combobox)
        passthrough_layout.addStretch(1)
        passthrough_layout.addWidget(connect_button)

        return passthrough_layout

    def update_device_type(self, index):
        self._device_info._device_type = DeviceType(index)

    def create_main_layout(self):
        main_layout = QHBoxLayout(self)

        # Prima colonna con l'icona
        icon_column_layout = QVBoxLayout()
        self._icon_column_layout = icon_column_layout
        icon_label = self.create_icon_label()
        icon_column_layout.addWidget(icon_label, alignment=Qt.AlignCenter)
        main_layout.addLayout(icon_column_layout)
        main_layout.addSpacing(AppSettings.margin_value)

        # Seconda colonna con il resto degli elementi
        details_passthrough_layout = QVBoxLayout()

        details_label = self.create_details_label()
        details_passthrough_layout.addWidget(details_label)

        passthrough_layout = self.create_passthrough_layout()
        details_passthrough_layout.addLayout(passthrough_layout)

        main_layout.addLayout(details_passthrough_layout)

        main_layout.setContentsMargins(
            AppSettings.padding_value,
            AppSettings.padding_value,
            AppSettings.padding_value,
            AppSettings.padding_value
        )

        return main_layout
    
    def update_icon(self):
        icon_label = self.create_icon_label()
        icon_column_layout = self.layout().itemAt(0)
        icon_column_layout.replaceWidget(icon_column_layout.itemAt(0).widget(), icon_label)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(0, 0, 0, 50))
        painter.drawRoundedRect(self.rect(), 10, 10)

    def create_icon_label(self):
        scale = 10
        size = AppSettings.font_size * scale

        icon_label = QLabel()
        self._icon_label = icon_label
        pixmap = get_image_from_url(self.get_icon_url())  # Sostituisci con l'URL effettivo
        if pixmap:
            # Calculate the scaled size while maintaining the aspect ratio
            scaled_pixmap = pixmap.scaledToWidth(int(size * 0.8))

            # Set the scaled pixmap to the QLabel
            icon_label.setPixmap(scaled_pixmap)
            icon_label.setWordWrap(True)
            icon_label.setFixedSize(QSize(size, size))
            icon_label.setAlignment(Qt.AlignCenter)
        else:
            icon_label.setText("Errore nel caricamento dell'immagine")

        icon_label.setWordWrap(True)
        return icon_label

    def get_icon_url(self):
        # Aggiungi logicamente qui le classi delle icone di Material Design in base al tipo di dispositivo
        if self._device_info.device_type == DeviceType.USB_STORAGE:
            return "https://camo.githubusercontent.com/06ebe89da5111cd155a8efb2db7a581e56bf45a5fb635d528ea3fe7d5276c100/68747470733a2f2f662e636c6f75642e6769746875622e636f6d2f6173736574732f313036373930372f313335313631392f64333235373434382d333732392d313165332d393566382d6234343538363238323534382e706e67"  # Sostituisci con la classe effettiva
        elif self._device_info.device_type == DeviceType.PHONE:
            return "https://cdn-icons-png.flaticon.com/512/0/191.png"  # Sostituisci con la classe effettiva
        elif self._device_info.device_type == DeviceType.PCI:
            return "https://static.thenounproject.com/png/780203-200.png"  # Sostituisci con la classe effettiva

    def connect_button_clicked(self):
        # Aggiungi qui la logica per il passthrough quando il pulsante "Collega" viene premuto
        pass
