import os
import sys
from util import Cfg
from core.parse_data import  cnki_refworks

from PySide6.QtCore import QSize, QStringListModel
from PySide6.QtGui import Qt, QAction, QIcon, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QMainWindow, QApplication, QAbstractItemView, QInputDialog, QFileDialog, \
    QLineEdit, QHeaderView

from ui_main import Ui_MainWindow


class TableModel(QStandardItemModel):
    def __init__(self, parent=None):
        super(TableModel, self).__init__(parent)


class MasterWindows(QMainWindow, Ui_MainWindow):
    def __init__(self): # 构造方法
        super(MasterWindows, self).__init__()  # 运行父类的构造方法
        self.setupUi(self)  # 传递自己
        # 工作空间——设置
        self.action_workspace_set.triggered.connect(self.actionWorkspaceSet)

        # 数据文件——数据目录
        self.btn_datafiles_dir.clicked.connect(self.actionDatafilesDir)
        # 数据文件——加载
        self.btn_datafiles_load.clicked.connect(self.actionDatafilesLoad)
        # 数据文件——合并
        self.btn_datafiles_combine.clicked.connect(self.actionDatafilesCombine)
        # 数据文件——解析cnki
        self.btn_datafiles_parse_cnki.clicked.connect(self.actionDatafilesParseCNKI)

        # 数据模型——显示

        self.setToolBars()

        self.showDatafiles()


    def setToolBars(self):
        """
        工具栏
        """
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolBar.setIconSize(QSize(16, 16))

        add_action = QAction(QIcon(r'icons\tianjia.png'), '添加', self)
        add_action.setStatusTip('添加')
        add_action.triggered.connect(app.quit)

        download_action = QAction(QIcon(r'icons\xiazai.png'), '下载', self)
        download_action.setStatusTip('下载')
        download_action.triggered.connect(app.quit)

        self.toolBar.addActions([add_action, download_action])



    def actionWorkspaceSet(self):
        """
        设置工作空间
        """
        fileName = QFileDialog.getExistingDirectory(self, "选择工作空间", "")  # 选择目录，返回选中的路径

    def actionDatafilesDir(self):
        """
        设置数据目录
        """
        dirName = QFileDialog.getExistingDirectory(self, "选择数据目录", "")  # 选择目录，返回选中的路径

        if len(dirName.strip()):
            Cfg.set('datafiles_dir', dirName)
            self.statusBar().showMessage('设置数据目录 '+dirName, 5000)

        self.actionDatafilesLoad()

    def actionDatafilesLoad(self):
        """
        加载数据文件
        """
        dir = Cfg.get('datafiles_dir')
        names = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
        self.showDatafiles(names)

    def actionDatafilesCombine(self):
        """
        合并数据文件
        """
        dir = Cfg.get('datafiles_dir')
        text, ok = QInputDialog.getText(self, '输入','新的文件名', QLineEdit.Normal, "")
        if ok and text!='':
            with open(os.path.join(dir, text), 'w', encoding='utf-8') as writer:
                rows = [mi for mi in self.listView_datafiles.selectedIndexes()]
                fnames = [self.listView_datafiles.model().data(row) for row in rows]
                for fname in fnames:
                    with open(os.path.join(dir, fname), encoding='utf-8') as reader:
                        writer.writelines(reader.readlines())
                        writer.write('\r\n')


    def actionDatafilesParseCNKI(self):
        """
        解析数据文件cnki
        """
        dir = Cfg.get('datafiles_dir')
        rows = [mi for mi in self.listView_datafiles.selectedIndexes()]
        fnames = [self.listView_datafiles.model().data(row) for row in rows]
        fnames = [os.path.join(dir, fname) for fname in fnames]

        ds = cnki_refworks.parse_file(fnames)
        columns = ['doctype', 'authors', 'orgs', 'title', 'source', 'pubyear', 'kws', 'abs']
        self.showDataTableView(ds, columns)
        print(ds[0])

    def showDatafiles(self, names=[]):
        """
        显示数据文件列表
        """
        self.listView_datafiles.setSelectionMode(QAbstractItemView.ExtendedSelection)
        slm = QStringListModel()
        slm.setStringList(names)
        self.listView_datafiles.setModel(slm)

    def showDataTableView(self, ds=[], columns=[]):
        """
        显示数据
        """
        self.tableView_data.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 设置模型
        model = QStandardItemModel(len(ds), len(columns))
        model.setHorizontalHeaderLabels(columns)
        self.tableView_data.setModel(model)
        # 添加数据
        for i, row in enumerate(ds):
            for j, col in enumerate(columns):
                model.setItem(i, j, QStandardItem(getattr(row, col)))



if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建GUI
    ui = MasterWindows()  # 创建PyQt设计的窗体对象
    ui.show()  # 显示窗体
    sys.exit(app.exec())  # 程序关闭时退出进程