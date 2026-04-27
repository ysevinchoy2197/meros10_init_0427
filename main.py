#10-misol
class Kompyuter:
    def __init__(self, nomi):
        self.nomi = nomi

    def yoqish(self):
        print("Yoqildi")


class Noutbuk(Kompyuter):
    def yoqish(self):
        print("Noutbuk ishga tushdi")



k1 = Kompyuter("PC")
k2 = Noutbuk("HP")

k1.yoqish()
k2.yoqish()
