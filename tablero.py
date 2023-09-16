class Tablero:
    def __init__(self,Nombre,Gmail,Email,User,Password,Billetera):
        self.Nombre = Nombre
        self.Gmail = Gmail
        self.Email = Email
        self.User = User
        self.Password = Password
        self.Billetera = Billetera
        
    def construi(self):
        print("construyendo...");
    def destrui(self):
        print("destruyendo...");
        
 ####lista de tableros       
star = Tablero("Simcity","larutina@gmail.com","Alumnos@Palermo.ar","simcity345",345,500);
star1 = Tablero("Simcity1","larutina1@gmail.com","Alumnos1@Palermo.ar","simcity3451",3451,5001); 
star2 = Tablero("Simcity2","larutina2@gmail.com","Alumnos2@Palermo.ar","simcity3452",3451,5001) ;     
      
print("================================");
print("\n");      
print(type(star));
star.destrui();
star1.destrui(); 
print("\n");
print("===============  NOMBRE =================");

print(star.Nombre);
print("===============  GMAIL =================");        
print(star.Gmail);
print("===============  EMAIL =================");        
print(star.Email);
print("===============  CONTRASEÑA =================");
print(star.Password);
print("===============  BILLETERA =================");        
print(star.Billetera);
print("===============  USER =================");
print(star.User);
