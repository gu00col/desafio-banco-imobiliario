# Desafio PYTHON
## Simulação de Banco Imobiliário


### Ideia: 
Considere o seguinte jogo hipotético muito semelhante a Banco Imobiliário, onde várias de suas mecânicas
foram simplificadas. Numa partida desse jogo, os jogadores se alteram em rodadas, numa ordem definida
aleatoriamente no começo da partida. Os jogadores sempre começam uma partida com saldo de 300 para
cada um.

Nesse jogo, o tabuleiro é composto por 20 propriedades em sequência. Cada propriedade tem um custo de
venda, um valor de aluguel, um proprietário caso já estejam compradas, e seguem uma determinada ordem no
tabuleiro. Não é possível construir hotéis e nenhuma outra melhoria sobre as propriedades do tabuleiro, por
simplicidade do problema.

No começo da sua vez, o jogador joga um dado equiprovável de 6 faces que determina quantas espaços no
tabuleiro o jogador vai andar.

- Ao cair em uma propriedade sem proprietário, o jogador pode escolher entre comprar ou não a
propriedade. Esse é a única forma pela qual uma propriedade pode ser comprada.
- Ao cair em uma propriedade que tem proprietário, ele deve pagar ao proprietário o valor do aluguel da
propriedade.
- Ao completar uma volta no tabuleiro, o jogador ganha 100 de saldo.

Jogadores só podem comprar propriedades caso ela não tenha dono e o jogador tenha o dinheiro da venda.
Ao comprar uma propriedade, o jogador perde o dinheiro e ganha a posse da propriedade.

Cada um dos jogadores tem uma implementação de comportamento diferente, que dita as ações que eles
vão tomar ao longo do jogo. Mais detalhes sobre o comportamento serão explicados mais à frente.

Um jogador que fica com saldo negativo perde o jogo, e não joga mais. Perde suas propriedades e portanto
podem ser compradas por qualquer outro jogador.

Termina quando restar somente um jogador com saldo positivo, a qualquer momento da partida. Esse jogador
é declarado o vencedor.

Desejamos rodar uma simulação para decidir qual a melhor estratégia. Para isso, idealizamos uma partida
com 4 diferentes tipos de possíveis jogadores. Os comportamentos definidos são:

- O jogador um é impulsivo;
- O jogador dois é exigente;
- O jogador três é cauteloso;
- O jogador quatro é aleatório;

O jogador impulsivo compra qualquer propriedade sobre a qual ele parar.

O jogador exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.

O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando
depois de realizada a compra.

O jogador aleatório compra a propriedade que ele parar em cima com probabilidade de 50%.

Caso o jogo demore muito, como é de costume em jogos dessa natureza, o jogo termina na milésima rodada
com a vitória do jogador com mais saldo. O critério de desempate é a ordem de turno dos jogadores nesta
partida.

**Saída**

Uma execução do programa proposto deve rodar 300 simulações, imprimindo no console os dados referentes
às execuções. Esperamos encontrar nos dados as seguintes informações:

- Quantas partidas terminam por time out (1000 rodadas);
- Quantos turnos em média demora uma partida;
- Qual a porcentagem de vitórias por comportamento dos jogadores;
- Qual o comportamento que mais vence.
## Stack utilizada

**Back-end:** Python, sqlite


## Instalação

**Tecnologia usada:** Python 3.8.5

Para que a simumação funcione você deve ter o python instalado

Apôs a isntalação do python as dependencias devem ser instaladas utilizando o arquivo requirements.txt

- Acesse a pasta do projeto e execute o comando abaixo:

```bash
  pip install -r requirements.txt
```

## Rodando os testes

Para rodar os testes, rode o seguinte comando

Dentro da pasta do desafio execute o comando:

```bash
  python main.py
```

### Ao executar a mensagem abaixo será exibida, e você deve escolher se quer ou não as mensagens do jogo

``` Antes de iniciar o teste você gostaria de ver todas as mensagens do teste? ex player 1 está na casa x e comprou a casa x? se sim digite 1 se não digite 2 ```

Caso escolha exibir as mensagens será exibido os textos como o exemplo abaixo:

```bash
Rodada 135

Jogador jogando 1
Caixa: 662.0
Perfil: impulsivo

Posição atual: ipanema
Preço de compra: 110.0
Aluguel: 55.0
Proprietario: 2

--Tirou 4 no dado!
Completou uma volta e recebeu 100 seu saldo anterior era 662.0 seu novo saldo é 762.0
Se move até a casa: 4!

Posição atual: barra da tijuca
Preço de compra: 50.0
Aluguel: 25.0
Proprietario: None
O jogador comprou a propriedade barra da tijuca por 50.0 sobrando em caixa 712.0
```

## O jogo demora em media 10 minutos para ser concluido e no final um resultado como esse será exibido:

```bash
----- Resultados ----
De 300 rodadas 175 partidas terminaram por timeout!
A media de rodadas por partida é de 641.7066666666667
A porcentagem de vitorias por perfil é:
 - 12% de vitorias para o perfil aleatorio
 - 28% de vitorias para o perfil cauteloso
 - 25% de vitorias para o perfil exigente
 - 35% de vitorias para o perfil impulsivo
O perfil que mais vence é o impulsivo
```
## 🚀 Sobre mim
Sou programador python a 2 anos voltado para a area de desenvolvimento web buscando me aprofundar na linguagem e aprender cada vez mais.


### Linkedin: https://www.linkedin.com/in/luis-g-b-oliveira/