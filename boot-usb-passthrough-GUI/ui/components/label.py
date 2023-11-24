from PyQt5.QtWidgets import QLabel
import consts.app_settings as AppSettings
import ui.utils.style_util as UtilStyle

def label(text, font_size=AppSettings.font_size):
  label = QLabel(text)

  # UtilStyle.setDefaultFontFamily(label)
  if font_size != AppSettings.font_size:
    UtilStyle.setFontSize(label, font_size)

  return label