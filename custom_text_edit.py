from PyQt5.QtWidgets import QTextEdit, QMenu, QAction

class InputTextEdit(QTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        # 自定义右键菜单项，包含快捷键提示
        cut_action = QAction("剪切", self)
        cut_action.setShortcut("Ctrl+X")
        cut_action.triggered.connect(self.cut)

        copy_action = QAction("复制", self)
        copy_action.setShortcut("Ctrl+C")
        copy_action.triggered.connect(self.copy)

        paste_action = QAction("粘贴", self)
        paste_action.setShortcut("Ctrl+V")
        paste_action.triggered.connect(self.paste)

        select_all_action = QAction("全选", self)
        select_all_action.setShortcut("Ctrl+A")
        select_all_action.triggered.connect(self.selectAll)

        menu.addAction(cut_action)
        menu.addAction(copy_action)
        menu.addAction(paste_action)
        menu.addAction(select_all_action)
        menu.exec_(event.globalPos())

class OutputTextEdit(QTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setReadOnly(True)

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        # 自定义右键菜单项，只包含复制和全选，包含快捷键提示
        copy_action = QAction("复制", self)
        copy_action.setShortcut("Ctrl+C")
        copy_action.triggered.connect(self.copy)

        select_all_action = QAction("全选", self)
        select_all_action.setShortcut("Ctrl+A")
        select_all_action.triggered.connect(self.selectAll)

        menu.addAction(copy_action)
        menu.addAction(select_all_action)
        menu.exec_(event.globalPos())
