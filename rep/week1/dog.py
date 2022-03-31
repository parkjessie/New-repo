class dog:

    # class attribute
    species = "dog"

    # instance attribute
    def __init__(self, name, age, breed):
        self.name = name
        self.breed = breed
        self.age = age

      
    
      

if __name__ == "__main__":
    sparky = dog("sparky", 3 , "golden doodle")
    print(sparky.name)
    print(sparky.breed)
    print(sparky.age)