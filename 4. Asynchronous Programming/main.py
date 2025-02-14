import asyncio
import time

# Função síncrona que simula a chamada de rede
def chamada_sync(id, tempo):
    print(f'Iniciando chamada síncrona {id}')
    time.sleep(tempo)
    print(f'Finalizando chamada síncrona {id}')

# Função principal síncrona que mede o tempo de execução das chamadas síncronas
def main_sync():
    inicio = time.time()

    # Executa as três chamadas
    chamada_sync(1, 2)
    chamada_sync(2, 1)
    chamada_sync(3, 1)

    fim = time.time()
    tempo_total = fim - inicio
    print(f'Tempo de execução síncrona: {tempo_total:.2f} segundos')


# Função assíncrona que simula uma chamada de rede
async def chamada_async(id, tempo):
    print(f'Iniciando chamada assíncrona {id}')
    await asyncio.sleep(tempo)
    print(f'Finalizando chamada assíncrona {id}')

# Função principal assíncrona que mede o tempo de execução das chamadas assíncronas
async def main_async():
    inicio = time.time()

    # Executa as três chamadas de forma concorrente
    await asyncio.gather(
        chamada_async(1, 2),
        chamada_async(2, 1),
        chamada_async(3, 1)
    )

    fim = time.time()
    tempo_total = fim - inicio
    print(f'Tempo de execução assíncrona: {tempo_total:.2f} segundos')


print('------------------------------')
print('Executando chamadas síncronas:\n')
main_sync()

print('------------------------------\n')
print('Executando chamadas assíncronas:')
asyncio.run(main_async())
