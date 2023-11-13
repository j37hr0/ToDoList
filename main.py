import sql
from sql import Connection
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog
import sys
import mainUI


dbconn = sql.Connection()
#dbconn.insert_entry("some newer entry")
dbconn.update_archive_status(2)

def add_button():
    #print(ui.text_to_insert.toPlainText())
    dbconn.insert_entry(ui.text_to_insert.toPlainText())
    ui.text_to_insert.clear()
    paint_lists()
def paint_lists():
    if ui.actionArchived.isChecked():
        items = dbconn.retrieve_all()
        ui.toDoListTable.setRowCount(len(items))
        for row, item in enumerate(items):
            for col, value in enumerate(item):
                ui.toDoListTable.setItem(row, col,  QtWidgets.QTableWidgetItem(str(value)))
    else:
        items = dbconn.retrieve_non_archived()
        ui.toDoListTable.setRowCount(len(items))
        for row, item in enumerate(items):
            for col, value in enumerate(item):
                ui.toDoListTable.setItem(row, col,  QtWidgets.QTableWidgetItem(str(value)))
    ui.toDoListTable.repaint()
    ui.toDoListTable.resizeRowsToContents()
    ui.toDoListTable.resizeColumnToContents(0)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = mainUI.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.setWindowTitle("To Do List App")
MainWindow.show()
paint_lists()
ui.add_btn.clicked.connect(lambda: add_button())
sys.exit(app.exec_())
