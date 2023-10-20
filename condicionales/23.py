import os 
os.system("cls")

matematicas = int (input("matematicas :"))
fisica = int(input("fisca : "))

propina = matematicas + fisica /2
if propina > 17 : propina += 2* matematicas
if fisica  > 15 : propina += fisica *1.5

promedio = ( matematicas + fisica ) / 2
print( f"promedio = {promedio : .2f}")
print( f"propina  = {promedio : .2f}")
print( f"reloj    = {'si'if promedio > 16 else 'no' }")
