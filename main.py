import view.recursos_rc as recursos_rc
import controller.Controlador as Controlador
import view.interface_agendaFit as interface_agendaFit
from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractItemView
from PySide6.QtCore import QTime
import model.GerenciadorBancoDeDados as GerenciadorBancoDeDados
import os

class MinhaJanela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.interface = interface_agendaFit.Ui_MainWindow()
        self.interface.setupUi(self)
        self.interface.paginas_principais.tabBar().setEnabled(False)

        #Conectando alguns botoes
        self.interface.botao_home.clicked.connect(lambda: self.interface.paginas_principais.setCurrentIndex(0))
        self.interface.botao_lancar.clicked.connect(lambda: self.interface.paginas_principais.setCurrentIndex(1))
        self.interface.botao_agendas.clicked.connect(lambda: self.interface.paginas_principais.setCurrentIndex(2))
        self.interface.botao_pacientes.clicked.connect(lambda: self.interface.paginas_principais.setCurrentIndex(3))
        self.interface.botao_pesquisar_pacientes_menu.clicked.connect(lambda: self.interface.paginas_principais.setCurrentIndex(4))
        self.interface.botao_mais_informacoes.clicked.connect(lambda: self.interface.paginas_principais.setCurrentIndex(5))

        self.interface.tabela_horarios_pesquisa.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.interface.input_hora.setTime(QTime(5,0))

        self.interface.calendario.selectionChanged.connect(lambda: self.interface.input_data.setDate(self.interface.calendario.selectedDate()))
        self.interface.input_data.dateChanged.connect(self.interface.calendario.setSelectedDate)






if __name__ == "__main__":
    app = QApplication([])
    try:
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_do_tema = os.path.join(diretorio_atual, r'view/tema.qss')
        # Abre o arquivo especificando a codificação UTF-8
        with open(caminho_do_tema, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print(f"Arquivo de tema não encontrado em: {caminho_do_tema}")
    except Exception as e:
        print(f"Ocorreu um erro ao carregar o tema: {e}")
    janela = MinhaJanela()
    gerenciador = GerenciadorBancoDeDados.GerenciadorBancoDeDados()
    controlador = Controlador.Controlador(janela.interface, gerenciador)
    janela.interface.botao_lancar_atendimento.clicked.connect(controlador.realizar_lancamento)
    janela.interface.gerar_resumo_paciente.clicked.connect(controlador.gerar_resumo_paciente)
    janela.interface.gerar_mensagem_e_resumo_profissional.clicked.connect(controlador.gerar_resumo_profissional)
    janela.interface.calendario_agenda.selectionChanged.connect(controlador.atualizar_tabela_agenda)
    janela.interface.combox_profissional_agenda.currentIndexChanged.connect(controlador.atualizar_tabela_agenda)
    janela.interface.tabela_horarios.cellChanged.connect(controlador.alterar_atendimento_na_tabela)
    janela.interface.excluir_linha.clicked.connect(controlador.excluir_atendimento_selecionado)
    janela.interface.lancar_paciente_novamente.clicked.connect(controlador.relancar_ultimo_excluido)
    janela.interface.botao_copiar_lancamento.clicked.connect(controlador.copiar_atendimentos_para_data)
    janela.interface.botao_pesquisar_paciente.clicked.connect(controlador.pesquisar_paciente_por_nome)
    






    
    janela.show()
    app.exec()
