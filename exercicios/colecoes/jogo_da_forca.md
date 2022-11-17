# Jogo da forca

O jogo da forca consiste em um jogo cujo objetivo principal do jogador é acertar a palavra proposta. A palavra a ser adivinhada é "mascarada" para que o(a) jogador(a) não tenha como saber de imediato de qual é a palavra que precisa adivinhar. Assim, o(a) jogador(a) passará a conhcer a palavra gradualmente, a medida que acerta as letras mediante a palpites.

A cada palpite incorreto, um boneco utilizado para representar o(a) jogador(a) tem uma parte do corpo do enforcada. Caso o(a) jogador(a) não adivinhe a palavra em um número X de tentativas, seu personagem é enforcado, indicando que o jogo terminou com uma derrota.

Sabendo disso, iremos utilizar a linguagem Python para criar uma versão do jogo da forca e, para isso, precisamos atender a alguns requisitos:

--------

### Requisitos

- O jogo deverá possuir um menu que será exibido no início do programa. Este menu deve conter as seguintes opções:

  ```
    [1] Jogar
    [2] Cadastrar palavra
    [0] Encerrar o programa
  ```
  
- Caso seja digitada uma opção que não seja uma das mostradas acima, o programa deverá avisar que foi inserida uma opção inválida e, então, exibir novamente o menu para solicitar uma nova entrada.
- O jogo deverá continuar até que o(a) jogador(a) vença ou seja derrotado(a). O(A) jogador(a) vencerá caso acerte todas as letras da palavra dentro do seu limite de palpites. Por outro lado, perderá caso ultrapasse o número de tentativas; tendo seu personagem enforcado.
- Como acontece no jogo original, a palavra a ser adivinhada precisa ser mascarada! Para isso, podemos usar, por exemplo, o símbolo `_` para substituir cada letra da palavra original. Exemplo: a palavra `banana` será exibida para o(a) jogador(a) como `_ _ _ _ _ _`.
- O número de tentativas que o(a) jogador(a) terá será equivalente ao tamanho da palavra a ser adivinhada. Por exemplo: a palavra `banana` possui 6 letras. Assim, o(a) jogador(a) terá no máximo 6 palpites a serem feitos. Caso não acerte a palavra completa dentro deste número de tentativas, deverá perder o jogo e seu personagem deverá ser enforcado - conforme já descrito acima.
- Caso o jogador acerte uma letra, o símbolo `_` deverá ser substituído pela letra original da palavra correspondente, na mesma posição. Tome novamente a palavra `banana` como exemplo: caso o jogador digite a letra `n` como palpite, a palavra passará a ser exibida como `_ _ n _ n _`.
- Se a palavra possuir letras repetidas, como no caso acima, basta que o usuário dê apenas um palpite correto sobre esta para que todas elas sejam reveladas. Exemplo: a palavra `banana` possui duas letras `n`. Portanto, o jogador não precisará palpitá-la duas vezes, mas apenas uma única vez para que ambas as letras `n` existentes na palavra sejam reveladas.

- Caso o jogador venca, deverá ser impresso a seguinte mensagem:

```
 PARABÉNS, VOCÊ GANHOU!
           ___________      
          '._==_==_=_.'     
          .-\\:      /-.    
         | (|:.     |) |   
          '-|:.     |-'     
           \\::.    /      
             '::. .'        
               ) (          
             _.' '._        
            '-------'       
```

Para isso, você poderá utilizar o modelo abaixo:

```python
    print("Parabéns, você ganhou!".upper())
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
```
- Caso o jogador perca, deverá ser impresso a seguinte mensagem:

```
    VOCÊ PERDEU!
    A palavra era PALAVRA
        _______________       
       /               \      
      /                 \     
    //                   \/\  
    \|   XXXX     XXXX   | /   
     |   XXXX     XXXX   |/     
     |   XXX       XXX   |      
     |                   |      
     \__      XXX      __/     
       |\     XXX     /|       
       | |           | |        
       | I I I I I I I |        
       |  I I I I I I  |        
       \_             _/       
         \_         _/         
           \_______/           
```


Para isso, você poderá utilizar o modelo abaixo:

```python
    print("Você perdeu!".upper())
    print(f"A palavra era {palavra_secreta.upper()}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
```

--------

## Dicas

- Para desenvolver o programa, busque criar **funções** para algumas rotinas do seu programa, assim você terá menos repetição de linhas de código e será mais fácil realizar correções futuras;
- É possível que você precise utilizar métodos para manipulação de strings, tais como `strip()`, `upper()`, etc.;
- Para que seja possível randomizar qual palavra o programa irá selecionar para que o(a) jogador(a) adivinhe, você precisará utilizar a função `randrange` da biblioteca `random`. Para importá-la no seu código, utilize a seguinte linha de comando no início do seu programa `from random import randrange`. Na próxima seção, você entenderá o porquê usaremos essa função;
- Caso você queira trabalhar com palavras que possuam acentos, é possível que você tenha problemas em algumas versões de interpretadores. Para isso, utilize em seu programa o seguinte importe: `import unidecode`. Você poderá fazer esse importe logo abaixo do importe da biblioteca `random`;

### Usabilidade da biblioteca random

- A biblioteca `random `-  para sortear um número inteiro que possa ser responsável pela aleatoriedade do jogo, assim, a cada execução, uma nova palavra poderá ser .., e a mesma será distinta da anterior
    

