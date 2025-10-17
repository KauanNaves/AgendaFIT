from model.Paciente import Paciente
from model.Atendimento import Atendimento
from model.Profissional import Profissional
import view.interface_agendaFit as interface_agendaFit
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox, QFileDialog
import model.GerenciadorBancoDeDados as GerenciadorBancoDeDados

class Controlador:
    def __init__(self, interface: interface_agendaFit.Ui_MainWindow, banco_de_dados: GerenciadorBancoDeDados.GerenciadorBancoDeDados):
        self.interface = interface
        self.db = banco_de_dados
        self.ultimo_excluido = []
        self.lista_profissionais = ["fernanda", "junia"]
        self.db.popular_dados_iniciais(self.lista_profissionais)
    
    def __dados(self):
        nome_profissional = self.interface.combox_profissional_agenda.currentText().lower().strip()
        profissional = Profissional(nome_profissional.lower().strip())
        data = self.interface.calendario_agenda.selectedDate().toString("dd/MM/yyyy")
        tabela = self.interface.tabela_horarios
        calendario = self.interface.calendario_agenda
        lista = [nome_profissional, profissional, data, tabela, calendario]
        return lista
        
    def realizar_lancamento(self):
        try:
            nome = self.interface.input_nome_paciente.text().lower().strip()
            profissional = self.interface.input_profissional.currentText().lower().strip()
            data = self.interface.input_data.date().toString("dd/MM/yyyy")
            hora = self.interface.input_hora.time().toString("HH:mm")
            descricao = self.interface.input_descricao.currentText().lower().strip()
            id_profissional = self.db.buscar_id_profissional(profissional)
            if not id_profissional:
                QMessageBox.warning(None, "ERRO", "PROFISSIONAL NÃO ENCONTRADO!")
                return None
            pacientes_no_horario = self.db.contar_pacientes_no_horario(id_profissional, data, hora)
            prosseguir_com_lancamento = False 
            if nome == "":
                QMessageBox.warning(None, "ERRO", "Nome incorreto!")
                return None    
            if pacientes_no_horario < 4: 
                prosseguir_com_lancamento = True   
                mensagem_sucesso = f"Atendimento lançado com sucesso!"
            else:
                resposta = QMessageBox.question(None, "Limite atingido!", f"Já existem {pacientes_no_horario} pacientes agendados para a hora {hora}.\nDeseja agendar mesmo assim?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if resposta == QMessageBox.StandardButton.Yes:
                    prosseguir_com_lancamento = True    
                    mensagem_sucesso = f"Lançamento realizado com sucesso! Agora existem {pacientes_no_horario + 1} pacientes agendados neste horário."

            if prosseguir_com_lancamento:   
                    self.db.lancar_atendimento(nome, profissional, data, hora, descricao) 
                    resumo_html = f"""
        NOME: {nome.upper()}<br>
        PROFISSIONAL: {profissional.upper()}<br>
        DATA: {data}<br>
        HORA: {hora}<br>
        DESCRIÇÃO: {descricao.upper()}
                        """
                    self.interface.texto_resumo_atendimento.setText(resumo_html)
                    QMessageBox.information(None, "Sucesso", mensagem_sucesso)
            else:
                self.interface.texto_resumo_atendimento.clear()

        except Exception as e:
            QMessageBox.critical(None, "Erro", f"Não foi possível realizar o lançamento: {e}")
            self.interface.texto_resumo_atendimento.clear()

    def atualizar_tabela_agenda(self): #ATUALIZAR AS TABELAS DE HORARIOS DAS PROFISSIONAIS
        nome_profissional = self.interface.combox_profissional_agenda.currentText().lower().strip()
        data = self.interface.calendario_agenda.selectedDate().toString("dd/MM/yyyy")
        tabela = self.interface.tabela_horarios
        id_profissional = self.db.buscar_id_profissional(nome_profissional)
        if id_profissional:
            atendimentos = self.db.buscar_atendimento_por_data(id_profissional, data)
        else:
            QMessageBox.warning(None, "ERRO", "PROFISSIONAL NÃO ENCONTRADO!")
            return None
        self._renderizar_tabela(atendimentos,tabela)

    def _renderizar_tabela(self, tupla_atendimentos: tuple, tabela):
        self.interface.tabela_horarios.blockSignals(True)
        
        tabela.clearContents()
        tabela.setRowCount(0)
        tabela.setRowCount(len(tupla_atendimentos))
        for i, atendimento_dados in enumerate(tupla_atendimentos):
            paciente = atendimento_dados[0].upper().strip()
            horario = atendimento_dados[3]
            descricao = atendimento_dados[4].upper().strip()
            id_atendimento = atendimento_dados[5]
            item_paciente = QTableWidgetItem(paciente)
            item_horario = QTableWidgetItem(horario)
            item_descricao = QTableWidgetItem(descricao)
            item_id_atendimento = QTableWidgetItem(str(id_atendimento))
            tabela.setItem(i, 0, item_paciente)
            tabela.setItem(i, 1, item_horario)
            tabela.setItem(i, 2, item_descricao)
            tabela.setItem(i, 3, item_id_atendimento)
            tabela.setColumnHidden(3, True)
            tabela.resizeColumnsToContents()
        self.interface.tabela_horarios.blockSignals(False)

    def excluir_atendimento_selecionado(self):
        try:
            *__, tabela, calendario = self.__dados()
            texto_resumo_excluido = self.interface.texto_ultimo_paciente_lancado_2
            linha = tabela.currentRow()
            nome_profissional = self.interface.combox_profissional_agenda.currentText().strip().lower()

            if linha != (-1):
                nome = tabela.item(linha, 0).text().strip().lower()
                print(nome)
                data = calendario.selectedDate().toString("dd/MM/yyyy")
                hora = tabela.item(linha, 1).text().strip()
                print(hora)
                descricao = tabela.item(linha, 2).text().lower().strip()
                print(descricao)
                id_atendimento = tabela.item(linha, 3).text()
                print(id_atendimento)
                self.ultimo_excluido = [nome, nome_profissional, data, hora, descricao]
                self.db.excluir_atendimento(int(id_atendimento))
                    
                resumo_html = f"""
        NOME: {nome.title()}<br>
        PROFISSIONAL: {nome_profissional.title()}<br>
        DATA: {data}<br>
        HORA: {hora}<br>
        DESCRIÇÃO: {descricao.upper()}
        """
                texto_resumo_excluido.setText(resumo_html)
                QMessageBox.information(None, "SUCESSO", "Atendimento excluído!")
                self.atualizar_tabela_agenda()
            else:
                QMessageBox.warning(None, "Aviso", "Selecione uma linha para excluir!")
        except Exception as e:
            print(e)

    def relancar_ultimo_excluido(self): 
        ultimo_excluido = self.ultimo_excluido
        if ultimo_excluido:
            self.db.lancar_atendimento(*ultimo_excluido)
            self.atualizar_tabela_agenda()
            QMessageBox.information(None, "Sucesso", "Paciente relançado!")
        else:
            QMessageBox.warning(None, "Erro", "Tivemos um erro ao tentar relançar o atendimento!")
            return None

    def copiar_atendimentos_para_data(self):
        nome_profissional = self.interface.combox_profissional_agenda.currentText().lower().strip()
        data = self.interface.calendario_agenda.selectedDate().toString("dd/MM/yyyy")
        id_profisional = self.db.buscar_id_profissional(nome_profissional)
        if not id_profisional:
            QMessageBox.warning(None, "Erro", "Profissional não encontrado!")
            return None
        
        nova_data = self.interface.input_data_para_lancamento_copiado.date()
        nova_data_formatada = nova_data.toString("dd/MM/yyyy")

        tupla_atendimentos = self.db.buscar_atendimento_por_data(id_profisional, data)
        for atendimento_dados in tupla_atendimentos:
            nome_paciente = atendimento_dados[0]
            hora = atendimento_dados[3]
            descricao = atendimento_dados[4]
            self.db.lancar_atendimento(nome_paciente, nome_profissional, nova_data_formatada, hora, descricao)

        QMessageBox.information(None, "Sucesso", "Dia copiado!")
        
    def alterar_atendimento_na_tabela(self, linha: int, coluna: int):
        nome_profissional = self.interface.combox_profissional_agenda.currentText().lower().strip()
        data = self.interface.calendario_agenda.selectedDate().toString("dd/MM/yyyy")
        tabela = self.interface.tabela_horarios
        id_profissional = self.db.buscar_id_profissional(nome_profissional)
        
        if not id_profissional:
            QMessageBox.warning(None, "ERRO", "TIVEMOS UM ERRO AO PROCURAR O PROFISSIONAL!")
            return None
        
        nome_antigo = tabela.item(linha, 0).text().strip().lower()
        horario_antigo = tabela.item(linha, 1).text().strip()
        descricao_antiga = tabela.item(linha, 2).text().strip().lower()
        novo_valor = tabela.item(linha, coluna).text().strip()
        
        if coluna == 0:
            novo_atendimento = Atendimento(Paciente(novo_valor.lower()), Profissional(nome_profissional), data, horario_antigo, descricao_antiga)
        elif coluna == 1:
            novo_atendimento = Atendimento(Paciente(nome_antigo), Profissional(nome_profissional), data, novo_valor, descricao_antiga)
        elif coluna == 2:
            novo_atendimento = Atendimento(Paciente(nome_antigo), Profissional(nome_profissional), data, horario_antigo, novo_valor.lower())
        id_atendimento = int(tabela.item(linha, 3).text())
        self.db.alterar_atendimento(id_atendimento, novo_atendimento)
        QMessageBox.information(None, "SUCESSO", "Atendimento alterado!")

    def gerar_resumo_paciente(self):
        nome_paciente = self.interface.input_resumo_nome_paciente.text().strip().lower()
        id_paciente = self.db.buscar_id_paciente(nome_paciente)
        if not id_paciente:
            QMessageBox.warning(None, "ERRO", "PACIENTE NÃO ENCONTRADO!")
            return None
        tupla_atendimentos = self.db.buscar_atendimentos_por_paciente(id_paciente)
        if not tupla_atendimentos:
            QMessageBox.warning(None, "ERRO", "ATENDIMENTOS NÃO ENCONTRADOS!")
            return None

        resumo = f"Olá {nome_paciente.title()} segue seus horários de fisioterapia:\n"

        for i, atendimento_dados in enumerate(tupla_atendimentos):
            if atendimento_dados[4] == "avaliação":
                resumo += f"\n{nome_paciente.title()} AVALIAÇÃO DIA {atendimento_dados[2]}\n{nome_paciente.title()} 1° ATENDIMENTO DIA {atendimento_dados[2]}"
            else:
                resumo += f"\n{nome_paciente.title()} {i + 1}° ATENDIMENTO DIA {atendimento_dados[2]} - HORA: {atendimento_dados[3]}"

        QMessageBox.information(None, "Sucesso", "Resumo gerado!")
        self.interface.mesagem_ou_resumo_final_texto.setText(resumo)
        
    def gerar_resumo_profissional(self):
        data = self.interface.mes_e_ano_resumo_profissional.date().toString("MM/yyyy").strip()
        nome_profissional = self.interface.input_profissional_resumo.currentText().lower().strip()
        id_profissional = self.db.buscar_id_profissional(nome_profissional)
        if not id_profissional:
            QMessageBox.warning(None, 'ERRO', "ERRO AO ENCONTRAR O PROFISSIONAL!")
            return None
        
        resumo = ""
        tupla_de_atendimentos = self.db.buscar_atendimentos_por_profissional(id_profissional, data)
        if not tupla_de_atendimentos:
            QMessageBox.warning(None, "ERRO", "NENHUM ATENDIMENTO ENCONTRADO!")
            return None
        data = tupla_de_atendimentos[0][2]

        agenda_agrupada = dict()
        for atendimento_dados in tupla_de_atendimentos:
            if atendimento_dados[2] in agenda_agrupada.keys():
                if atendimento_dados[3] in agenda_agrupada[atendimento_dados[2]].keys():
                    agenda_agrupada[atendimento_dados[2]][atendimento_dados[3]].append(atendimento_dados[0])
                else:
                    agenda_agrupada[atendimento_dados[2]][atendimento_dados[3]] = [atendimento_dados[0]]
            else:
                agenda_agrupada[atendimento_dados[2]] = {atendimento_dados[3]: [atendimento_dados[0]]}

        for data in agenda_agrupada:
            resumo += f"\n\nDIA {data}"
            for hora in agenda_agrupada[data]:
                resumo += f"\n{hora}"
                lista_nomes = [nome.upper().strip() for nome in agenda_agrupada[data][hora]]
                resumo += f" - {' | '.join(lista_nomes)}"

        if not resumo:
            QMessageBox.warning(None, "ERRO", "Agenda não encontrada!")
            resumo = ""
        else:
            QMessageBox.information(None, "Sucesso", "Resumo gerado!")
        self.interface.mesagem_ou_resumo_final_texto.setText(resumo)

    def _exibir_horarios_paciente(self, tupla_atendimentos: tuple):
        self.interface.tabela_horarios_pesquisa.blockSignals(True)
        tabela = self.interface.tabela_horarios_pesquisa

        tabela.clearContents()
        tabela.setRowCount(0)
        tabela.setRowCount(len(tupla_atendimentos))
        for i, atendimento_dados in enumerate(tupla_atendimentos):
            paciente = atendimento_dados[0].upper().strip()
            profissional = atendimento_dados[1].upper().strip()
            data = atendimento_dados[2]
            horario = atendimento_dados[3]
            descricao = atendimento_dados[4].upper().strip()
            item_paciente = QTableWidgetItem(paciente)
            item_profissional = QTableWidgetItem(profissional)
            item_data = QTableWidgetItem(data)
            item_horario = QTableWidgetItem(horario)
            item_descricao = QTableWidgetItem(descricao)
            tabela.setItem(i, 0, item_paciente)
            tabela.setItem(i, 1, item_profissional)
            tabela.setItem(i, 2, item_data)
            tabela.setItem(i, 3, item_horario)
            tabela.setItem(i, 4, item_descricao)
            tabela.resizeColumnsToContents()

        self.interface.tabela_horarios_pesquisa.blockSignals(False)
        
    def pesquisar_paciente_por_nome(self):
        nome_paciente = self.interface.input_nome_paciente_pesquisar.text().lower().strip()
        id_paciente = self.db.buscar_id_paciente(nome_paciente)
        if not id_paciente:
            QMessageBox.warning(None, "ERRO", "PACIENTE NÃO ENCONTRADO!")
            return None
        tupla_atendimentos = self.db.buscar_atendimentos_por_paciente(id_paciente)
        self._exibir_horarios_paciente(tupla_atendimentos)
        if tupla_atendimentos:
            QMessageBox.information(None, "SUCESSO", "Paciente encontrado!")
        else:
            QMessageBox.warning(None, "ERRO", "Paciente não encontrado!")

