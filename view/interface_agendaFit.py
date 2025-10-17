# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_agendaFit.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QDateEdit,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextBrowser, QTimeEdit, QToolBox, QVBoxLayout,
    QWidget)
import view.recursos_rc as recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 730)
        MainWindow.setMinimumSize(QSize(0, 730))
        MainWindow.setMaximumSize(QSize(16777215, 730))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 725))
        self.centralwidget.setMaximumSize(QSize(16777215, 725))
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 735))
        self.frame_2.setMaximumSize(QSize(16777215, 735))
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_da_esquerda = QFrame(self.frame_2)
        self.frame_da_esquerda.setObjectName(u"frame_da_esquerda")
        self.frame_da_esquerda.setMinimumSize(QSize(0, 550))
        self.frame_da_esquerda.setMaximumSize(QSize(150, 625))
        self.frame_da_esquerda.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_da_esquerda.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_da_esquerda)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.paginas_menu_principal = QToolBox(self.frame_da_esquerda)
        self.paginas_menu_principal.setObjectName(u"paginas_menu_principal")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        self.paginas_menu_principal.setFont(font)
        self.paginas_menu_principal.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.paginas_menu_principal.setStyleSheet(u"")
        self.pagina1_menu = QWidget()
        self.pagina1_menu.setObjectName(u"pagina1_menu")
        self.pagina1_menu.setGeometry(QRect(0, 0, 132, 539))
        self.verticalLayout_4 = QVBoxLayout(self.pagina1_menu)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.botao_home = QPushButton(self.pagina1_menu)
        self.botao_home.setObjectName(u"botao_home")
        self.botao_home.setMouseTracking(False)
        self.botao_home.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.botao_home.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botao_home.setIcon(icon)
        self.botao_home.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.botao_home)

        self.botao_lancar = QPushButton(self.pagina1_menu)
        self.botao_lancar.setObjectName(u"botao_lancar")
        icon1 = QIcon()
        icon1.addFile(u":/icons/buton_lancar.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botao_lancar.setIcon(icon1)
        self.botao_lancar.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.botao_lancar)

        self.botao_agendas = QPushButton(self.pagina1_menu)
        self.botao_agendas.setObjectName(u"botao_agendas")
        icon2 = QIcon()
        icon2.addFile(u":/icons/agenda.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botao_agendas.setIcon(icon2)
        self.botao_agendas.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.botao_agendas)

        self.botao_pacientes = QPushButton(self.pagina1_menu)
        self.botao_pacientes.setObjectName(u"botao_pacientes")
        icon3 = QIcon()
        icon3.addFile(u":/icons/paciente.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botao_pacientes.setIcon(icon3)
        self.botao_pacientes.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.botao_pacientes)

        self.botao_pesquisar_pacientes_menu = QPushButton(self.pagina1_menu)
        self.botao_pesquisar_pacientes_menu.setObjectName(u"botao_pesquisar_pacientes_menu")
        icon4 = QIcon()
        icon4.addFile(u":/icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botao_pesquisar_pacientes_menu.setIcon(icon4)
        self.botao_pesquisar_pacientes_menu.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.botao_pesquisar_pacientes_menu)

        self.verticalSpacer = QSpacerItem(20, 300, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.paginas_menu_principal.addItem(self.pagina1_menu, u"MENU")
        self.pagina_informacoes_menu = QWidget()
        self.pagina_informacoes_menu.setObjectName(u"pagina_informacoes_menu")
        self.pagina_informacoes_menu.setGeometry(QRect(0, 0, 126, 110))
        self.verticalLayout_5 = QVBoxLayout(self.pagina_informacoes_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_informacoes_menu = QFrame(self.pagina_informacoes_menu)
        self.frame_informacoes_menu.setObjectName(u"frame_informacoes_menu")
        self.frame_informacoes_menu.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_informacoes_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_informacoes_menu)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.botao_mais_informacoes = QPushButton(self.frame_informacoes_menu)
        self.botao_mais_informacoes.setObjectName(u"botao_mais_informacoes")
        icon5 = QIcon()
        icon5.addFile(u":/icons/informacoes.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botao_mais_informacoes.setIcon(icon5)
        self.botao_mais_informacoes.setIconSize(QSize(30, 30))

        self.verticalLayout_23.addWidget(self.botao_mais_informacoes)

        self.texto_versao_ = QLabel(self.frame_informacoes_menu)
        self.texto_versao_.setObjectName(u"texto_versao_")

        self.verticalLayout_23.addWidget(self.texto_versao_)


        self.verticalLayout_5.addWidget(self.frame_informacoes_menu)

        self.paginas_menu_principal.addItem(self.pagina_informacoes_menu, u"INFORMA\u00c7\u00d5ES")

        self.verticalLayout_2.addWidget(self.paginas_menu_principal)


        self.horizontalLayout_2.addWidget(self.frame_da_esquerda)

        self.frame_da_direira = QFrame(self.frame_2)
        self.frame_da_direira.setObjectName(u"frame_da_direira")
        self.frame_da_direira.setEnabled(True)
        self.frame_da_direira.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_da_direira.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_da_direira)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.paginas_principais = QTabWidget(self.frame_da_direira)
        self.paginas_principais.setObjectName(u"paginas_principais")
        self.paginas_principais.setEnabled(True)
        font1 = QFont()
        font1.setBold(True)
        self.paginas_principais.setFont(font1)
        self.paginas_principais.setUsesScrollButtons(True)
        self.pagina_home = QWidget()
        self.pagina_home.setObjectName(u"pagina_home")
        self.pagina_home.setEnabled(True)
        self.verticalLayout_6 = QVBoxLayout(self.pagina_home)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_logo_do_programa = QLabel(self.pagina_home)
        self.label_logo_do_programa.setObjectName(u"label_logo_do_programa")

        self.verticalLayout_6.addWidget(self.label_logo_do_programa)

        self.paginas_principais.addTab(self.pagina_home, "")
        self.pagina_lancar = QWidget()
        self.pagina_lancar.setObjectName(u"pagina_lancar")
        self.verticalLayout_8 = QVBoxLayout(self.pagina_lancar)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_calendario = QFrame(self.pagina_lancar)
        self.frame_calendario.setObjectName(u"frame_calendario")
        sizePolicy.setHeightForWidth(self.frame_calendario.sizePolicy().hasHeightForWidth())
        self.frame_calendario.setSizePolicy(sizePolicy)
        self.frame_calendario.setMaximumSize(QSize(16777215, 250))
        self.frame_calendario.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_calendario.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_calendario)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.calendario = QCalendarWidget(self.frame_calendario)
        self.calendario.setObjectName(u"calendario")

        self.verticalLayout_9.addWidget(self.calendario)


        self.verticalLayout_8.addWidget(self.frame_calendario)

        self.frame_lancamento = QFrame(self.pagina_lancar)
        self.frame_lancamento.setObjectName(u"frame_lancamento")
        sizePolicy.setHeightForWidth(self.frame_lancamento.sizePolicy().hasHeightForWidth())
        self.frame_lancamento.setSizePolicy(sizePolicy)
        self.frame_lancamento.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_lancamento.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_lancamento)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.input_nome_paciente = QLineEdit(self.frame_lancamento)
        self.input_nome_paciente.setObjectName(u"input_nome_paciente")

        self.verticalLayout_10.addWidget(self.input_nome_paciente)

        self.input_profissional = QComboBox(self.frame_lancamento)
        self.input_profissional.addItem("")
        self.input_profissional.addItem("")
        self.input_profissional.setObjectName(u"input_profissional")

        self.verticalLayout_10.addWidget(self.input_profissional)

        self.input_data = QDateEdit(self.frame_lancamento)
        self.input_data.setObjectName(u"input_data")
        self.input_data.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input_data.sizePolicy().hasHeightForWidth())
        self.input_data.setSizePolicy(sizePolicy1)
        self.input_data.setMaximumSize(QSize(150, 16777215))
        self.input_data.setDateTime(QDateTime(QDate(2025, 1, 1), QTime(15, 0, 0)))
        self.input_data.setMinimumDateTime(QDateTime(QDate(2025, 1, 1), QTime(15, 0, 0)))
        self.input_data.setMaximumDate(QDate(2030, 12, 31))
        self.input_data.setCalendarPopup(True)

        self.verticalLayout_10.addWidget(self.input_data)

        self.input_hora = QTimeEdit(self.frame_lancamento)
        self.input_hora.setObjectName(u"input_hora")
        self.input_hora.setMaximumTime(QTime(23, 59, 59))

        self.verticalLayout_10.addWidget(self.input_hora)

        self.input_descricao = QComboBox(self.frame_lancamento)
        self.input_descricao.addItem("")
        self.input_descricao.addItem("")
        self.input_descricao.addItem("")
        self.input_descricao.addItem("")
        self.input_descricao.setObjectName(u"input_descricao")

        self.verticalLayout_10.addWidget(self.input_descricao)

        self.frame_resumo_atendimento_lancar = QFrame(self.frame_lancamento)
        self.frame_resumo_atendimento_lancar.setObjectName(u"frame_resumo_atendimento_lancar")
        self.frame_resumo_atendimento_lancar.setMaximumSize(QSize(16777215, 100))
        self.frame_resumo_atendimento_lancar.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_resumo_atendimento_lancar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_resumo_atendimento_lancar)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.botao_lancar_atendimento = QPushButton(self.frame_resumo_atendimento_lancar)
        self.botao_lancar_atendimento.setObjectName(u"botao_lancar_atendimento")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.botao_lancar_atendimento.sizePolicy().hasHeightForWidth())
        self.botao_lancar_atendimento.setSizePolicy(sizePolicy2)
        self.botao_lancar_atendimento.setMinimumSize(QSize(0, 0))
        self.botao_lancar_atendimento.setMaximumSize(QSize(150, 45))
        self.botao_lancar_atendimento.setStyleSheet(u"")
        self.botao_lancar_atendimento.setIcon(icon1)
        self.botao_lancar_atendimento.setIconSize(QSize(35, 35))

        self.horizontalLayout_6.addWidget(self.botao_lancar_atendimento)

        self.texto_resumo_atendimento = QLabel(self.frame_resumo_atendimento_lancar)
        self.texto_resumo_atendimento.setObjectName(u"texto_resumo_atendimento")
        sizePolicy.setHeightForWidth(self.texto_resumo_atendimento.sizePolicy().hasHeightForWidth())
        self.texto_resumo_atendimento.setSizePolicy(sizePolicy)
        self.texto_resumo_atendimento.setMaximumSize(QSize(300, 500))

        self.horizontalLayout_6.addWidget(self.texto_resumo_atendimento)


        self.verticalLayout_10.addWidget(self.frame_resumo_atendimento_lancar)


        self.verticalLayout_8.addWidget(self.frame_lancamento)

        self.paginas_principais.addTab(self.pagina_lancar, "")
        self.pagina_agendas = QWidget()
        self.pagina_agendas.setObjectName(u"pagina_agendas")
        self.verticalLayout_11 = QVBoxLayout(self.pagina_agendas)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.paginas_agendas = QTabWidget(self.pagina_agendas)
        self.paginas_agendas.setObjectName(u"paginas_agendas")
        self.agenda_junia = QWidget()
        self.agenda_junia.setObjectName(u"agenda_junia")
        self.verticalLayout_14 = QVBoxLayout(self.agenda_junia)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.combox_profissional_agenda = QComboBox(self.agenda_junia)
        self.combox_profissional_agenda.addItem("")
        self.combox_profissional_agenda.addItem("")
        self.combox_profissional_agenda.setObjectName(u"combox_profissional_agenda")

        self.verticalLayout_14.addWidget(self.combox_profissional_agenda)

        self.frame_calendario_2 = QFrame(self.agenda_junia)
        self.frame_calendario_2.setObjectName(u"frame_calendario_2")
        self.frame_calendario_2.setMaximumSize(QSize(16777215, 210))
        self.frame_calendario_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_calendario_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_calendario_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.calendario_agenda = QCalendarWidget(self.frame_calendario_2)
        self.calendario_agenda.setObjectName(u"calendario_agenda")

        self.verticalLayout_15.addWidget(self.calendario_agenda)


        self.verticalLayout_14.addWidget(self.frame_calendario_2)

        self.frame_agenda_junia = QFrame(self.agenda_junia)
        self.frame_agenda_junia.setObjectName(u"frame_agenda_junia")
        self.frame_agenda_junia.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_agenda_junia.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_agenda_junia)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tabela_horarios = QTableWidget(self.frame_agenda_junia)
        if (self.tabela_horarios.columnCount() < 4):
            self.tabela_horarios.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabela_horarios.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabela_horarios.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabela_horarios.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabela_horarios.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabela_horarios.setObjectName(u"tabela_horarios")
        self.tabela_horarios.setMaximumSize(QSize(400, 16777215))
        self.tabela_horarios.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.tabela_horarios.setFrameShape(QFrame.Shape.VLine)
        self.tabela_horarios.setFrameShadow(QFrame.Shadow.Plain)

        self.horizontalLayout_7.addWidget(self.tabela_horarios)

        self.frame_3 = QFrame(self.frame_agenda_junia)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_3)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.excluir_linha = QPushButton(self.frame_3)
        self.excluir_linha.setObjectName(u"excluir_linha")
        self.excluir_linha.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/icons/excluir.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.excluir_linha.setIcon(icon6)
        self.excluir_linha.setIconSize(QSize(13, 13))

        self.verticalLayout_22.addWidget(self.excluir_linha)

        self.titulo_ultimo_paciente_excluido_2 = QLabel(self.frame_3)
        self.titulo_ultimo_paciente_excluido_2.setObjectName(u"titulo_ultimo_paciente_excluido_2")

        self.verticalLayout_22.addWidget(self.titulo_ultimo_paciente_excluido_2)

        self.texto_ultimo_paciente_lancado_2 = QLabel(self.frame_3)
        self.texto_ultimo_paciente_lancado_2.setObjectName(u"texto_ultimo_paciente_lancado_2")
        sizePolicy.setHeightForWidth(self.texto_ultimo_paciente_lancado_2.sizePolicy().hasHeightForWidth())
        self.texto_ultimo_paciente_lancado_2.setSizePolicy(sizePolicy)

        self.verticalLayout_22.addWidget(self.texto_ultimo_paciente_lancado_2)

        self.lancar_paciente_novamente = QPushButton(self.frame_3)
        self.lancar_paciente_novamente.setObjectName(u"lancar_paciente_novamente")

        self.verticalLayout_22.addWidget(self.lancar_paciente_novamente)

        self.verticalSpacer_3 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_22.addItem(self.verticalSpacer_3)

        self.texto_copiar_lancamento = QLabel(self.frame_3)
        self.texto_copiar_lancamento.setObjectName(u"texto_copiar_lancamento")

        self.verticalLayout_22.addWidget(self.texto_copiar_lancamento)

        self.input_data_para_lancamento_copiado = QDateEdit(self.frame_3)
        self.input_data_para_lancamento_copiado.setObjectName(u"input_data_para_lancamento_copiado")
        self.input_data_para_lancamento_copiado.setMinimumDateTime(QDateTime(QDate(2025, 1, 1), QTime(0, 0, 0)))
        self.input_data_para_lancamento_copiado.setMaximumDate(QDate(2050, 12, 31))
        self.input_data_para_lancamento_copiado.setCalendarPopup(True)

        self.verticalLayout_22.addWidget(self.input_data_para_lancamento_copiado)

        self.botao_copiar_lancamento = QPushButton(self.frame_3)
        self.botao_copiar_lancamento.setObjectName(u"botao_copiar_lancamento")
        self.botao_copiar_lancamento.setFont(font1)
        icon7 = QIcon()
        icon7.addFile(u":/icons/copiar.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botao_copiar_lancamento.setIcon(icon7)
        self.botao_copiar_lancamento.setIconSize(QSize(15, 15))

        self.verticalLayout_22.addWidget(self.botao_copiar_lancamento)


        self.horizontalLayout_7.addWidget(self.frame_3)


        self.verticalLayout_14.addWidget(self.frame_agenda_junia)

        self.paginas_agendas.addTab(self.agenda_junia, "")

        self.verticalLayout_11.addWidget(self.paginas_agendas)

        self.paginas_principais.addTab(self.pagina_agendas, "")
        self.pagina_pacientes = QWidget()
        self.pagina_pacientes.setObjectName(u"pagina_pacientes")
        self.verticalLayout_18 = QVBoxLayout(self.pagina_pacientes)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_gerar_resumo_mensagem = QFrame(self.pagina_pacientes)
        self.frame_gerar_resumo_mensagem.setObjectName(u"frame_gerar_resumo_mensagem")
        self.frame_gerar_resumo_mensagem.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_gerar_resumo_mensagem.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_gerar_resumo_mensagem)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_gerar_resumo_mensagem_ = QFrame(self.frame_gerar_resumo_mensagem)
        self.frame_gerar_resumo_mensagem_.setObjectName(u"frame_gerar_resumo_mensagem_")
        self.frame_gerar_resumo_mensagem_.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_gerar_resumo_mensagem_.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_gerar_resumo_mensagem_)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_gerar_resumo_mensagem_paciente = QFrame(self.frame_gerar_resumo_mensagem_)
        self.frame_gerar_resumo_mensagem_paciente.setObjectName(u"frame_gerar_resumo_mensagem_paciente")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_gerar_resumo_mensagem_paciente.sizePolicy().hasHeightForWidth())
        self.frame_gerar_resumo_mensagem_paciente.setSizePolicy(sizePolicy3)
        self.frame_gerar_resumo_mensagem_paciente.setMaximumSize(QSize(300, 16777215))
        self.frame_gerar_resumo_mensagem_paciente.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_gerar_resumo_mensagem_paciente.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_gerar_resumo_mensagem_paciente)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.input_resumo_nome_paciente = QLineEdit(self.frame_gerar_resumo_mensagem_paciente)
        self.input_resumo_nome_paciente.setObjectName(u"input_resumo_nome_paciente")

        self.verticalLayout_20.addWidget(self.input_resumo_nome_paciente)

        self.gerar_resumo_paciente = QPushButton(self.frame_gerar_resumo_mensagem_paciente)
        self.gerar_resumo_paciente.setObjectName(u"gerar_resumo_paciente")

        self.verticalLayout_20.addWidget(self.gerar_resumo_paciente)


        self.horizontalLayout_5.addWidget(self.frame_gerar_resumo_mensagem_paciente)

        self.frame_gerar_resumo_mensagem_profissional = QFrame(self.frame_gerar_resumo_mensagem_)
        self.frame_gerar_resumo_mensagem_profissional.setObjectName(u"frame_gerar_resumo_mensagem_profissional")
        sizePolicy3.setHeightForWidth(self.frame_gerar_resumo_mensagem_profissional.sizePolicy().hasHeightForWidth())
        self.frame_gerar_resumo_mensagem_profissional.setSizePolicy(sizePolicy3)
        self.frame_gerar_resumo_mensagem_profissional.setMaximumSize(QSize(300, 16777215))
        self.frame_gerar_resumo_mensagem_profissional.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_gerar_resumo_mensagem_profissional.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_gerar_resumo_mensagem_profissional)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.input_profissional_resumo = QComboBox(self.frame_gerar_resumo_mensagem_profissional)
        self.input_profissional_resumo.addItem("")
        self.input_profissional_resumo.addItem("")
        self.input_profissional_resumo.setObjectName(u"input_profissional_resumo")

        self.verticalLayout_19.addWidget(self.input_profissional_resumo)

        self.mes_e_ano_resumo_profissional = QDateEdit(self.frame_gerar_resumo_mensagem_profissional)
        self.mes_e_ano_resumo_profissional.setObjectName(u"mes_e_ano_resumo_profissional")
        self.mes_e_ano_resumo_profissional.setMaximumDateTime(QDateTime(QDate(2051, 1, 5), QTime(23, 59, 59)))
        self.mes_e_ano_resumo_profissional.setMinimumDateTime(QDateTime(QDate(2025, 1, 1), QTime(0, 0, 0)))
        self.mes_e_ano_resumo_profissional.setMinimumDate(QDate(2025, 1, 1))
        self.mes_e_ano_resumo_profissional.setCalendarPopup(True)

        self.verticalLayout_19.addWidget(self.mes_e_ano_resumo_profissional)

        self.gerar_mensagem_e_resumo_profissional = QPushButton(self.frame_gerar_resumo_mensagem_profissional)
        self.gerar_mensagem_e_resumo_profissional.setObjectName(u"gerar_mensagem_e_resumo_profissional")

        self.verticalLayout_19.addWidget(self.gerar_mensagem_e_resumo_profissional)


        self.horizontalLayout_5.addWidget(self.frame_gerar_resumo_mensagem_profissional)


        self.horizontalLayout_4.addWidget(self.frame_gerar_resumo_mensagem_)


        self.verticalLayout_18.addWidget(self.frame_gerar_resumo_mensagem)

        self.frame_gerar_mensagem_e_resumo = QFrame(self.pagina_pacientes)
        self.frame_gerar_mensagem_e_resumo.setObjectName(u"frame_gerar_mensagem_e_resumo")
        self.frame_gerar_mensagem_e_resumo.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_gerar_mensagem_e_resumo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_gerar_mensagem_e_resumo)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.mesagem_ou_resumo_final_texto = QTextBrowser(self.frame_gerar_mensagem_e_resumo)
        self.mesagem_ou_resumo_final_texto.setObjectName(u"mesagem_ou_resumo_final_texto")

        self.verticalLayout_21.addWidget(self.mesagem_ou_resumo_final_texto)


        self.verticalLayout_18.addWidget(self.frame_gerar_mensagem_e_resumo)

        self.paginas_principais.addTab(self.pagina_pacientes, "")
        self.tela_procurar_pacientes = QWidget()
        self.tela_procurar_pacientes.setObjectName(u"tela_procurar_pacientes")
        self.horizontalLayout = QHBoxLayout(self.tela_procurar_pacientes)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_pesquisar_pacientes = QFrame(self.tela_procurar_pacientes)
        self.frame_pesquisar_pacientes.setObjectName(u"frame_pesquisar_pacientes")
        self.frame_pesquisar_pacientes.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_pesquisar_pacientes.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_pesquisar_pacientes)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame = QFrame(self.frame_pesquisar_pacientes)
        self.frame.setObjectName(u"frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setMinimumSize(QSize(600, 0))
        self.frame.setMaximumSize(QSize(750, 100))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.input_nome_paciente_pesquisar = QLineEdit(self.frame)
        self.input_nome_paciente_pesquisar.setObjectName(u"input_nome_paciente_pesquisar")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.input_nome_paciente_pesquisar.sizePolicy().hasHeightForWidth())
        self.input_nome_paciente_pesquisar.setSizePolicy(sizePolicy5)
        self.input_nome_paciente_pesquisar.setMinimumSize(QSize(150, 35))
        self.input_nome_paciente_pesquisar.setMaximumSize(QSize(550, 16777215))

        self.horizontalLayout_3.addWidget(self.input_nome_paciente_pesquisar)

        self.botao_pesquisar_paciente = QPushButton(self.frame)
        self.botao_pesquisar_paciente.setObjectName(u"botao_pesquisar_paciente")
        self.botao_pesquisar_paciente.setMinimumSize(QSize(55, 45))
        self.botao_pesquisar_paciente.setMaximumSize(QSize(105, 16777215))
        self.botao_pesquisar_paciente.setIcon(icon4)
        self.botao_pesquisar_paciente.setIconSize(QSize(19, 19))

        self.horizontalLayout_3.addWidget(self.botao_pesquisar_paciente)


        self.verticalLayout_12.addWidget(self.frame)

        self.frame_4 = QFrame(self.frame_pesquisar_pacientes)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabela_horarios_pesquisa = QTableWidget(self.frame_4)
        if (self.tabela_horarios_pesquisa.columnCount() < 5):
            self.tabela_horarios_pesquisa.setColumnCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabela_horarios_pesquisa.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabela_horarios_pesquisa.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabela_horarios_pesquisa.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabela_horarios_pesquisa.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabela_horarios_pesquisa.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        self.tabela_horarios_pesquisa.setObjectName(u"tabela_horarios_pesquisa")
        self.tabela_horarios_pesquisa.setMaximumSize(QSize(16777215, 650))

        self.verticalLayout_7.addWidget(self.tabela_horarios_pesquisa)


        self.verticalLayout_12.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame_pesquisar_pacientes)

        self.paginas_principais.addTab(self.tela_procurar_pacientes, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_24 = QVBoxLayout(self.tab)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout_24.addWidget(self.label_2)

        self.paginas_principais.addTab(self.tab, "")

        self.verticalLayout_3.addWidget(self.paginas_principais)


        self.horizontalLayout_2.addWidget(self.frame_da_direira)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.paginas_menu_principal.setCurrentIndex(0)
        self.paginas_principais.setCurrentIndex(0)
        self.paginas_agendas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.botao_home.setText("")
        self.botao_lancar.setText("")
        self.botao_agendas.setText("")
        self.botao_pacientes.setText("")
        self.botao_pesquisar_pacientes_menu.setText("")
        self.paginas_menu_principal.setItemText(self.paginas_menu_principal.indexOf(self.pagina1_menu), QCoreApplication.translate("MainWindow", u"MENU", None))
        self.botao_mais_informacoes.setText("")
        self.texto_versao_.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">AGENDA FIT<br/>v2.0.0</p></body></html>", None))
        self.paginas_menu_principal.setItemText(self.paginas_menu_principal.indexOf(self.pagina_informacoes_menu), QCoreApplication.translate("MainWindow", u"INFORMA\u00c7\u00d5ES", None))
        self.label_logo_do_programa.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#0b43c5;\"><br/></span><span style=\" font-size:28pt; font-weight:600; color:#000000;\">AGENDA FIT</span></p></body></html>", None))
        self.paginas_principais.setTabText(self.paginas_principais.indexOf(self.pagina_home), QCoreApplication.translate("MainWindow", u"Home", None))
        self.input_nome_paciente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DO PACIENTE", None))
        self.input_profissional.setItemText(0, QCoreApplication.translate("MainWindow", u"FERNANDA", None))
        self.input_profissional.setItemText(1, QCoreApplication.translate("MainWindow", u"JUNIA", None))

        self.input_descricao.setItemText(0, QCoreApplication.translate("MainWindow", u"CISLAV", None))
        self.input_descricao.setItemText(1, QCoreApplication.translate("MainWindow", u"AVALIA\u00c7\u00c3O", None))
        self.input_descricao.setItemText(2, QCoreApplication.translate("MainWindow", u"PARTICULAR", None))
        self.input_descricao.setItemText(3, QCoreApplication.translate("MainWindow", u"PILATES", None))

        self.botao_lancar_atendimento.setText("")
        self.botao_lancar_atendimento.setProperty(u"class", "")
        self.texto_resumo_atendimento.setText("")
        self.paginas_principais.setTabText(self.paginas_principais.indexOf(self.pagina_lancar), QCoreApplication.translate("MainWindow", u"Lan\u00e7ar", None))
        self.combox_profissional_agenda.setItemText(0, QCoreApplication.translate("MainWindow", u"FERNANDA", None))
        self.combox_profissional_agenda.setItemText(1, QCoreApplication.translate("MainWindow", u"JUNIA", None))

        ___qtablewidgetitem = self.tabela_horarios.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"PACIENTE", None));
        ___qtablewidgetitem1 = self.tabela_horarios.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"HOR\u00c1RIO", None));
        ___qtablewidgetitem2 = self.tabela_horarios.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"DESCRI\u00c7\u00c3O", None));
        ___qtablewidgetitem3 = self.tabela_horarios.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ID ATENDIMENTO", None));
        self.excluir_linha.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR LINHA", None))
        self.excluir_linha.setProperty(u"class", "")
        self.titulo_ultimo_paciente_excluido_2.setText(QCoreApplication.translate("MainWindow", u"\u00daltimo paciente exclu\u00eddo:", None))
        self.texto_ultimo_paciente_lancado_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.lancar_paciente_novamente.setText(QCoreApplication.translate("MainWindow", u"LAN\u00c7AR NOVAMENTE", None))
        self.texto_copiar_lancamento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">COPIAR MESMOS <br/>LAN\u00c7AMENTOS<br/>PARA DIA DIFERENTE</span></p></body></html>", None))
        self.input_data_para_lancamento_copiado.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
        self.botao_copiar_lancamento.setText(QCoreApplication.translate("MainWindow", u"COPIAR", None))
        self.paginas_agendas.setTabText(self.paginas_agendas.indexOf(self.agenda_junia), QCoreApplication.translate("MainWindow", u"AGENDAS", None))
        self.paginas_principais.setTabText(self.paginas_principais.indexOf(self.pagina_agendas), QCoreApplication.translate("MainWindow", u"Agendas", None))
        self.input_resumo_nome_paciente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DO PACIENTE", None))
        self.gerar_resumo_paciente.setText(QCoreApplication.translate("MainWindow", u"RESUMO", None))
        self.gerar_resumo_paciente.setProperty(u"class", "")
        self.input_profissional_resumo.setItemText(0, QCoreApplication.translate("MainWindow", u"FERNANDA", None))
        self.input_profissional_resumo.setItemText(1, QCoreApplication.translate("MainWindow", u"JUNIA", None))

        self.mes_e_ano_resumo_profissional.setDisplayFormat(QCoreApplication.translate("MainWindow", u"MM/yyyy", None))
        self.gerar_mensagem_e_resumo_profissional.setText(QCoreApplication.translate("MainWindow", u"RESUMO ", None))
        self.gerar_mensagem_e_resumo_profissional.setProperty(u"class", "")
        self.mesagem_ou_resumo_final_texto.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:600;\"><br /></p></body></html>", None))
        self.paginas_principais.setTabText(self.paginas_principais.indexOf(self.pagina_pacientes), QCoreApplication.translate("MainWindow", u"Pacientes", None))
        self.input_nome_paciente_pesquisar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o nome do paciente para buscar...", None))
        self.botao_pesquisar_paciente.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        ___qtablewidgetitem4 = self.tabela_horarios_pesquisa.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"PACIENTE", None));
        ___qtablewidgetitem5 = self.tabela_horarios_pesquisa.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"PROFISSIONAL", None));
        ___qtablewidgetitem6 = self.tabela_horarios_pesquisa.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"DATA", None));
        ___qtablewidgetitem7 = self.tabela_horarios_pesquisa.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"HORA", None));
        ___qtablewidgetitem8 = self.tabela_horarios_pesquisa.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"DESCRI\u00c7\u00c3O", None));
        self.paginas_principais.setTabText(self.paginas_principais.indexOf(self.tela_procurar_pacientes), QCoreApplication.translate("MainWindow", u"Hor\u00e1rios", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">AGENDA FIT - 2.0</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:12pt;\">Autor - </span><span style=\" font-size:12pt; font-style:italic;\">Kauan Augusto Naves</span></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:14pt;\">Descri\u00e7\u00e3o:</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Este programa foi feito para o controle de atendimentos em uma academia,<br/>organizando os agendamentos di\u00e1rios e gerando resumos por profissional com datas,<br/>hor\u00e1rios e nomes dos pacientes.</span></p></body></html>", None))
        self.paginas_principais.setTabText(self.paginas_principais.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Sobre", None))
    # retranslateUi

