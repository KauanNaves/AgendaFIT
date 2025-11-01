## AgendaFIT

                Agenda FIT - Sistema de Agendamento
Agenda FIT é um sistema de desktop desenvolvido em Python com PySide6, projetado para gerenciar agendamentos de pacientes para profissionais em uma clínica ou academia. O sistema oferece uma interface gráfica intuitiva para facilitar o controle de horários, a geração de resumos e a consulta de atendimentos.

## Motivação

O Agenda FIT não é apenas um projeto de estudo, mas uma solução desenvolvida para atender a uma necessidade real. A gestão de agendamentos em uma academia local era realizada de forma manual utilizando agendas de papel, o que gerava desafios como:

* Dificuldade para visualizar rapidamente os horários vagos e preenchidos.
* Lentidão para gerar relatórios mensais para os profissionais.
* Risco de erros manuais e perda de informações.
* Falta de um histórico consolidado e de fácil acesso para cada paciente.

O objetivo deste software foi criar uma ferramenta centralizada, ágil e confiável para transformar essa rotina. Com a automação, o tempo gasto com a gestão da agenda foi drasticamente reduzido de 8 horas para apenas 2 horas, representando uma economia de 75% no tempo e permitindo que a equipe se concentre mais no atendimento ao paciente.



## Descrição
Este projeto foi criado para otimizar a organização de atendimentos diários, permitindo que os profissionais visualizem suas agendas, lancem novos horários e gerem relatórios mensais de forma rápida e eficiente. O sistema utiliza um banco de dados local SQLite3 para armazenar todas as informações de forma segura e persistente na máquina do usuário.

## Funcionalidades Principais
O sistema conta com as seguintes funcionalidades:

Agendamento de Atendimentos: Permite registrar novos atendimentos informando o nome do paciente, o profissional responsável, data, hora e uma descrição (ex: Avaliação, Pilates, Particular).

Visualização de Agenda Diária: Apresenta uma tabela com todos os atendimentos de um profissional para uma data específica, selecionada através de um calendário interativo.

Edição e Exclusão de Agendamentos: É possível alterar informações diretamente na tabela de horários ou excluir um atendimento com um clique.

Cópia de Agendamentos: Funcionalidade para copiar todos os atendimentos de um dia para outra data, ideal para agendamentos recorrentes.

Geração de Resumos para Profissionais: Gera um relatório de texto com todos os atendimentos de um profissional para um determinado mês e ano, agrupados por dia e hora.

Histórico de Pacientes: Permite pesquisar por um paciente e exibir todo o seu histórico de atendimentos, incluindo datas, horários e profissionais.

Persistência de Dados: As informações são salvas localmente em um banco de dados SQLite, garantindo que os dados não sejam perdidos ao fechar o programa.

## Tecnologias Utilizadas
- Linguagem: Python 3

- Interface Gráfica (GUI): PySide6 (Qt for Python)

- Banco de Dados: SQLite3

- Manipulação de Caminhos: pathlib para gerenciamento de diretórios de forma multiplataforma.

## Estrutura do Projeto
O código está organizado seguindo uma estrutura que separa as responsabilidades em diferentes camadas (Model-View-Controller):

main.py: Ponto de entrada da aplicação, responsável por iniciar a interface e conectar os eventos aos métodos do controlador.

view/: Contém os arquivos da interface gráfica (interface_agendaFit.py), recursos visuais (recursos_rc.py) e o arquivo de estilo (tema.qss).

controller/Controlador.py: Orquestra a lógica da aplicação, intermediando a comunicação entre a interface do usuário (View) e o banco de dados (Model).

model/: Inclui as classes de dados (Paciente.py, Profissional.py, Atendimento.py) e o GerenciadorBancoDeDados.py, que encapsula toda a lógica de acesso e manipulação dos dados.

