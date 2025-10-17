from .Profissional import Profissional
from .Paciente import Paciente


class Atendimento:
    def __init__(self, paciente: Paciente, profissional: Profissional, data: str, hora: str, descricao: str) -> None:
        self.paciente = paciente
        self.profissional = profissional
        self.data = data.strip()
        self.hora = hora.strip()
        self.descricao = descricao.lower().strip()

    def from_dict(self) -> dict:
        return {"nome": self.paciente.nome, "profissional": self.profissional.nome, "data": self.data, "hora": self.hora, "descricao": self.descricao}
    
