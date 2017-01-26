import pyperclip, re

#Expressao regular para encontrar o padrao do numero de telefone

telefone = re.compile(r'''(
    (\d{2,3}|\(\d{2,3}\))?              #codigo de area
    (\s|-|\.)?                          #primeiro separador 
    (\d{4,5})                           #primeiro conjunto de numeros
    (\s|-|\.)?                          #segundo separador
    (\d{4})                             #segundo conjunto de numeros
    )''', re.VERBOSE)


#Expressao regular para encontrar os padrao do Email

Email = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                   #Nome do usuario Ex Nome_do-usuario
    @                                   #simbolo de @
    ([a-zA-Z0-9.-]+)?                   #Dominio Ex hotmail
    (\.[a-zA-Z]{2,4})                   #Dominio de trabalho Ex .com .org
    )''', re.VERBOSE)

#armazenando os padroes encontrados de numero em Numero
#e de emails em Endereco

text = str(pyperclip.paste())          
Endereco = []
for groups in telefone.findall(text):
    Numero = '-'.join([groups[1], groups[3], groups[5]])
    Endereco.append(Numero)
for groups in Email.findall(text):
    Endereco.append(groups[0])
    
#copiando os resultados para area de transferencia

if len(Endereco) > 0:
    pyperclip.copy('\n'.join(Endereco))
    print('copiado para area de transferencia')
    print('\n'.join(Endereco))
else:
    print('Numero de telefone ou endereco de Email nao encontrados')
    
