def main():
    from PySide6.QtWidgets import QApplication
    from hvppyreading.pdfviewer import PdfViewer

    app = QApplication()
    viewer = PdfViewer()
    viewer.show()
    app.exec()


if __name__ == "__main__":
    main()