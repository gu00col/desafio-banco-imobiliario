<div id='cabeçalho'/>  

<div align=center>
    <a><img width="450" alt="Logo" src="https://user-images.githubusercontent.com/60848932/147513743-1e2b1540-e149-409b-b5e5-476141f109e9.png"></a>

# PYTHONDX - Jogo Imobiliário

</div><br>


## 📚 Índice
 1. [Sobre o Projeto](#projeto)
 2. [Tecnologias Utilizadas](#tecnologias)
 3. [Pré-requisitos](#requisitos)
 6. [Autor](#autor)


<div id='projeto'/>  

<br>

## 💻 Sobre o Projeto

Foi desenvolvido um Jogo Imobiliario em Python 3.9 <br>
As informações do desafio estão no arquivo: *DESAFIO_PYTHONDX.pdf*

*Tarefas executadas:*
- [x] Criar o handler do Flask
- [x] Template para a primeira tela
- [ ] Módulo de conexão com o BD
- [ ] Requirements para instalação do projeto para devs
- [ ] Cookie management
- [ ] Template para a resposta da query para análise
- [ ] Template para a resposta do envio da ação principal
- [ ] Módulo para gerenciar o request e response

*Tarefas Pendentes:*
- [ ] Criar o handler do Flask
- [ ] Template para a primeira tela

<div id='tecnologias'/>

<br>

## 🛠 Tecnologias Utilizadas

As seguintes ferramentas foram utilizadas na construção do projeto:

&rarr; <a href="https://www.python.org/"> Python </a> - Linguagem de Programação <br>
&rarr; <a href="https://www.sqlalchemy.org/"> SQLAlchemy </a> - Banco de Dados  <br>

<div id='requisitos'/>

<br>


## 🚀 Pré-requisitos

* Ter o [Java](https://www.oracle.com/br/java/technologies/javase-jdk11-downloads.html) instalado (JDK e JRE).
* Ter o [Maven](https://maven.apache.org/) instaldo.

<br>

## 🚀 Dependências do projeto

- <a href="https://spring.io/projects/spring-data-jpa#overview">Spring Data JPA</a><br>
- <a href="https://spring.io/projects/spring-ws">Spring Web</a><br>
- <a href="https://spring.io/projects/spring-boot">Spring Boot DevTools</a><br>
- <a href="https://spring.io/guides/gs/accessing-data-mysql/">MySQL Driver </a><br>
- <a href="https://spring.io/guides/gs/accessing-data-jpa/">H2database</a><br>
- <a href="https://projectlombok.org/setup/maven">Lombok </a><br>

<br>

## 🚀 Compilando e rodando o projeto

- *Faça uma copia do projeto para sua maquina*

Clone o repositório:
```bash
$ git clone https://github.com/caamilacgs/DaraSquad
```
Entre dentro da pasta:
```bash
$ cd DaraSquad
```

- *Execute o projeto:*

Acesse o projeto por uma IDE de sua preferência: INTELIJ, ECLIPSE, VSCODE etc.
Consulte o arquivo aplication.properties para definir as configurações de acesso local ao banco.
    - <a href="https://github.com/caamilacgs/DaraSquad/blob/camila/conexao/h2.md"> Procedimento de como configurar o banco H2 </a>
    - <a href="https://github.com/caamilacgs/DaraSquad/blob/camila/conexao/mysql.md"> Procedimento de como configurar o banco MYSQL </a>
    
Para compilar o projeto vá até a pasta onde se encontra o arquivo `pom.xml` e execute no terminal o comando: `mvn clean install`

Se o resultado do build for `BUILD SUCCESS`, rode o projeto usando: `mvn exec:java`

Logo após, abra o seu navegador e acesse a pagina inicial: `http://localhost:8080/`

<br>

## 🚀 Teste da API

Pode ser feito pelo swagger: <a href="http://localhost:8080/swagger-ui.html">http://localhost:8080/swagger-ui.html</a><br>

Ou importanto a collecion no Postman: <a href="https://www.getpostman.com/collections/505906448da72bda396c">https://www.getpostman.com/collections/505906448da72bda396c</a>

<br>

## 🤝 Autor

<table>
    <td align="center"><br/>
        <a href="https://github.com/amandagsa">
            <img src="https://user-images.githubusercontent.com/60848932/147514081-d692f757-77ab-42d4-82be-1e521ed5522f.png" width="105px;"
                alt="Luis Gustavo Barbosa de Oliveira" /><br><sub><b>Luis Gustavo Barbosa de Oliveira</b></sub><br></a><br/>
        <p align="center">
            <a href="https://github.com/gu00col">
                <img src="https://user-images.githubusercontent.com/60848932/117540779-2bad0e80-afe7-11eb-8391-2b6661a3efc3.png"
                    width="30px" alt="GitHub" />
            </a>
            <a href="https://www.linkedin.com/in/luis-g-b-oliveira/">
                <img src="https://user-images.githubusercontent.com/60848932/117540778-29e34b00-afe7-11eb-8a68-5916e9822145.png"
                    width="30px" alt="Linkedin" />
            </a>
            <a href="mailto:gu00col@gmail.com">
                <img src="https://user-images.githubusercontent.com/60848932/117541013-3ddb7c80-afe8-11eb-83c2-79827e99ec59.png"
                    width="30px" alt="Email" />
            </a>
        </p>
    </td>
</table>
<div id='autor'/>

<br>


[⬆ Voltar ao topo](#cabeçalho)<br>