from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont
from ui.screens.home import BootUsbPassthroughGUI
import consts.app_settings as AppSettings
import ui.utils.style_util as UtilStyle

def start_gui():
    app = QApplication([])

    UtilStyle.setDarkTheme(app)

    # Imposta il font predefinito per l'intera applicazione
    default_font = QFont(AppSettings.font_name, AppSettings.font_size)
    app.setFont(default_font)

    # Crea e mostra l'applicazione
    window = BootUsbPassthroughGUI()
    window.show()

    # Imposta le dimensioni iniziali della finestra (larghezza x altezza)
    window.resize(900, 500)

    app.exec_()