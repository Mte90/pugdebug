# -*- coding: utf-8 -*-

"""
    pugdebug - a standalone PHP debugger
    =========================
    copyright: (c) 2015 Robert Basic
    license: GNU GPL v3, see LICENSE for more details
"""

__author__ = "robertbasic"

from PyQt5.QtWidgets import (QLineEdit, QFormLayout, QSpinBox, QCheckBox,
                             QGroupBox)


class PugdebugSettingsForm():

    def __init__(self):
        # Construct the widgets
        self.widgets = {
            'path/project_root': QLineEdit(),
            'path/path_mapping': QLineEdit(),
            'debugger/host': QLineEdit(),
            'debugger/port_number': QSpinBox(),
            'debugger/idekey': QLineEdit(),
            'debugger/break_at_first_line': QCheckBox("Break at first line"),
            'debugger/max_depth': QLineEdit(),
            'debugger/max_children': QLineEdit(),
            'debugger/max_data': QLineEdit(),
            'editor/tab_size': QSpinBox(),
            'editor/font_size': QSpinBox(),
            'editor/enable_text_wrapping': QCheckBox("Enable text wrapping"),
        }

        # Widget settings
        self.widgets['debugger/port_number'].setRange(1, 65535)

        self.widgets['editor/tab_size'].setRange(1, 16)
        self.widgets['editor/tab_size'].setSuffix(' spaces')

        self.widgets['editor/font_size'].setRange(8, 24)
        self.widgets['editor/font_size'].setSuffix(' pt')

        self.setup_path_widgets()
        self.setup_debugger_widgets()
        self.setup_editor_widgets()

    def setup_path_widgets(self):
        path_layout = QFormLayout()
        path_layout.addRow("Root:", self.widgets['path/project_root'])
        path_layout.addRow("Maps from:", self.widgets['path/path_mapping'])

        self.path_group = QGroupBox("Path")
        self.path_group.setLayout(path_layout)

    def setup_debugger_widgets(self):
        debugger_layout = QFormLayout()
        debugger_layout.addRow("Host", self.widgets['debugger/host'])
        debugger_layout.addRow("Port", self.widgets['debugger/port_number'])
        debugger_layout.addRow("IDE Key", self.widgets['debugger/idekey'])
        debugger_layout.addRow(
            "",
            self.widgets['debugger/break_at_first_line']
        )
        debugger_layout.addRow("Max depth", self.widgets['debugger/max_depth'])
        debugger_layout.addRow(
            "Max children",
            self.widgets['debugger/max_children']
        )
        debugger_layout.addRow("Max data", self.widgets['debugger/max_data'])

        self.debugger_group = QGroupBox("Debugger")
        self.debugger_group.setLayout(debugger_layout)

    def setup_editor_widgets(self):
        editor_layout = QFormLayout()
        editor_layout.addRow("Tab size", self.widgets['editor/tab_size'])
        editor_layout.addRow("Font size", self.widgets['editor/font_size'])
        editor_layout.addRow("", self.widgets['editor/enable_text_wrapping'])

        self.editor_group = QGroupBox("Editor")
        self.editor_group.setLayout(editor_layout)

    def set_widget_value(self, widget, value):
        """A generic method which can set the value of any of the used widgets.
        """
        if isinstance(widget, QLineEdit):
            widget.setText(str(value))
        elif isinstance(widget, QSpinBox):
            widget.setValue(int(value))
        elif isinstance(widget, QCheckBox):
            if widget.isTristate():
                widget.setCheckState(int(value))
            else:
                widget.setChecked(bool(value))
        else:
            name = type(widget).__name__
            raise Exception("Don't know how to set a value for %s" % name)

    def get_widget_value(self, widget):
        """A generic method which can set the value of any of the used widgets.
        """
        if isinstance(widget, QLineEdit):
            return widget.text()
        elif isinstance(widget, QSpinBox):
            return widget.value()
        elif isinstance(widget, QCheckBox):
            return (widget.checkState() if widget.isTristate()
                    else widget.isChecked())
        else:
            name = type(widget).__name__
            raise Exception("Don't know how to get a value for %s" % name)
