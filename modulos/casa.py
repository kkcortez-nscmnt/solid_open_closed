class Casa:

    def __init__(self) -> None:
        self.__endereco = "Alameda dos Anjos"
        self.__propietario = None

    def acender_luzes(self) -> None:
        print(" Luzes acesas")
    
    def get_endereco(self) -> str:
        return self.__endereco
    
    def set_propietario(self, propietario: any) -> None:
        self.__propietario = propietario
    
    def get_propietario(self) -> any:
        return self.__propietario