import pandas as pd
from multiprocessing import Pool, cpu_count
from tqdm import tqdm  # importa o tqdm para barra de progresso

# Define o número de processos concorrentes com base no número de CPUs disponíveis
CONCURRENCY = cpu_count()

# Define o total de linhas conhecido e o tamanho do chunk
total_linhas = 1000000  # Total de linhas conhecido
chunksize = 1000000 # Define o tamanho do chunk
filename = "data/measurements.txt"  # Certifique-se de que este é o caminho correto para o arquivo

def process_chunk(chunk):
    # Agrega os dados dentro do chunk usando Pandas
    aggregated = chunk.groupby('station')['measure'].agg(['min', 'max', 'mean']).reset_index()
    return aggregated

def create_df_with_pandas(filename, total_linhas, chunksize=chunksize):
    # Calcula o número total de chunks
    total_chunks = total_linhas // chunksize + (1 if total_linhas % chunksize else 0)
    results = []

    # Lê o arquivo CSV em chunks usando Pandas
    with pd.read_csv(filename, sep=';', header=None, names=['station', 'measure'], chunksize=chunksize) as reader:
        # Envolvendo o iterador com tqdm para visualizar o progresso
        for chunk in tqdm(reader, total=total_chunks):
            # Processa cada chunk e armazena o resultado
            results.append(process_chunk(chunk))
    
    # Concatena todos os resultados em um único DataFrame
    final_df = pd.concat(results)
    return final_df

# Bloco principal do script
if __name__ == "__main__":
    import time
    start_time = time.time()  # Marca o tempo de início
    final_df = create_df_with_pandas(filename, total_linhas, chunksize)
    print(final_df)
    took = time.time() - start_time  # Calcula o tempo decorrido
    print(f"Pandas Took: {took:.2f} sec")  # Imprime o tempo decorrido