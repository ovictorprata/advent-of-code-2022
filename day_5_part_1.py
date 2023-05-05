input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

piles_number = None
commands_treated = []
commands = []

input = input.split('\n')

for key, value in enumerate(input):
    if value.find('1') != -1:
        piles_number = key
        break

commands = input[(piles_number+2):]
piles_number = 

for i in commands:
    i = i.strip().split(' ')
    move = int(i[1])
    initial = int(i[3])
    end = int(i[5])
    commands_treated.append([move, initial, end])
print(commands_treated)


# for i in input:
#     lista_letras_1 = [s for s in string_1[1:-1].split() for s in s]
#     print(lista_letras_1)  # Output: ['Z', 'M', 'P']