# Testes em Python
Bem-vindo ao repositório Testes em Python!

## Sobre o projeto
Este repositório é dedicado a mostrar as melhores práticas e exemplos para escrever testes de integração, unitários em Python utilizando o framework unittest.

## Objetivo
Seja você um desenvolvedor experiente ou um iniciante, o objetivo deste guia é ajudar a entender a importância dos testes com alguns exercícios/exemplos de como implementá-los de forma eficaz em seus projetos.

## Índice
* Introdução

* Primeiros passos

* Técnicas avançadas de teste

* Melhores práticas

* Contribuindo

## Introdução
Testes são uma parte crucial do desenvolvimento de software. Eles garantem que seu código funcione como esperado e ajudam a prevenir bugs de chegarem à produção. Neste repositório, focamos no unittest, um módulo embutido no Python que fornece um framework robusto para escrever e executar testes.

## Primeiros passos
Para começar a usar o unittest, você precisará ter o Python instalado em sua máquina. Você pode verificar se o Python está instalado executando:

```
python --version
```

Se você não tiver o Python instalado em seu computador, pode baixá-lo no **[site oficial](https://www.python.org/downloads/)**.

Obs: A versão utilizada foi a 3.10, mas fique a vontade de utilizar a versão que mais se adequar e que preferir. Além disso, o framework unittest vem instalado juntamente com a linguagem Python

### Criação do ambiente virtual para desenvolvimento (Windows)
Durante este, foi-se criado um ambiente virtual, o que garante o desenvolvimento estável e consistente sem interferir em outros projetos ou no ambiente global. Para criá-lo e ativá-lo, execute os seguintes comandos:

```
python -m venv nome_ambiente
venv\Scripts\Activate
```

Já no Linux:

```
python3 -m venv venv
source venv/bin/activate
```

## Técnicas avançadas de teste
Uma vez que você esteja confortável com o básico, pode explorar técnicas mais avançadas, como:

• Mocking: Simular objetos e comportamentos para testes mais complexos;
• Test fixtures: Configurar e desmontar condições para seus testes;
• Testes parametrizados: Executar o mesmo teste com diferentes entradas.

## Melhores práticas
Aqui estão algumas melhores práticas a serem lembradas:

•  Escreva testes claros e concisos: Cada teste deve focar em uma única funcionalidade;
•  Use nomes descritivos: Os nomes dos métodos de teste devem descrever claramente o que estão testando;
•  Mantenha os testes independentes: Os testes não devem depender uns dos outros;
•  Execute testes frequentemente: Integre os testes em seu fluxo de trabalho de desenvolvimento.

## Contribuindo
Contribuições são sempre bem-vindas! Se você tiver ideias para melhorar este repositório, sinta-se à vontade para abrir uma issue ou enviar um pull request.



