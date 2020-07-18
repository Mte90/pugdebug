# -*- coding: utf-8 -*-

"""
    pugdebug - a standalone PHP debugger
    =========================
    copyright: (c) 2015 Robert Basic
    license: GNU GPL v3, see LICENSE for more details
"""

__author__ = "robertbasic"

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem

from pugdebug import settings


class PugdebugBreakpointViewer(QTreeWidget):

    item_double_clicked_signal = pyqtSignal(str, int)

    def __init__(self):
        super(PugdebugBreakpointViewer, self).__init__()

        self.setColumnCount(2)
        self.setHeaderLabels(['File', 'Line', 'Full filename'])

        self.setColumnWidth(0, 350)
        self.header().setStretchLastSection(False)
        self.setColumnHidden(2, True)

        self.setRootIsDecorated(False)

        self.itemDoubleClicked.connect(self.handle_item_double_clicked)

    def set_breakpoints(self, breakpoints):
        self.clear()

        for breakpoint in breakpoints:
            filename = self.__cut_filename(breakpoint['filename'])
            args = [
                filename,
                str(breakpoint['lineno']),
                breakpoint['filename']
            ]

            item = QTreeWidgetItem(args)
            item.setToolTip(0, breakpoint['filename'])

            self.addTopLevelItem(item)

    def handle_item_double_clicked(self, item, column):
        file = item.text(2)
        line = int(item.text(1))

        self.item_double_clicked_signal.emit(file, line)

    def __cut_filename(self, filename):
        path_map = settings.get('path/path_mapping')
        if len(path_map) > 0:
            path_map = path_map.rstrip('/')
            filename = filename[len(path_map):]
        else:
            root = settings.get('path/project_root')
            root = root.rstrip('/')
            filename = filename[len(root):]
        return "~%s" % filename
