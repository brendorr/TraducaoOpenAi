# WOTRptbr
Resumo: Projeto de traducao utilizando ChatGPT

Motivação: entedimento da histório do jogo Pathfinder: Wrath of the Righteous [https://store.steampowered.com/app/1184370/Pathfinder_Wrath_of_the_Righteous__Enhanced_Edition/] a partir de legendas em nossa lingua nativa

O que é
A ideia do projeto é utilizar a API do ChatGPT disponibilizada pela OpenAI, considerando os limites de acesso do usuário, para traduzir os textos e falas do jogo, que estão em inglês, para Português-BR.
O algoritmo que executa esta tarefa está escrito em Python e o arquivo dos textos do jogo foi obtido na ...
Foi levado em consideração as palavras chaves e estruturas específicas identificadas no arquivo de textos e devem e foram mantidas no arquivo de tradução
...

Stack
Foi utilizado Python na construção do algoritmo, a biblioteca Flask para acessar a API (como orientado pela documentação: https://platform.openai.com/docs/quickstart/build-your-application) e a biblioteca RegEx para dividir os textos.
