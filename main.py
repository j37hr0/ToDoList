import sql
from sql import Connection
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog
import sys


dbconn = sql.Connection()
#dbconn.insert_entry("some new entry")
dbconn.update_archive_status(2)
