## Desafio #1 - Banco de Pessoas

Uma pesquisa foi realizada para coletar alguns dados sobre um grupo de pessoas. Os dados que sabemos sobre cada pessoa
que compõe este grupo são: **nome**, **idade**, **sexo**, **estado civil**, **área de atuação profissional**, **salário**
e se esta possui ou não **dependentes**.

Essas informações foram estruturadas em um **dicionário** que, em nosso cenário, funcionará como um "banco de dados"
sobre o qual podemos "armazenar" os dados desta pesquisa e também extrair algumas informações a partir disto.

A variável `pessoas` irá funcionar como a fonte de acesso a esses dados. O exemplo abaixo mostra uma parte da estrutura
atributa à variável que usaremos como "banco de dados".

````python
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
    }
]
````

### Sabendo disso, desenvolva uma aplicação em Python que seja capaz de:

1. Listar o número de pessoas existentes (sem considerar os dependentes)
2. Listar o número de pessoas existentes (considerando os dependentes)
3. Exibir o número de pessoas do sexo feminino (sem considerar os dependentes)
4. Exibir o número de pessoas do sexo feminino (considerando os dependentes que também sejam do sexo feminino)
5. Calcular a média salarial do Banco de Pessoas, considerando apenas duas casas decimais
6. Listar os nomes das pessoas que trabalham na área de Saúde
7. Listar os nomes das pessoas que são maiores de idade
8. Listar o número de pessoas desempregadas

Cada uma dessas opções devem ser dispostas em um menu para que o usuário selecione qual operação ele deseja realizar.
Portanto, será necessário criar um menu. O programa deverá ser encerrado apenas quando o usuário digitar a opção ``0``
(zero).
