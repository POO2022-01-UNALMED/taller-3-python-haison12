class Tv:
    _numTV = 0
    def __init__(self,marca,estado):
        self._canal = 1
        self._precio = 500
        self._volumen = 1
        self._marca = marca
        self._estado = estado
        Tv._numTV += 1

    def set_marca(self,marca):
        self._marca = marca
    def get_marca(self):
        return self._marca
    def set_control(self,control):
        self._control = control
    def get_control(self):
        return self._control
    def set_precio(self,precio):
        self._precio = precio
    def get_precio(self):
        return self._precio
    def set_volumen(self,volumen):
        if self._estado and volumen >= 0 and volumen <=7:
            self._volumen = volumen
    def get_volumen(self):
        return self._volumen
    def set_canal(self,canal):
        if self._estado and canal >= 1 and canal <=120:
            self._canal = canal
    def get_canal(self):
        return self._canal

    @classmethod
    def get_numTv(cls):
        return cls._numTV

    @classmethod
    def set_numTv(cls,numTV):
        Tv._numTV = numTV


    def turnOn(self,estado):
        self._estado = estado
    def turnOff(self,estado):
        self._estado = estado

    def getEstado(self):
        return self._estado


    def canalUp(self):
        if self._estado and self._canal < 120:
            self._canal += 1


    def canalDown(self):
        if self._estado and self._canal > 1:
            self._canal -= 1


    def volumenUp(self):
        if self._estado and self._volumen < 7:
            self._volumen += 1


    def volumenDown(self):
        if self._estado and self._volumen <= 7:
            self._volumen -= 1


