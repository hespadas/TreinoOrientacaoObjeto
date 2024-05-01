class Elevador:
    def __init__(
        self,
        max_andares,
        capacidade_maxima,
    ):
        self.andar_atual_elevador = 1
        self.max_andares = max_andares
        self.capacidade_max = capacidade_maxima
        self._usuarios = []

    def subir(self, andar_destino: int) -> None:
        while self.andar_atual_elevador != andar_destino:
            print(f"subindo, Andar {self.andar_atual_elevador}")
            self.andar_atual_elevador += 1

    def descer(self, andar_destino: int) -> None:
        while self.andar_atual_elevador != andar_destino:
            print(f"descendo, Andar {self.andar_atual_elevador}")
            self.andar_atual_elevador -= 1

    def buscar_usuario(self, andar_usuario: int) -> None:
        if andar_usuario == self.andar_atual_elevador:
            return
        if andar_usuario <= self.andar_atual_elevador:
            self.descer(andar_usuario)
            print(
                f"Elevador Descendo do andar {self.andar_atual_elevador} para o {andar_usuario} "
            )
            self.andar_atual_elevador = andar_usuario
            return
        if andar_usuario >= self.andar_atual_elevador:
            print(
                f"Elevador Subindo do andar {self.andar_atual_elevador} para o {andar_usuario} "
            )
            self.subir(andar_usuario)
            self.andar_atual_elevador = andar_usuario
            return

    def levar_usuario(self, andar_escolha: int) -> None:
        if andar_escolha >= self.andar_atual_elevador:
            self.subir(andar_escolha)
            return
        if andar_escolha <= self.andar_atual_elevador:
            self.descer(andar_escolha)
            return

    def get_pessoas(self) -> None:
        pessoas_elevador = [(pessoa.nome) for pessoa in self._usuarios]
        print(pessoas_elevador)

    def inserir_pessoas(self, pessoa) -> None:
        self._usuarios.append(pessoa)
