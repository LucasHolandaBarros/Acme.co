import os
from datetime import datetime, timedelta
import shutil

#Diretórios
FROM_DIR = "/home/valcann/backupsFrom"
LOG_DIR = "/home/valcann"
TO_DIR = "/home/valcann/backupsTo"

#Arquivos de log
LOG_FROM = os.path.join(LOG_DIR, "backupsFrom.log")
LOG_TO = os.path.join(LOG_DIR, "backupsTo.log")

#Limite é a data limite, no máximo 3 dias de duração das informações
limite = datetime.now() - timedelta(days=3)

#Função que retorna as informações dos arquivos
def get_arq_info(path):
    stat = os.stat(path)
    tamanho = stat.st_size
    criado = datetime.fromtimestamp(stat.st_birthtime).strftime("%Y-%m-%d %H:%M:%S") #Deixando os horários mais legíveis
    modificado = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    return f"Arquivo: {path} | Tamanho: {tamanho} bytes | Criação: {criado} | Modificação: {modificado}"

#Lista os arquivos presentes em uma pasta e passa para um log
def listar_arquivos(diretorio, log_file):
    with open(log_file, "w") as log:
        for arquivo in os.listdir(diretorio):
            caminho = os.path.join(diretorio, arquivo)
            if os.path.isfile(caminho):
                log.write(get_arq_info(caminho) + "\n")

#Função que remove os arquivos antigos, aqueles que tinham mais de 3 dias de vida
def remover_antigos(diretorio, limite):
    for arquivo in os.listdir(diretorio):
        caminho = os.path.join(diretorio, arquivo)
        if os.path.isfile(caminho):
            criado = datetime.fromtimestamp(os.stat(caminho).st_birthtime)
            if criado < limite:
                os.remove(caminho)

#Função que copia os arquivos que sobraram, ou seja, aqueles que possuiam menos de 3, ou 3, dias de vida
def copiar_recentes(origem, destino, limite):
    for arquivo in os.listdir(origem):
        caminho = os.path.join(origem, arquivo)
        if os.path.isfile(caminho):
            criado = datetime.fromtimestamp(os.stat(caminho).st_birthtime)
            if criado >= limite:
                shutil.copy2(caminho, destino)

if __name__ == "__main__":

    if not os.path.exists(FROM_DIR):
        raise SystemExit(f"Pasta de origem não encontrada: {FROM_DIR}")
    
    #1. Log inicial, com as informações de todos os arquivos localizados em: /home/valcann/backupsFrom
    listar_arquivos(FROM_DIR, LOG_FROM)

    #2. Removendo todos os arquivos antigos, aqueles que tinham mais de 3 dias de vida
    remover_antigos(FROM_DIR, limite)

    #3. Copiando os arquivos que sobraram, aqueles que possuem menos ou exatamente 3 dias de vida
    copiar_recentes(FROM_DIR, TO_DIR, limite)

    #4. Log final, com os arquivos que só possuem até, ou exatamente 3 dias de vida 
    listar_arquivos(TO_DIR, LOG_TO)

    print("Backup concluído com sucesso!")