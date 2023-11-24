from PyQt5.QtGui import QFont
import consts.app_settings as AppSettings
import consts.style as Style

# def setDefaultStyle(component):
#   setDefaultFontFamily(component)
#   setDefaultFontSize(component)

# def setDefaultFontFamily(component):
#   component.setFont(QFont(family=AppSettings.font_name))

# def setDefaultFontSize(component):
#   setFontSize(component, AppSettings.font_size)

def setFontSize(component, font_size):
  font = QFont()
  font.setPointSize(font_size)
  component.setFont(font)

def setDarkTheme(app):
  dark_stylesheet = f"""
    QWidget {{
        background-color: {Style.background};
        color: {Style.foreground};
    }}

    QGroupBox {{
        border: 2px solid {Style.foreground};
        border-radius: {AppSettings.border_radius};
        margin-top: 0.5em;
    }}

    QGroupBox:title {{
        subcontrol-origin: margin;
        subcontrol-position: top center;
        padding: 0 0.5em;
    }}

    QCheckBox {{
        color: {Style.foreground};
    }}

    QCheckBox::indicator {{
        border: 2px solid {Style.border_light};
        width: 15px;
        height: 15px;
        border-radius: {AppSettings.border_radius_cb};
    }}

    QCheckBox::indicator:checked {{
        background-color: {Style.border_dark};
    }}
  """

  app.setStyleSheet(dark_stylesheet)
