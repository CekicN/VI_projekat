class Igrac:
    def __init__(self, naziv):
        self.naziv = naziv
        self.poeni = 0
    def __str__(self):
        return f"{self.naziv}: {self.poeni}"
    