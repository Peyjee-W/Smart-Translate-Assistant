from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QGroupBox, QFormLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDesktopWidget
from custom_text_edit import InputTextEdit, OutputTextEdit
from api_utils import translate_text
from file_utils import init_file, append_translation

class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.file_path = init_file()  # 初始化文件路径

    def initUI(self):
        self.setWindowTitle('智能翻译助手')
        self.setWindowIcon(QIcon('Tr.ico'))  # 设置窗口图标
        self.resize(600, 400)  # 设置窗口初始尺寸
        self.center()  # 将窗口置于屏幕中央

        main_layout = QVBoxLayout()
        
        # 翻译设置区域
        settings_group = QGroupBox("翻译设置")
        settings_layout = QFormLayout()

        # 翻译方向选择
        self.direction_combo = QComboBox()
        self.direction_combo.addItem("英译中")
        self.direction_combo.addItem("中译英")
        self.direction_combo.addItem("中译日")
        self.direction_combo.addItem("日译中")
        settings_layout.addRow(QLabel("选择翻译方向:"), self.direction_combo)

        # 翻译风格选择
        self.style_combo = QComboBox()
        self.style_combo.addItem("学术风格")
        self.style_combo.addItem("地道表达")
        self.style_combo.addItem("正式语气")
        self.style_combo.addItem("非正式语气")
        settings_layout.addRow(QLabel("选择翻译风格:"), self.style_combo)

        settings_group.setLayout(settings_layout)
        main_layout.addWidget(settings_group)
        
        # 输入文本框
        self.input_text = InputTextEdit()
        self.input_text.setPlaceholderText("请输入要翻译的内容...")
        main_layout.addWidget(QLabel("输入文本"))
        main_layout.addWidget(self.input_text)
        
        # 翻译按钮
        self.translate_button = QPushButton('翻译')
        self.translate_button.setStyleSheet("padding: 10px; font-size: 16px;")
        self.translate_button.clicked.connect(self.translate_text)
        main_layout.addWidget(self.translate_button)
        
        # 输出文本框
        self.output_text = OutputTextEdit()
        main_layout.addWidget(QLabel("翻译结果"))
        main_layout.addWidget(self.output_text)
        
        self.setLayout(main_layout)
    
    def center(self):
        # 获取屏幕的尺寸
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口的尺寸，包括边框
        size = self.frameGeometry()
        # 计算使窗口居中的位置
        x = (screen.width() - size.width()) // 2
        y = (screen.height() - size.height()) // 2
        # 移动窗口到计算出的居中位置
        self.move(x, y)

    def translate_text(self):
        # 获取翻译方向、翻译风格和输入文本
        direction = self.direction_combo.currentText()
        style = self.style_combo.currentText()
        input_text = self.input_text.toPlainText()
        
        if not input_text.strip():
            self.output_text.setText("请输入要翻译的内容。")
            return

        # 获取翻译结果
        translation = translate_text(direction, style, input_text)
        if translation:
            self.output_text.setText(translation)
            # 保存原文和译文
            append_translation(self.file_path, input_text, translation)
