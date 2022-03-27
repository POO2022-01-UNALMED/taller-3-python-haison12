class Control:

    def enlazar(self, Tv):
        self._Tv = Tv
        self._Tv._Control = self

    def turnOn(self):
        self._Tv.turnOn()
    def turnOff(self,estado):
        self._Tv.turnOff()


    def canalUp(self):
        self._Tv.canalUp()


    def canalDown(self):
        self._Tv.canalDown()


    def volumenUp(self):
        self._Tv.volumenUp()


    def volumenDown(self):
        self._Tv.volumenDown()


    def setCanal(self, canal):
        if self._Tv._estado and canal >= 1 and canal <= 120:
            self._Tv._canal = canal

    def get_tv(self):
        return self._Tv

    def volumenUp(self,Tv):
        self._Tv = Tv

