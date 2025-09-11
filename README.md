# Backup Automático

Script em Python para automatizar backups locais.

## O que faz
- Lista arquivos da pasta de origem e salva em `backupsFrom.log`.
- Remove arquivos com mais de **3 dias**.
- Copia arquivos recentes (≤ 3 dias) para a pasta de destino.
- Gera `backupsTo.log` com os arquivos copiados.

## Requisitos
- Python 3.8 ou superior
- Permissões de leitura/escrita nas pastas definidas no script

## Como usar
1. Clone o repositório:
```bash
git clone https://github.com/LucasHolandaBarros/Acme.co
```
2. Crie as pastas se não existirem:
```bash
mkdir -p /home/valcann/backupsFrom
mkdir -p /home/valcann/backupsTo
```
3. Execute:
```bash
python3 backup.py
```

link para o repositório: https://github.com/LucasHolandaBarros/Acme.co
