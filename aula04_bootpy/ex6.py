##  6. Eliminação de Duplicatas
##  Objetivo: Dada uma lista de emails, remover todos os duplicados.

# Lista de emails com alguns duplicados
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]

# Converte a lista de emails para um conjunto (set) para eliminar duplicados,
# e depois converte de volta para uma lista
emails_unicos = list(set(emails))

# Imprime a lista de emails sem duplicados
print(emails_unicos)