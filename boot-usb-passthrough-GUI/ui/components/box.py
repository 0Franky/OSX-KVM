from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QCheckBox, QLabel, QHBoxLayout, QScrollArea, QWidget
import consts.app_settings as AppSettings
from ui.components.flow_layout import FlowLayout

def createGroupBox(title, content=[], show_switch=False, switch_title=""):
    # Crea una box con titolo e contenuto
    group_box = QGroupBox(title)

    # Configura stile per spostare il titolo sopra il bordo
    style_sheet = f"QGroupBox {{ border: 2px solid gray; border-radius: {AppSettings.border_radius}; margin-top: 0.5em; }} "
    style_sheet += f"QGroupBox:title {{ subcontrol-origin: margin; subcontrol-position: top center; padding: 0 0.5em; }}"
    group_box.setStyleSheet(style_sheet)

    # Crea un layout principale per la group_box
    main_layout = QVBoxLayout(group_box)

    # Aggiungi uno switch opzionale
    if show_switch:
        switch_layout = QHBoxLayout()
        switch_layout.addStretch()

        switch = QCheckBox(switch_title)
        switch_layout.addWidget(switch)

        main_layout.addLayout(switch_layout)

    # Aggiungi il contenuto alla box
    flow_layout = FlowLayout(hSpacing=AppSettings.margin_value, vSpacing=AppSettings.margin_value)

    for item in content:
        flow_layout.addWidget(item)

    # Wrappa la box_layout in un widget scorrevole
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)

    # Imposta uno stile senza bordo al QScrollArea
    scroll_area.setStyleSheet("QScrollArea { border: none; padding: 0.5em; }")

    scroll_content = QWidget()
    scroll_content.setLayout(flow_layout)
    scroll_area.setWidget(scroll_content)

    # Aggiungi il QScrollArea al layout principale
    main_layout.addWidget(scroll_area)

    return group_box
