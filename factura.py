# Trebuie creată clasa Factura care reprezintă factura la energie.
# Atributele necesare sunt: consumul (kWh), costul unui kWh și un cost fix de întreținere pe lună
# Creați un constructor pentru a inițializa atribute. Atenție la tipul lor. Creați setter și getter pentru atributul consum.
# Faceti verificările necesare atributelor Folosiți atributele
# pentru a calcula costul total al facturii în funcție de atribute.
# Folosiți __str__ pentru a afișa acest cost

class Factura:
    COUNTER = 1000

    def __init__(self, consume: int, kw_cost: float = 1.1, maintainance_cost=20):
        Factura.COUNTER += 1
        self.__id = Factura.COUNTER
        self.__consume = consume
        self.__kw_cost = kw_cost
        self.__maintainance_cost = maintainance_cost
        self.__total = self.__consume * self.__kw_cost + self.__maintainance_cost

    @property
    def consume(self):
        return self.__consume

    @consume.setter
    def consume(self, new):
        if isinstance(new, int) and new in range(1, 1000):
            self.__consume = new
            self.__total = self.__consume * self.__kw_cost + self.__maintainance_cost

    @property
    def total(self):
        return self.__total

    def __str__(self):
        return f'Factura ID: {self.__id}\nConsum: {self.__consume}kWh\n Total factura: {self.total:.2f}lei'
