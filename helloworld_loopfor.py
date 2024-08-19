cadena1 = 'Hello World'
cadena2 = ' abcdefhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYXZ'
cadena3 = ''
for i in cadena1:
    for ii in cadena2:
        if ii == i:
            cadena3 = cadena3 + ii
            print(cadena3)
            break
        else: print(cadena3 + ii)

# print(cadena1[0])
# print(cadena1[1])
# for i in range(11):
#     print(i,cadena1[i])


# numeros=[1,4,7,2,6,8,5,2,4,7,8765,2]

# for i in range(len(numeros)):
#     print(i,numeros[i])

# print("\n\n")
# for i in numeros:
#     print(i)
