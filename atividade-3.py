nota1 = float(input("Nota do aluno: "))
nota2 = float(input("Nota do aluno: "))
nota3 = float(input("Nota do aluno: "))
nota4 = float(input("Nota do aluno: "))

lista = [nota1, nota2, nota3, nota4]
print(lista)

mean= sum(lista) / len(lista)
print (mean)