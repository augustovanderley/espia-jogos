# Busca Jogos Colecoes de Amigos 

Este projeto visa mostrar quais são os seus amigos que possuem um determinado jogo. O projeto usa a coleção da ludopedia dos seus amigos para realizar essa busca. 

## Getting Started

Primeiro, você deve duplicar o arquivo `env.example`, criando um arquivo chamado `.env` e adicionando a variável de ambiente com o valor do `access_token` da ludopedia. Caso não tenha token, siga as instruções da [documentação da API](https://ludopedia.com.br/api/documentacao.html#section/Aplicativo), criando o seu próprio aplicativo. 


## Como rodar o projeto

Para executar o projeto, você precisa ter python 3.12 e poetry instalado, que pode ser instalado com:

```bash
foo@bar:~$ pip install poetry
```

Depois, para rodar o projeto, você pode rodar usando:

```bash
foo@bar:~$ make jogos JOGO="azul"
```

ou

```bash
foo@bar:~$ make amigos AMIGO="felinto"
```

### Cadastrando amigos

Para cadastrar novos amigos, você precisa criar um arquivo `meus_amigos.json` na raiz do projeto, seguindo o seguinte padrão:

```json
[
    {
       "id_usuario":"104391",
       "usuario":"AugustVanderley",
       "nome_legivel":"Augusto Vanderley",
       "thumb": "https://ludopedia.com.br/uploads/avatar/avatar_104391_sm_1573572022.jpg"
    }
]
```

Para conseguir descobrir o id do usuário, é necessário rodar o seguinte comando, colocando o nome exato dos usuários:

```bash
foo@bar:~$ espia usuario AugustVanderley
{
    "id": 104391,
    "usuario": "AugustVanderley",
    "nome_legivel": "INSIRA NOME LEGIVEL"
}
```

Copie e cole o trecho acima no arquivo `meus_amigos.json` para adicionar o usuário na sua base de dados.

### Buscando jogos na coleção de amigos

Uma vez com a lib instalada, para realizar a busca de amigos que possuem um jogo, execute a seguinte chamada, aqui com exemplo do jogo "Food Chain Magnate":

```bash
foo@bar:~$ espia jogos "food chain magnate"
```

O resultado mostrará as pessoas que possuem aquele jogo, assim como a nota que eles deram ao jogo. 