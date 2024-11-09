import os
import sys
import random
import time

# Função para verificar os argumentos passados para o script
def check_args(file_args):
    """
    Verifica se os argumentos de entrada são válidos e imprime a utilização correta se não forem
    """
    try:
        # Verifica se o número de argumentos é diferente de 2 ou se o segundo argumento não é um número positivo
        if len(file_args) != 2 or int(file_args[1]) <= 0:
            raise Exception()
    except:
        # Imprime a utilização correta do script e sai
        print("Usage:  create_measurements.sh <positive integer number of records to create>")
        print("        You can use underscore notation for large number of records.")
        print("        For example:  1_000_000_000 for one billion")
        exit()

# Função para construir a lista de nomes de estações meteorológicas
def build_weather_station_name_list():
    """
    Obtém os nomes das estações meteorológicas a partir de um arquivo de exemplo e remove duplicatas
    """
    station_names = []
    # Abre o arquivo de estações meteorológicas
    with open('./data/weather_stations.csv', 'r', encoding="utf-8") as file:
        file_contents = file.read()
    # Processa cada linha do arquivo
    for station in file_contents.splitlines():
        if "#" in station:
            next
        else:
            # Adiciona o nome da estação à lista
            station_names.append(station.split(';')[0])
    # Remove duplicatas e retorna a lista
    return list(set(station_names))

# Função para converter bytes em um formato legível
def convert_bytes(num):
    """
    Converte bytes para um formato legível (e.g., KiB, MiB, GiB)
    """
    for x in ['bytes', 'KiB', 'MiB', 'GiB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

# Função para formatar o tempo decorrido em um formato legível
def format_elapsed_time(seconds):
    """
    Formata o tempo decorrido em um formato legível
    """
    if seconds < 60:
        return f"{seconds:.3f} seconds"
    elif seconds < 3600:
        minutes, seconds = divmod(seconds, 60)
        return f"{int(minutes)} minutes {int(seconds)} seconds"
    else:
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if minutes == 0:
            return f"{int(hours)} hours {int(seconds)} seconds"
        else:
            return f"{int(hours)} hours {int(minutes)} minutes {int(seconds)} seconds"

# Função para estimar o tamanho do arquivo de dados de teste
def estimate_file_size(weather_station_names, num_rows_to_create):
    """
    Tenta estimar o tamanho do arquivo de dados de teste
    """
    max_string = float('-inf')
    min_string = float('inf')
    per_record_size = 0
    record_size_unit = "bytes"

    # Calcula o tamanho máximo e mínimo dos nomes das estações
    for station in weather_station_names:
        if len(station) > max_string:
            max_string = len(station)
        if len(station) < min_string:
            min_string = len(station)
        per_record_size = ((max_string + min_string * 2) + len(",-123.4")) / 2

    # Calcula o tamanho total do arquivo
    total_file_size = num_rows_to_create * per_record_size
    human_file_size = convert_bytes(total_file_size)

    return f"O tamanho estimado do arquivo é:  {human_file_size}.\nO tamanho final será provavelmente muito menor (metade)."

# Função para gerar e escrever os dados de teste no arquivo
def build_test_data(weather_station_names, num_rows_to_create):
    """
    Gera e escreve no arquivo a quantidade solicitada de dados de teste
    """
    start_time = time.time()
    coldest_temp = -99.9
    hottest_temp = 99.9
    station_names_10k_max = random.choices(weather_station_names, k=10_000)
    batch_size = 10000 # Em vez de escrever linha por linha no arquivo, processa um lote de estações e grava no disco
    progress_step = max(1, (num_rows_to_create // batch_size) // 100)
    print('Criando o arquivo... isso vai demorar uns 10 minutos...')

    try:
        # Abre o arquivo para escrita
        with open("./data/measurements.txt", 'w', encoding="utf-8") as file:
            for s in range(0,num_rows_to_create // batch_size):
                # Gera um lote de dados de teste
                batch = random.choices(station_names_10k_max, k=batch_size)
                prepped_deviated_batch = '\n'.join([f"{station};{random.uniform(coldest_temp, hottest_temp):.1f}" for station in batch]) # :.1f deve ser mais rápido que round em grande escala, porque round utiliza operação matemática
                file.write(prepped_deviated_batch + '\n')
                
        sys.stdout.write('\n')
    except Exception as e:
        # Imprime a mensagem de erro e sai
        print("Something went wrong. Printing error info and exiting...")
        print(e)
        exit()
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    file_size = os.path.getsize("./data/measurements.txt")
    human_file_size = convert_bytes(file_size)
 
    print("Arquivo escrito com sucesso data/measurements.txt")
    print(f"Tamanho final:  {human_file_size}")
    print(f"Tempo decorrido: {format_elapsed_time(elapsed_time)}")

# Função principal do programa
def main():
    """
    Função principal do programa
    """
    num_rows_to_create = 1000000  # Número de linhas a serem criadas
    weather_station_names = []
    weather_station_names = build_weather_station_name_list()
    print(estimate_file_size(weather_station_names, num_rows_to_create))
    build_test_data(weather_station_names, num_rows_to_create)
    print("Arquivo de teste finalizado.")

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
exit()