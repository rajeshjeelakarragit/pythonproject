class Cloth:
   pass

# class method
@classmethod
def brandName(cls):
   print("Name of the brand is Raymond")

# adding dynamically
setattr(Cloth, "brand_name", brandName)
newObj = Cloth()
newObj.brand_name()

# deleting dynamically
del Cloth.brandName