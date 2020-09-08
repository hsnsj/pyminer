# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from pyminer2.ui.base.widgets.treeviews import PMDatasetsTreeview, PMFilesTreeview
from pyminer2.ui.base.widgets.tablewidget import PMTableWidget
from pyminer2.ui.base.widgets.reportwidget import PMReportWidget
from pyminer2.ui.base.widgets.menu_tool_stat_bars import PMMenuBar, PMToolBarRight, PMToolBarTop
from pyminer2.ui.base.widgets.flowwidget import PMFlowWidget
from pyminer2.ui.base.widgets.controlpanel import PMPage, PMPageData, PMPageModel, PMPagePlot, PMPageStats
from pyminer2.ui.base.widgets.consolewidget import ConsoleWidget
from PyQt5 import QtCore, QtGui, QtWidgets

from .widgets import PMPageExt

from pyminer2.extensions.extensions_manager.manager import extensions_manager


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.widget_left = QtWidgets.QWidget(self.splitter_3)
        self.widget_left.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_left.setObjectName("widget_left")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_left)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(self.widget_left)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.treeWidget_storehouse = PMDatasetsTreeview(self.splitter)
        self.treeWidget_storehouse.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)
        self.treeWidget_storehouse.setObjectName("treeWidget_storehouse")
        self.widget_4 = QtWidgets.QWidget(self.splitter)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.widget_4)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.treeView_files = PMFilesTreeview(self.tab)
        self.treeView_files.setTabKeyNavigation(True)
        self.treeView_files.setDragEnabled(True)
        self.treeView_files.setDragDropOverwriteMode(True)
        self.treeView_files.setAlternatingRowColors(False)
        self.treeView_files.setUniformRowHeights(True)
        self.treeView_files.setSortingEnabled(True)
        self.treeView_files.setAnimated(True)
        self.treeView_files.setAllColumnsShowFocus(False)
        self.treeView_files.setWordWrap(False)
        self.treeView_files.setHeaderHidden(False)
        self.treeView_files.setObjectName("treeView_files")
        self.treeView_files.header().setSortIndicatorShown(True)
        self.verticalLayout_8.addWidget(self.treeView_files)
        self.tabWidget_2.addTab(self.tab, "")
        self.verticalLayout_7.addWidget(self.tabWidget_2)
        self.verticalLayout_3.addWidget(self.splitter)
        self.widget = QtWidgets.QWidget(self.splitter_3)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.widget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter_2)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_data = QtWidgets.QWidget()
        self.tab_data.setObjectName("tab_data")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_data)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget_dataset = PMTableWidget(self.tab_data)
        self.tableWidget_dataset.setStyleSheet("")
        self.tableWidget_dataset.setAlternatingRowColors(False)
        self.tableWidget_dataset.setObjectName("tableWidget_dataset")
        self.tableWidget_dataset.setColumnCount(30)
        self.tableWidget_dataset.setRowCount(30)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(28, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setVerticalHeaderItem(29, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(28, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(29, item)
        self.horizontalLayout_2.addWidget(self.tableWidget_dataset)
        self.tabWidget.addTab(self.tab_data, "")
        self.tab_flow = PMFlowWidget()
        self.tab_flow.setObjectName("tab_flow")
        self.tabWidget.addTab(self.tab_flow, "")
        self.tab_report = PMReportWidget()
        self.tab_report.setObjectName("tab_report")
        self.tabWidget.addTab(self.tab_report, "")
        self.tabWidget_console = QtWidgets.QTabWidget(self.splitter_2)
        self.tabWidget_console.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget_console.setObjectName("tabWidget_console")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textEdit_console = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_console.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit_console.setReadOnly(True)
        self.textEdit_console.setObjectName("textEdit_console")
        self.verticalLayout_4.addWidget(self.textEdit_console)
        self.tabWidget_console.addTab(self.tab_3, "")
        self.console_widget = ConsoleWidget()
        self.console_widget.setObjectName("console_widget")
        self.tabWidget_console.addTab(self.console_widget, "")
        self.verticalLayout.addWidget(self.splitter_2)
        self.horizontalLayout.addWidget(self.splitter_3)
        self.widget_right = QtWidgets.QWidget(self.centralwidget)
        self.widget_right.setMinimumSize(QtCore.QSize(280, 0))
        self.widget_right.setMaximumSize(QtCore.QSize(280, 16777215))
        self.widget_right.setObjectName("widget_right")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_right)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_right)
        self.stackedWidget.setObjectName("stackedWidget")
        # self.page_assess = PMPage(self)
        # self.page_data = PMPageData(self)
        # self.page_stats = PMPageStats(self)
        # self.page_plot = PMPagePlot(self)
        # self.page_model = PMPageModel(self)  # QtWidgets.QWidget()
        # self.page_ext= PMPageExt(self)
        self.page_assess = PMPage()
        self.page_data = PMPageData()
        self.page_stats = PMPageStats()
        self.page_plot = PMPagePlot()
        self.page_model = PMPageModel()  # QtWidgets.QWidget()
        self.page_ext = PMPageExt(self)
        self.stackedWidget.addWidget(self.page_data)
        self.page_stats = PMPageStats()
        self.page_stats.setObjectName("page_stats")
        self.stackedWidget.addWidget(self.page_stats)
        self.page_plot = PMPagePlot()
        self.page_plot.setObjectName("page_plot")
        self.stackedWidget.addWidget(self.page_plot)
        self.page_model = PMPageModel()
        self.page_model.setObjectName("page_model")
        self.stackedWidget.addWidget(self.page_model)
        self.stackedWidget.addWidget(self.page_assess)
        self.stackedWidget.addWidget(self.page_ext)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.widget_right)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar_left = PMToolBarTop(MainWindow)
        self.toolBar_left.setObjectName("toolBar_left")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_left)
        self.toolBar_right = PMToolBarRight(MainWindow)
        self.toolBar_right.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.toolBar_right.setObjectName("toolBar_right")
        MainWindow.addToolBar(QtCore.Qt.RightToolBarArea, self.toolBar_right)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.statusBar.setFont(font)
        self.statusBar.setAutoFillBackground(False)
        self.statusBar.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menubar = PMMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.action_data = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/dbviewtables.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_data.setIcon(icon)
        self.action_data.setObjectName("action_data")
        self.action_stats = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/lc_autosum.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_stats.setIcon(icon1)
        self.action_stats.setObjectName("action_stats")
        self.action_plot = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/lc_drawchart.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_plot.setIcon(icon2)
        self.action_plot.setObjectName("action_plot")
        self.action_model = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/lc_statisticsmenu.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_model.setIcon(icon3)
        self.action_model.setObjectName("action_model")
        self.action_9 = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/New.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_9.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.action_9.setFont(font)
        self.action_9.setObjectName("action_9")
        self.action_menu_open = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/folder.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_menu_open.setIcon(icon5)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.action_menu_open.setFont(font)
        self.action_menu_open.setObjectName("action_menu_open")
        self.action_menu_import_file = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/input.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_menu_import_file.setIcon(icon6)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.action_menu_import_file.setFont(font)
        self.action_menu_import_file.setObjectName("action_menu_import_file")
        self.action_menu_save = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/Save.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_menu_save.setIcon(icon7)
        self.action_menu_save.setObjectName("action_menu_save")
        self.action_menu_save_as = QtWidgets.QAction(MainWindow)
        self.action_menu_save_as.setObjectName("action_menu_save_as")
        self.action_menu_option = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/wb-setting-normal.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_menu_option.setIcon(icon8)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.action_menu_option.setFont(font)
        self.action_menu_option.setObjectName("action_menu_option")
        self.action_quit = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/Delete.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_quit.setIcon(icon9)
        self.action_quit.setObjectName("action_quit")
        self.action_menu_cut = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/Cut.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_menu_cut.setIcon(icon10)
        self.action_menu_cut.setObjectName("action_menu_cut")
        self.action_menu_copy = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/Copy.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_menu_copy.setIcon(icon11)
        self.action_menu_copy.setObjectName("action_menu_copy")
        self.action_menu_paste = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/Paste.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_menu_paste.setIcon(icon12)
        self.action_menu_paste.setObjectName("action_menu_paste")
        self.action_menu_toolbar = QtWidgets.QAction(MainWindow)
        self.action_menu_toolbar.setCheckable(True)
        self.action_menu_toolbar.setChecked(True)
        self.action_menu_toolbar.setObjectName("action_menu_toolbar")
        self.action_menu_statusbar = QtWidgets.QAction(MainWindow)
        self.action_menu_statusbar.setCheckable(True)
        self.action_menu_statusbar.setChecked(True)
        self.action_menu_statusbar.setObjectName("action_menu_statusbar")
        self.action_transposition = QtWidgets.QAction(MainWindow)
        self.action_transposition.setObjectName("action_transposition")
        self.action_menu_data_filter = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/lc_formfilternavigator.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_menu_data_filter.setIcon(icon13)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.action_menu_data_filter.setFont(font)
        self.action_menu_data_filter.setObjectName("action_menu_data_filter")
        self.action_menu_data_merge_v = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/mergedocuments.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_menu_data_merge_v.setIcon(icon14)
        self.action_menu_data_merge_v.setObjectName("action_menu_data_merge_v")
        self.action_menu_data_merge_h = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/lc_mergecells.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_menu_data_merge_h.setIcon(icon15)
        self.action_menu_data_merge_h.setObjectName("action_menu_data_merge_h")
        self.action_menu_stat_describe = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.action_menu_stat_describe.setFont(font)
        self.action_menu_stat_describe.setObjectName(
            "action_menu_stat_describe")
        self.action_distribution = QtWidgets.QAction(MainWindow)
        self.action_distribution.setObjectName("action_distribution")
        self.action_missvalue = QtWidgets.QAction(MainWindow)
        self.action_missvalue.setObjectName("action_missvalue")
        self.action_outlier = QtWidgets.QAction(MainWindow)
        self.action_outlier.setObjectName("action_outlier")
        self.action_corr = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.action_corr.setFont(font)
        self.action_corr.setObjectName("action_corr")
        self.action_regression = QtWidgets.QAction(MainWindow)
        self.action_regression.setObjectName("action_regression")
        self.action_classify = QtWidgets.QAction(MainWindow)
        self.action_classify.setObjectName("action_classify")
        self.action_dimension_reduction = QtWidgets.QAction(MainWindow)
        self.action_dimension_reduction.setObjectName(
            "action_dimension_reduction")
        self.action_non_parametric_test = QtWidgets.QAction(MainWindow)
        self.action_non_parametric_test .setObjectName(
            "action_non_parametric_test ")
        self.action_time_series_prediction = QtWidgets.QAction(MainWindow)
        self.action_time_series_prediction.setObjectName(
            "action_time_series_prediction")
        self.action_survival_analysis = QtWidgets.QAction(MainWindow)
        self.action_survival_analysis.setObjectName("action_survival_analysis")
        self.action_line = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.action_line.setFont(font)
        self.action_line.setObjectName("action_line")
        self.action_histogram = QtWidgets.QAction(MainWindow)
        self.action_histogram.setObjectName("action_histogram")
        self.action_scatter = QtWidgets.QAction(MainWindow)
        self.action_scatter.setObjectName("action_scatter")
        self.action_boxplot = QtWidgets.QAction(MainWindow)
        self.action_boxplot.setObjectName("action_boxplot")
        self.action_bar = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.action_bar.setFont(font)
        self.action_bar.setObjectName("action_bar")
        self.action_menu_tree = QtWidgets.QAction(MainWindow)
        self.action_menu_tree.setObjectName("action_menu_tree")
        self.action_roc = QtWidgets.QAction(MainWindow)
        self.action_roc.setObjectName("action_roc")
        self.action_menu_woe_iv = QtWidgets.QAction(MainWindow)
        self.action_menu_woe_iv.setObjectName("action_menu_woe_iv")
        self.action_scorecard = QtWidgets.QAction(MainWindow)
        self.action_scorecard.setObjectName("action_scorecard")
        self.action_ks = QtWidgets.QAction(MainWindow)
        self.action_ks.setObjectName("action_ks")
        self.action_officesite = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/hlinettp.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_officesite.setIcon(icon16)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.action_officesite.setFont(font)
        self.action_officesite.setObjectName("action_officesite")
        self.action_update = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.action_update.setFont(font)
        self.action_update.setObjectName("action_update")
        self.action_help = QtWidgets.QAction(MainWindow)
        self.action_help.setIcon(icon16)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.action_help.setFont(font)
        self.action_help.setObjectName("action_help")
        self.action_about = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.action_about.setFont(font)
        self.action_about.setObjectName("action_about")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.action_6.setFont(font)
        self.action_6.setObjectName("action_6")
        self.action_menu_database = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/dbqueryedit.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_menu_database.setIcon(icon17)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.action_menu_database.setFont(font)
        self.action_menu_database.setObjectName("action_menu_database")
        self.action_8 = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/infobox.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_8.setIcon(icon18)
        self.action_8.setObjectName("action_8")
        self.action_assess = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/lc_dbreportedit.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_assess.setIcon(icon19)
        self.action_assess.setObjectName("action_assess")
        self.action_menu_dataset = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/lc_dataarearefresh.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_menu_dataset.setIcon(icon20)
        self.action_menu_dataset.setObjectName("action_menu_dataset")
        self.action_dataset_export = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/lc_save.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_dataset_export.setIcon(icon21)
        self.action_dataset_export.setObjectName("action_dataset_export")
        self.action_dataset_rename = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/lc_dbqueryrename.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_dataset_rename.setIcon(icon22)
        self.action_dataset_rename.setObjectName("action_dataset_rename")
        self.action_menu_data_row_filter = QtWidgets.QAction(MainWindow)
        self.action_menu_data_row_filter.setObjectName(
            "action_menu_data_row_filter")
        self.action_menu_result = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/lc_dia.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_menu_result.setIcon(icon23)
        self.action_menu_result.setObjectName("action_menu_result")
        self.action_menu_sort = QtWidgets.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/lc_dbsortingandgrouping.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_menu_sort.setIcon(icon24)
        self.action_menu_sort.setObjectName("action_menu_sort")
        self.action_package_manager = QtWidgets.QAction(MainWindow)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/lc_insertplugin.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_package_manager.setIcon(icon25)
        self.action_package_manager.setObjectName("action_package_manager")
        self.action_jupyter_notebook = QtWidgets.QAction(MainWindow)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/jupyter.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_jupyter_notebook.setIcon(icon26)
        self.action_jupyter_notebook.setObjectName("action_jupyter_notebook")
        self.actionWindows = QtWidgets.QAction(MainWindow)
        self.actionWindows.setObjectName("actionWindows")
        self.actionFusion = QtWidgets.QAction(MainWindow)
        self.actionFusion.setObjectName("actionFusion")
        self.actionQdarkstyle = QtWidgets.QAction(MainWindow)
        self.actionQdarkstyle.setObjectName("actionQdarkstyle")
        self.action_ipython = QtWidgets.QAction(MainWindow)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(
            QtGui.QPixmap(":/pyqt/source/images/python.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_ipython.setIcon(icon27)
        self.action_ipython.setObjectName("action_ipython")
        self.action_7 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.action_7.setFont(font)
        self.action_7.setObjectName("action_7")
        self.actionWindowsVista = QtWidgets.QAction(MainWindow)
        self.actionWindowsVista.setObjectName("actionWindowsVista")
        self.action_hide_right = QtWidgets.QAction(MainWindow)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(
            QtGui.QPixmap(
                ":/pyqt/source/images/lc_arrowshapes.right-arrow-callout.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.action_hide_right.setIcon(icon28)
        self.action_hide_right.setObjectName("action_hide_right")
        self.action_menu_workdir = QtWidgets.QAction(MainWindow)
        self.action_menu_workdir.setCheckable(True)
        self.action_menu_workdir.setChecked(True)
        self.action_menu_workdir.setObjectName("action_menu_workdir")
        self.action_menu_todolist = QtWidgets.QAction(MainWindow)
        self.action_menu_todolist.setCheckable(True)
        self.action_menu_todolist.setChecked(True)
        self.action_menu_todolist.setObjectName("action_menu_todolist")
        self.action_menu_toolbox = QtWidgets.QAction(MainWindow)
        self.action_menu_toolbox.setCheckable(True)
        self.action_menu_toolbox.setChecked(True)
        self.action_menu_toolbox.setObjectName("action_menu_toolbox")
        self.action_minitray = QtWidgets.QAction(MainWindow)
        self.action_minitray.setObjectName("action_minitray")
        self.action_info = QtWidgets.QAction(MainWindow)
        self.action_info.setObjectName("action_info")
        self.action_success = QtWidgets.QAction(MainWindow)
        self.action_success.setObjectName("action_success")
        self.action_warning = QtWidgets.QAction(MainWindow)
        self.action_warning.setObjectName("action_warning")
        self.action_error = QtWidgets.QAction(MainWindow)
        self.action_error.setObjectName("action_error")
        self.toolBar_left.addSeparator()

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_console.setCurrentIndex(0)
        self.action_quit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyMiner"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.bind_events()

    def bind_events(self):
        self.action_quit.triggered.connect(self.close)
        self.action_install_ext.triggered.connect(extensions_manager.install)