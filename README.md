# Ponderada CLI
## Descrição
Esse repositório contém um projeto que se trata de uma Interface por Linha de Comando (CLI) para controle de um braço mecânico.

## Pré-requisitos
**Python 3 instalado**

## Guia de Instalação (Windows, através do terminal)
Na janela do terminal digite os seguintes comandos para cada dependência

**Ativar o venv**
```python -m venv venv```
```venv\Scripts\activate```
**Instalar as dependências necessárias**
- pydobot 
```pip install pydobot```
- inquirer
```pip install inquirer```
- yaspin
```pip install yaspin```
- typer
```pip install "typer[all]"```
- requirements.txt
```pip install -r requirements.txt```
```pip freeze > requirements.txt```
**Para executar a aplicação**
```python src/main.py```

## Funcionalidades
**Ligar:** Liga a sucção da ferramenta do robô.
**Home:** Move o robô para a posição inicial predefinida.
**Posição Atual:** Exibe a posição atual da ferramenta do robô.
**Mover:** Move a ferramenta do robô em um eixo específico por uma determinada distância.
**Desligar:** Desliga a sucção da ferramenta do robô.

## Vídeos de demonstração
Para visualizar na prática, assista esse [vídeo](). 
