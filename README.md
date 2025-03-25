# FTP Connection Tool

## Descrição 🧙‍♂️
Esta é uma ferramenta simples para testar conexões com servidores FTP. Ela se conecta a um servidor especificado, envia credenciais padrão (`USER ftp` e `PASS ftp`) e executa o comando `PWD` para obter o diretório atual.

## Funcionalidades 🔧
- Estabelece conexão com um servidor FTP.
- Envia credenciais padrão de login.
- Executa o comando `PWD` para listar o diretório atual.
- Exibe o banner de resposta do servidor.

## Requisitos ✅✅
- Python 3.x

## Instalação
Clone este repositório:
```bash
$ git clone https://github.com/seu-usuario/seu-repositorio.git
$ cd seu-repositorio
```

## Uso ⚠️
Execute o script informando o endereço IP do servidor FTP:
```bash
$ python3 ftp_tool.py <IP_DO_SERVIDOR>
```
Exemplo:
```bash
$ python3 ftp_tool.py 192.168.1.1
```

## Exemplo de Saída
```
Conectando ao servidor...
220 FTP Server ready.
Enviando USER...
331 User name okay, need password.
Enviando PASS...
230 Login successful.
Enviando comando PWD...
257 "/" is the current directory.
```

## Observação
Esta ferramenta é apenas para fins educacionais e de testes.


