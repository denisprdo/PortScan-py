## Resumo
Scanner de portas para efetuar pentest.

## Pré-requisitos
Antes de executar este programa, você precisará ter o Python 2.7 instalado em seu sistema. Você pode verificar se o Python 2.7 está instalado executando o seguinte comando no terminal:

```bash
python --version
```

## Permissões de Execução
Antes de executar o programa, é importante garantir que você tenha permissões de execução para o arquivo Python. Caso contrário, você pode encontrar um erro de "permissão negada" ao tentar executá-lo.

Para conceder permissões de execução, você pode usar o comando `chmod` no terminal. Navegue até o diretório onde o arquivo Python está localizado e execute o seguinte comando:

```bash
chmod +x PortScan-py
```

## Execução
Você pode executar o programa usando o seguinte comando:

```
./PortScan-py ip_address porta_inicial porta_final
```

Exemplo:
```
./PortScan-py 192.168.0.1 1 25
```
