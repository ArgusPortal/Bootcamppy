import duckdb
import time

# Função para executar uma query em DuckDB
def create_duckdb():
    """
    Executa uma query em DuckDB para ler o arquivo de dados, calcular
    a temperatura mínima, média e máxima para cada estação e imprimir
    os resultados ordenados por estação.
    """
    # Executa a query SQL em DuckDB
    duckdb.sql("""
        SELECT station,
            MIN(temperature) AS min_temperature,
            CAST(AVG(temperature) AS DECIMAL(3,1)) AS mean_temperature,
            MAX(temperature) AS max_temperature
        FROM read_csv("data/measurements.txt", AUTO_DETECT=FALSE, sep=';', columns={'station':VARCHAR, 'temperature': 'DECIMAL(3,1)'})
        GROUP BY station
        ORDER BY station
    """).show()  # Mostra os resultados da query

# Bloco principal do script
if __name__ == "__main__":
    import time
    start_time = time.time()  # Marca o tempo de início
    create_duckdb()  # Chama a função para executar a query em DuckDB
    took = time.time() - start_time  # Calcula o tempo decorrido
    print(f"Duckdb Took: {took:.2f} sec")  # Imprime o tempo decorrido