


class Control:
    def enlazar(self, tv):
        self._tv = tv
        self._tv._control = self
    
    
    def turnOn(self):
        self._tv.turnOn()

    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()

    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()
    
    def setCanal(self, numero):
        if self._tv._estado and numero >= 1 and numero <= 120:
            self._tv._estado = numero

    

    def setTv(self, tv):
        self._tv = tv
    
    def getTv(self):
        return self._tv