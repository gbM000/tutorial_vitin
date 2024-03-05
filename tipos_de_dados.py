#dados simples
a = 10 #int
print(f"valor da variavel {a} tipo {type(a)}")
a = "palavra" # string [str]
print(f"valor da variavel {a} tipo {type(a)}")
a = 1.1 # float 
print(f"valor da variavel {a} tipo {type(a)}")
a = True # boolean [bool]
print(f"valor da variavel {a} tipo {type(a)}")

#coleções
a = [10, "blabla", 1.5,[5,2],True] # lista [list] (coleção mutável)
print(type(a))

## para percorrer coleções use o for()

for i in a:
  print(f"valor: {i}")

a = (10,"texto", 10, 5.5, False) # tuplas [tuple] (coleção imutável)
print(type(a))
for i in a:
  print(f"valor: {i}")

a = {"aa","ee","ii","oo","uu",10} # conjunto [set] (coleção mutável)
print(type(a))
for i in a:
  print(i)

a = {
  "nome": "joao",
  "idade": 20,
  "matriculado": True,
  "notas": [9.8,8.5,6.7,8.8]
}

print(type(a))
for i in a:
  print(f"{i}: {a[i]}")