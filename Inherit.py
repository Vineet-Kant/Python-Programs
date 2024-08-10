class Mobile:
    def camera(self,c1,c2):
        self.rearcamera = c1
        self.front_camera= c2
        return self
    def color(self,c2):
        print("Color",c2)

class Asus(Mobile):
    def screenlength(self,s1):
        print(" Inches",s1)
    def noofsidebutton(self,s2):
        print("No.",s2)
    def torch(self,s3):
        print("Yes/No",s3)

a1=Mobile()
d2 = a1.camera("8","2")
print(d2.rearcamera, d2.front_camera )  # Rear Camera: 8MP and Front Camera: 2MP
print(a1.color("Black"))
b1=Asus()
print(b1.screenlength("6"))
print(b1.noofsidebutton("3"))
print(b1.torch("Yes"))
# print(b1.camera("8"))
