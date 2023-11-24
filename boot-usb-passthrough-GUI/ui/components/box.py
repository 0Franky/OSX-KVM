from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QCheckBox, QLabel, QHBoxLayout
import consts.app_settings as AppSettings
from ui.components.flow_layout import FlowLayout

def createGroupBox(title, content = [], show_switch=False, switch_title=""):
  # Crea una box con titolo e contenuto
  group_box = QGroupBox(title)

  # Configura stile per spostare il titolo sopra il bordo
  style_sheet = f"QGroupBox {{ border: 2px solid gray; border-radius: {AppSettings.border_radius}; margin-top: 0.5em; padding: 0.5em; }} "
  style_sheet += f"QGroupBox:title {{ subcontrol-origin: margin; subcontrol-position: top center; padding: 0 0.5em; }}"
  group_box.setStyleSheet(style_sheet)

  # Imposta il layout della box
  box_layout = QVBoxLayout(group_box)

  # Aggiungi uno switch opzionale
  if show_switch:
    switch_layout = QHBoxLayout()
    switch_layout.addStretch()

    switch = QCheckBox(switch_title)
    switch_layout.addWidget(switch)

    box_layout.addLayout(switch_layout)

  # Aggiungi il contenuto alla box
  flow_layout = FlowLayout(hSpacing=AppSettings.margin_value, vSpacing=AppSettings.margin_value)
  box_layout.addLayout(flow_layout)

  for item in content:
    flow_layout.addWidget(item)

  return group_box
