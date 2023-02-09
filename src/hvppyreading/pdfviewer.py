import os
from typing import Optional

from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtWidgets import QMainWindow, QWidget, QFileDialog
from PySide6.QtGui import QAction


class PdfViewer(QMainWindow):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.pdfview: QPdfView = QPdfView(self)
        self.pdfdoc: QPdfDocument = QPdfDocument(self)
        self.pdfview.setDocument(self.pdfdoc)
        self.setCentralWidget(self.pdfview)

        self.open_action = QAction("Open", self)
        self.open_action.triggered.connect(self.open_file)
        self.menuBar().addAction(self.open_action)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open", filter="PDF files(*.pdf)"
        )
        if not file_path:
            return

        if not os.path.exists(file_path):
            print(f"The file '{file_path}' not exists.")
            return
        self.pdfdoc.load(file_path)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    
    app = QApplication()
    viewer = PdfViewer()
    viewer.show()
    app.exec()
