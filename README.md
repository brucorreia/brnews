# README - BRNews

## Descrição do Projeto

Este projeto consiste em um crawler desenvolvido para coletar as notícias dos maiores portais de notícias e enviá-las automaticamente para o canal Telegram [BR_News](https://t.me/brnewscrawler). O objetivo é fornecer uma maneira simples de se informar a partir dos maiores portais.

## Funcionalidades

- **Coleta de Notícias:** O crawler é capaz de acessar os maiores portais de notícias do Brasil para extrair informações relevantes.

- **Envio Automático para um Canal Telegram:** As notícias coletadas são enviadas automaticamente para o canal Telegram [BR News Crawler](https://t.me/brnewscrawler).

- **Atualização Regular:** O crawler é configurado para realizar atualizações regulares, garantindo que as notícias mais recentes estejam sempre disponíveis no canal.

## Como Usar

1. **Requisitos:**
   - Python 3.x
   - Bibliotecas Python listadas no arquivo `requirements.txt`

2. **Configuração do Ambiente:**
   - Instalação docker
   - Instalação docker-compose
   - Clone o repositório: `git clone https://github.com/brucorreia/brnews.git`
   - Acesse o diretório do projeto: `cd brnews`

3. **Configuração do Telegram:**
   - Crie um bot no Telegram usando o [BotFather](https://core.telegram.org/bots#botfather).
   - Obtenha o token do bot e adicione-o em um canal.

4. **Configuração do Crawler:**
   - Edite o arquivo `.env` e insira o token do seu bot Telegram.

5. **Execução:**
   - Execute o crawler: `docker-compose up`

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar pull requests com melhorias.

## Contato

Para mais informações ou dúvidas, entre em contato através do canal Telegram [BR News Crawler](https://t.me/brnewscrawler).

---

*Este projeto é desenvolvido e mantido por [Bruno Correia](https://github.com/brucorreia).*