from typing import Type

class Casa:
    def __init__(self) -> None:
        self._endereco = "Alameda dos Anjos - 666, PalletTown "
    
    def acender_luzes(self) -> None:
        print("Estou Acendendo as luzes")
    
    def get_endereco(self) -> str:
        return self.__endereco
    

class Pessoa:

    def __init__(self, nome: str, local: Type[Casa]) -> None:
        self.__nome = nome
        self.__local = local
    
    def entrar_no_local(self) -> None:
        self.__local.acender_luzes()

    def apresentar_local(self, local: any) -> None:
        endereco = local.get_endereco()
        print(endereco)
        

 