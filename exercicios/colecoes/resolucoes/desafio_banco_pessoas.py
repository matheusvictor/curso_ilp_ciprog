pessoas = [
    {
        "nome": "João das Neves",
        "idade": 33,
        "sexo": "M",
        "estado_civil": "Casado",
        "área": "Saúde",
        "profissão": "Médico",
        "salário": 7000,
        "dependentes": [
            {
                "nome": "Alice das Neves",
                "sexo": "F",
                "idade": 12,
                "parentesco": "Filha"
            }
        ]
    },
    {
        "nome": "Ana Müller",
        "idade": 20,
        "sexo": "F",
        "estado_civil": "Solteira",
        "área": "Tecnologia",
        "profissão": "Estagiária",
        "salário": 1500,
        "dependentes": []
    },
    {
        "nome": 'Joanna D\'Arc',
        "idade": 30,
        "sexo": "F",
        "estado_civil": "Casada",
        "área": "Direito",
        "profissão": "Advogada",
        "salário": 3200,
        "dependentes": []
    },
    {
        "nome": "Adelino da Silva",
        "idade": 47,
        "sexo": "M",
        "estado_civil": "Divorciado",
        "área": "Empreendimento",
        "profissão": "Vendedor",
        "salário": 800,
        "dependentes": []
    },
    {
        "nome": "Roberto Luiz",
        "idade": 28,
        "sexo": "M",
        "estado_civil": "Solteiro",
        "área": "Educação",
        "profissão": "Professor",
        "salário": 1600,
        "dependentes": []
    },
    {
        "nome": "Marcos Antonio",
        "idade": 31,
        "sexo": "M",
        "estado_civil": "Casado",
        "área": "Educação",
        "profissão": "Professor",
        "salário": 1600,
        "dependentes": [
            {
                "nome": "Sergio",
                "sexo": "M",
                "idade": 5,
                "parentesco": "Filho"
            }
        ]
    },
    {
        "nome": "Luisa Vieira",
        "idade": 41,
        "sexo": "F",
        "estado_civil": "Solteira",
        "área": "Ciências",
        "profissão": "Engenheira Química",
        "salário": 3500,
        "dependentes": [
            {
                "nome": "Beatriz Vieira",
                "sexo": "F",
                "idade": 20,
                "parentesco": "Filha"
            },
            {
                "nome": "Lucas",
                "sexo": "M",
                "idade": 17,
                "parentesco": "Filho"
            }
        ]
    },
    {
        "nome": "Amanda Cerqueira",
        "idade": 35,
        "sexo": "F",
        "estado_civil": "Solteira",
        "área": "Tecnologia",
        "profissão": "Desenvolvedora",
        "salário": 3500,
        "dependentes": []
    },
    {
        "nome": "Carlos Alberto",
        "idade": 22,
        "sexo": "M",
        "estado_civil": "Solteiro",
        "área": "Tecnologia",
        "profissão": "Desenvolvedor",
        "salário": 3500,
        "dependentes": []
    },
    {
        "nome": "Silvana Andrade",
        "idade": 28,
        "sexo": "F",
        "estado_civil": "Casada",
        "área": "Saúde",
        "profissão": "Médica",
        "salário": 5000,
        "dependentes": []
    },
    {
        "nome": "Pamela Amorim",
        "idade": 25,
        "sexo": "F",
        "estado_civil": "Solteira",
        "área": "Saúde",
        "profissão": "Pediatra",
        "salário": 1800,
        "dependentes": []
    },
    {
        "nome": "Pamela Amorim",
        "idade": 25,
        "sexo": "F",
        "estado_civil": "Solteira",
        "área": "Saúde",
        "profissão": "Pediatra",
        "salário": 1800,
        "dependentes": []
    },
    {
        "nome": "Paulo Roberto",
        "idade": 32,
        "sexo": "M",
        "estado_civil": "Divorciado",
        "área": "Direito",
        "profissão": "Advogado",
        "salário": 2800,
        "dependentes": []
    },
    {
        "nome": "Juliana Camarim",
        "idade": 17,
        "sexo": "F",
        "estado_civil": "Solteira",
        "área": "Saúde",
        "profissão": "Estagiária",
        "salário": 800,
        "dependentes": []
    },
    {
        "nome": "Carlos",
        "idade": 25,
        "sexo": "M",
        "estado_civil": "Solteiro",
        "área": None,
        "profissão": None,
        "salário": 0,
        "dependentes": []
    }
]

# 1. Listar o número de pessoas existentes (sem considerar os dependentes)
numero_profissionais = len(pessoas)
print(f'Sem considerar as pessoas dependentes, existe(m) {numero_profissionais} pessoa(s) registradas.')

# 2. Listar o número de pessoas existentes (considerando os dependentes)
numero_total_pessoas = len(pessoas)
for pessoa in pessoas:
    if pessoa['dependentes']:
        numero_total_pessoas += len(pessoa['dependentes'])

print(f'Considerando as pessoas dependentes, existe(m) {numero_total_pessoas} pessoa(s) registradas.')

# 3. Exibir o número de pessoas do sexo feminino (sem considerar os dependentes)
numero_pessoas_sexo_feminino = 0
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        numero_pessoas_sexo_feminino += 1

print(f'Existe(m) {numero_pessoas_sexo_feminino} pessoa(s) do sexo feminino.')

# 4. Exibir o número de pessoas do sexo feminino (considerando os dependentes que também sejam do sexo feminino)
numero_total_pessoas_sexo_feminino = numero_pessoas_sexo_feminino
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        for dependente in pessoa['dependentes']:
            if dependente['sexo'] == 'F':
                numero_total_pessoas_sexo_feminino += 1

print(f'Existe(m) {numero_pessoas_sexo_feminino} pessoa(s) do sexo feminino, considerando também os dependentes.')

# 5. Calcular a média salarial do Banco de Pessoas, considerando apenas duas casas decimais
soma_total_salario = 0
for pessoa in pessoas:
    soma_total_salario += pessoa['salário']
media_salarial = soma_total_salario / numero_profissionais
print(soma_total_salario)
print(f'Média salarial: R$ {media_salarial:.2f}')

# 6. Listar os nomes das pessoas que trabalham na área de Saúde
pessoas_area_saude = set()
for pessoa in pessoas:
    if pessoa['área'] == 'Saúde':
        pessoas_area_saude.add(pessoa['nome'])
print(f'Nomes das pessoas que atuam na área de Saúde: {pessoas_area_saude}')

# 7. Listar os nomes das pessoas que são maiores de idade
nomes_maiores_idade = set()
for pessoa in pessoas:
    if pessoa['idade'] >= 18:
        nomes_maiores_idade.add(pessoa['nome'])
print(f'Nomes das pessoas que são maiores de idade: {nomes_maiores_idade}')

# 8. Listar o número de pessoas desempregadas
qtd_pessoas_desempregadas = 0
for pessoa in pessoas:
    if pessoa['profissão'] is None or pessoa['área'] is None or pessoa['salário'] == 0:
        qtd_pessoas_desempregadas += 1
print(f'Existe(m) {qtd_pessoas_desempregadas} pessoas desempregadas!')
