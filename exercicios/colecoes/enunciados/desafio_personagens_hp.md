## Desafio #2 - Hogwarts precisa de você!

Existe uma lista de personagens da saga, porém, o diretor de Hogwarts notou que os nomes das pessoas estão misturados .
Assim, dificulta a identificação de alunos a partir dos nomes de suas Casas, sexo, idade, etc.

Além disso, há um problema muito sério: nesta lista estão bruxos e trouxas, juntos. Porém, Hogwarts não poderá ensinar
magias para aquelas que não são capazes de conjurá-las.

Por sorte, alguns professores da escola souberam que você também é uma espécie de bruxa(o), afinal, sabe programar e
isso é um tipo de magia poderosa! Sendo assim, você será responsável por criar alguns filtros que venham a auxiliar a
escola de magia nesta missão.

As informações dos personagens foram atribuídas à variável `personagens` e as magias, por sua vez, à variável `magias`.
Abaixo seguem uma parte dos dados que cada uma dessas variáveis guardam, respectivamente:

### Lista de personagens

````python
personagens = [
    {
        "name": "Harry Potter",
        "alternate_names": [

        ],
        "species": "human",
        "gender": "male",
        "house": "Gryffindor",
        "dateOfBirth": "31-07-1980",
        "yearOfBirth": 1980,
        "wizard": True,
        "ancestry": "half-blood",
        "eyeColour": "green",
        "hairColour": "black",
        "wand": {
            "wood": "holly",
            "core": "phoenix feather",
            "length": 11
        },
        "patronus": "stag",
        "hogwartsStudent": True,
        "hogwartsStaff": False,
        "actor": "Daniel Radcliffe",
        "alternate_actors": [

        ],
        "alive": True,
        "image": "https://hp-api.herokuapp.com/images/harry.jpg"
    }
]
````

### Lista de magias

````python
magias = [
    {
        "name": "Aberto",
        "description": "Opens locked doors"
    }
]
````

Os nomes dos atributos estão em inglês, mas Dumbledore te forneceu um grimório que pode auxiliar: Google Tradutor.

---

## Dada essas informações, desenvolva uma aplicação em Python que seja capaz de:

1. Listar os nomes de todos personagens que pertençam a uma determinada casa (ex.: Hufflepuff)
2. Crie uma lista que contenha apenas os personagens que são bruxos (wizard = True) e, em seguida, liste seus nomes
3. Crie uma lista que contenha apenas os personagens que são trouxas (wizard = False) e, em seguida, liste seus nomes
4. Dado o nome de um(a) personagem que seja bruxo(a), faça com que ele(a) possa aprender uma das magias possíveis
   (utilize a coleção contida na variável `magias` para encontrar a magia em que deseja ensinar)

### Importante:

Cada uma dessas opções devem ser dispostas em um menu para que seja possível selecionar qual operação deve ser
realizada. Ou seja, o programa deve receber uma entrada do teclado para realizar a opção escolhida, exibir o resultado
e, em seguida, exibir novamente o menu. Esses passos deverá se repetir até a pessoa usuária digite a opção ``0``
(zero) para que o programa seja encerrado.

> **Obs.: Utilize funções para deixar seu código mais organizado e com menos repetições.**

### Informações adicionais:

Lista de personagens e magias obtidas aqui: 
