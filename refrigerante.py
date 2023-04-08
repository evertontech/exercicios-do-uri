e, f, c = input().split()


e = int(e)
f = int(f)
c = int(c)

garrafas_trocadas = e + f

refrigerante = 0

while garrafas_trocadas >= c:
    refrigerante = refrigerante + 1 
    garrafas_trocadas = garrafas_trocadas - c
    garrafas_trocadas = garrafas_trocadas + 1
    

print(refrigerante)