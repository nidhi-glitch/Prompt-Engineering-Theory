import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QSizePolicy, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTextBrowser
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from qtpy.QtCore import QUrl

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.browser = QWebEngineView(self)
        self.view.load(QUrl("https://www.google.com"))
        self.layout.addWidget(self.browser)

        self.address_bar = QLineEdit(self)
        self.layout.addWidget(self.address_bar)

        self.go_button = QPushButton('Go', self)
        self.layout.addWidget(self.go_button)

        self.back_button = QPushButton('Back', self)
        self.layout.addWidget(self.back_button)

        self.forward_button = QPushButton('Forward', self)
        self.layout.addWidget(self.forward_button)

        self.refresh_button = QPushButton('Refresh', self)
        self.layout.addWidget(self.refresh_button)

        self.browser.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.go_button.clicked.connect(self.navigate)
        self.back_button.clicked.connect(self.browser.back)
        self.forward_button.clicked.connect(self.browser.forward)
        self.refresh_button.clicked.connect(self.browser.reload)
        self.address_bar.returnPressed.connect(self.navigate)

        self.browser.page().urlChanged.connect(self.update_address_bar)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Web Browser')

    def navigate(self):
        url = self.address_bar.text()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        self.browser.setUrl(QUrl(url))

    def update_address_bar(self, q):
        self.address_bar.setText(q.toString())
        self.address_bar.setCursorPosition(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view=QWebEngineView()
    view.load(QUrl("https://www.google.com"))
    view.show()
    sys.exit(app.exec_())
