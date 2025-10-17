import sqlite3
from .Atendimento import Atendimento
import pathlib


class GerenciadorBancoDeDados:
    def __init__(self):
        caminho_home = pathlib.Path.home()
        caminho_pasta = caminho_home / "AgendaFIT_Data"
        caminho_pasta.mkdir(exist_ok=True)
        self.__caminho_banco = caminho_pasta / "BancoDeDadosAgendaFIT.db"
        self.__connectionDB = None
        self.__cursor = None
        self.__criar_banco()
    
    def popular_dados_iniciais(self, lista_profissionais: list) -> None:
        sql_query = "SELECT nome_profissional FROM profissionais WHERE nome_profissional = ?"
        for profissional in lista_profissionais:    
            self.__cursor.execute(sql_query, (profissional,))
            resultado = self.__cursor.fetchone()
            if not resultado:
                self.__cursor.execute('INSERT INTO profissionais VALUES (NULL, ?)', (profissional,))
        self.__connectionDB.commit()

    def __criar_banco(self) -> None:
        self.__connectionDB = sqlite3.connect(self.__caminho_banco)
        self.__cursor = self.__connectionDB.cursor()
        self.__cursor.execute('CREATE TABLE IF NOT EXISTS profissionais (id_profissional INTEGER PRIMARY KEY AUTOINCREMENT, nome_profissional TEXT NOT NULL)')
        self.__cursor.execute('CREATE TABLE IF NOT EXISTS pacientes (id_paciente  INTEGER PRIMARY KEY AUTOINCREMENT, nome_paciente TEXT NOT NULL)')
        self.__cursor.execute('CREATE TABLE IF NOT EXISTS atendimentos (id_atendimento INTEGER  PRIMARY KEY AUTOINCREMENT, id_profissional INTEGER, id_paciente INTEGER, data TEXT NOT NULL, hora TEXT NOT NULL, descricao TEXT NOT NULL, FOREIGN KEY(id_profissional) REFERENCES profissionais(id_profissional), FOREIGN KEY(id_paciente) REFERENCES pacientes(id_paciente))')
        self.__connectionDB.commit()

    def lancar_atendimento(self, nome_paciente: str, nome_profissional: str, data: str, hora: str, descricao: str) -> None:
        try:
            sql_query_paciente = 'INSERT INTO pacientes VALUES (NULL, ?)'
            sql_query_profissional = 'INSERT INTO profissionais VALUES (NULL, ?)'
            sql_query_atendimento = 'INSERT INTO atendimentos VALUES (NULL, ?, ?, ?, ?, ?)'
            # SALVANDO PACIENTE
            self.__cursor.execute('SELECT id_paciente FROM pacientes WHERE nome_paciente = ?', (nome_paciente,))
            resultado = self.__cursor.fetchone()

            if resultado:
                id_paciente = resultado[0]
            else:
                self.__cursor.execute(sql_query_paciente, (nome_paciente,))
                id_paciente = self.__cursor.lastrowid
            
            # SALVANDO PROFISSIONAL
            self.__cursor.execute('SELECT id_profissional FROM profissionais WHERE nome_profissional = ?', (nome_profissional,))
            resultado = self.__cursor.fetchone()

            if resultado:
                id_profissional = resultado[0]
            else:
                self.__cursor.execute(sql_query_profissional, (nome_profissional,))
                id_profissional = self.__cursor.lastrowid

            # SALVANDO ATENDIMENTO
            self.__cursor.execute(sql_query_atendimento, (id_profissional,id_paciente, data, hora, descricao,))

            self.__connectionDB.commit()

        except sqlite3.Error as erro:
            print(f'ERRO AO SALVAR DADOS: {erro}')
        
        except Exception as e:
            print(f"TIVEMOS UM ERRO: {e}")

    def buscar_atendimento_por_data(self, id_profissional: int, data: str) -> list:
       self.__cursor.execute('SELECT pacientes.nome_paciente, profissionais.nome_profissional, atendimentos.data, atendimentos.hora, atendimentos.descricao, atendimentos.id_atendimento FROM atendimentos JOIN pacientes ON atendimentos.id_paciente = pacientes.id_paciente JOIN profissionais ON atendimentos.id_profissional = profissionais.id_profissional WHERE atendimentos.id_profissional = ? AND atendimentos.data = ? ORDER BY hora ASC', (id_profissional, data,))
       resultado = self.__cursor.fetchall()
       return resultado

    def buscar_atendimentos_por_paciente(self, id_paciente: int) -> list:
        self.__cursor.execute('SELECT pacientes.nome_paciente, profissionais.nome_profissional, atendimentos.data, atendimentos.hora, atendimentos.descricao FROM atendimentos JOIN pacientes ON atendimentos.id_paciente = pacientes.id_paciente JOIN profissionais ON atendimentos.id_profissional = profissionais.id_profissional WHERE atendimentos.id_paciente = ? ORDER BY SUBSTR (data, 7, 4), SUBSTR (data, 4, 2), SUBSTR (data, 1, 2), hora ASC', (id_paciente,))
        resultado = self.__cursor.fetchall()
        return resultado

    def buscar_atendimentos_por_profissional(self, id_profissional: int, mes_e_ano: str) -> list:
        mes_e_ano = "%" + mes_e_ano
        self.__cursor.execute('SELECT pacientes.nome_paciente, profissionais.nome_profissional, atendimentos.data, atendimentos.hora, atendimentos.descricao FROM atendimentos JOIN pacientes ON atendimentos.id_paciente = pacientes.id_paciente JOIN profissionais ON atendimentos.id_profissional = profissionais.id_profissional WHERE atendimentos.id_profissional = ? AND atendimentos.data LIKE ? ORDER BY SUBSTR (data, 7, 4), SUBSTR (data, 4, 2), SUBSTR (data, 1, 2), hora ASC', (id_profissional, mes_e_ano,))
        resultado = self.__cursor.fetchall()
        return resultado

    def excluir_atendimento(self, id_atendimento: int) -> bool:
        try:
            self.__cursor.execute('DELETE FROM atendimentos WHERE atendimentos.id_atendimento = ?', (id_atendimento,))
            self.__connectionDB.commit()
            return True
        except sqlite3.Error as erro:
            print(f'OCORREU UM ERRO AO TENTAR DELETAR: {erro}')
            return False
        except Exception as e:
            print(f'TIVEMOS UM ERRO: {e}')
            return False
        
    def alterar_atendimento(self, id_atendimento: int, atendimento: Atendimento) -> bool:
        try:    
            nome_paciente = atendimento.paciente.nome
            data = atendimento.data
            hora = atendimento.hora
            descricao = atendimento.descricao
            sql_query_paciente = 'INSERT INTO pacientes VALUES (NULL, ?)'

            self.__cursor.execute('SELECT id_paciente FROM pacientes WHERE nome_paciente = ?', (nome_paciente,))
            resultado = self.__cursor.fetchone()
            if resultado:
                id_paciente = resultado[0]
            else:
                self.__cursor.execute(sql_query_paciente, (nome_paciente,))
                id_paciente = self.__cursor.lastrowid

            sql_query_atendimento = 'UPDATE atendimentos SET id_paciente = ?, data = ?, hora = ?, descricao = ? WHERE atendimentos.id_atendimento = ?'
            self.__cursor.execute(sql_query_atendimento, (id_paciente, data, hora, descricao, id_atendimento,))
            self.__connectionDB.commit()
            return True
        except sqlite3.Error as erro:
            print(f'TIVEMOS UM ERRO AO TENTAR ALTERAR O ATENDIMENTO: {erro}')
            return False
        except Exception as e:
            print(f'OCORREU UM ERRO: {e}')
            return False
        
    def contar_pacientes_no_horario(self, id_profissional: int, data: str, hora: str) -> int:
            self.__cursor.execute('SELECT COUNT(*) FROM atendimentos WHERE atendimentos.id_profissional = ? AND atendimentos.data = ? AND atendimentos.hora = ? AND atendimentos.descricao <> "pilates"', (id_profissional, data, hora,))
            resultado = self.__cursor.fetchone()
            return resultado[0]

    def buscar_id_profissional(self, nome_profissional: str) -> int:
        self.__cursor.execute('SELECT profissionais.id_profissional FROM profissionais WHERE profissionais.nome_profissional = ?', (nome_profissional,))
        resultado = self.__cursor.fetchone()
        if resultado:
            return resultado[0]
        return None

    def buscar_id_paciente(self, nome_paciente: str) -> int:
        self.__cursor.execute('SELECT pacientes.id_paciente FROM pacientes WHERE pacientes.nome_paciente = ?', (nome_paciente,))
        resultado = self.__cursor.fetchone()
        if resultado:
            return resultado[0]
        return None