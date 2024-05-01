from typing import Type

from dojo_lhama_POO.desafio1.toDo.elevador import Elevador


class Pessoa:
    def __init__(self, nome: str, elevador: Elevador = Type[Elevador]):
        self.nome = nome
        self.andar_usuario = 1
        self.elevador = elevador

    def chamar_elevador(self) -> None:
        self.elevador.buscar_usuario(self.andar_usuario)
        self.entrar_elevador()
        self.definir_andar()
        self.sair_elevador()

    def entrar_elevador(self) -> None:
        print(
            f"{self.nome} entrando no elevador no andar {self.elevador.andar_atual_elevador}"
        )
        self.elevador.inserir_pessoas(self)

    def definir_andar(self) -> None:
        andar_definido_usuario = int(
            input(
                f"Para Qual Andar você deseja ir {self.nome}? de 1 até {self.elevador.max_andares}: ->"
            )
        )
        self.elevador.levar_usuario(andar_definido_usuario)

    def sair_elevador(self) -> None:
        print(
            f"Andar {self.elevador.andar_atual_elevador}, {self.nome} saiu do elevador"
        )
        self.andar_usuario = self.elevador.andar_atual_elevador

    def get_andar_usuario(self) -> None:
        print(f"{self.nome} esta no {self.andar_usuario} andar")
