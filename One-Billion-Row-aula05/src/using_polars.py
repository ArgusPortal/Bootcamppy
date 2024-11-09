import polars as pl

# Created by Koen Vossen, 
# Github: https://github.com/koenvo
# Twitter/x Handle: https://twitter.com/mr_le_fox
# https://x.com/mr_le_fox/status/1741893400947839362?s=20

# Função para criar um DataFrame usando Polars
def create_polars_df():
    # Configura o tamanho do chunk para streaming
    pl.Config.set_streaming_chunk_size(1000000)
    return (
        # Lê o arquivo CSV usando Polars em modo de streaming
        pl.scan_csv("data/measurements.txt", separator=";", has_header=False, new_columns=["station", "measure"], schema={"station": pl.String, "measure": pl.Float64})
        # Agrupa os dados pela coluna 'station'
        .group_by(by="station")
        # Agrega os dados calculando o máximo, mínimo e média da coluna 'measure'
        .agg(
            max = pl.col("measure").max(),
            min = pl.col("measure").min(),
            mean = pl.col("measure").mean()
        )
        # Ordena os resultados pela coluna 'station'
        .sort("station")
        # Coleta os resultados em um DataFrame, habilitando o streaming
        .collect(streaming=True)
    )

# Bloco principal do script
if __name__ == "__main__":
    import time
    start_time = time.time()  # Marca o tempo de início
    # Chama a função para criar o DataFrame e imprime o resultado
    df = create_polars_df()
    print(df)
    took = time.time() - start_time  # Calcula o tempo decorrido
    print(f"Polars Took: {took:.2f} sec")  # Imprime o tempo decorrido