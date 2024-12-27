import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Funções de crescimento comum
def O_1(n): return 1
def O_log_n(n): return np.log2(n)
def O_n(n): return n
def O_n_log_n(n): return n * np.log2(n)
def O_n2(n): return n**2

# Teste de desempenho
def measure_execution_time(func, sizes):
    times = []
    for size in sizes:
        start_time = time.time()
        func(size)  # Executa a função
        end_time = time.time()
        times.append(end_time - start_time)
    return times

# Função para análise
def analyze_complexity(sizes, times):
    functions = [O_1, O_log_n, O_n, O_n_log_n, O_n2]
    labels = ["O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n^2)"]

    best_fit = None
    best_label = None
    min_error = float('inf')

    for func, label in zip(functions, labels):
        try:
            popt, _ = curve_fit(func, sizes, times)
            error = np.mean((func(np.array(sizes)) * popt[0] - times) ** 2)
            if error < min_error:
                min_error = error
                best_fit = func
                best_label = label
        except Exception:
            pass

    return best_label, best_fit

# Gráfico
def plot_results(sizes, times, best_fit, best_label):
    plt.scatter(sizes, times, label="Medições", color='blue')
    if best_fit:
        plt.plot(sizes, best_fit(np.array(sizes)), label=f"Ajuste: {best_label}", color='red')
    plt.xlabel("Tamanho da Entrada (n)")
    plt.ylabel("Tempo (s)")
    plt.title("Análise de Complexidade Assintótica")
    plt.legend()
    plt.show()

# Exemplo: função para analisar
def example_function(size):
    # Simula uma função O(n^2)
    for _ in range(size):
        for _ in range(size):
            pass

# Entradas e análise
sizes = [10, 20, 40, 80, 160]
times = measure_execution_time(example_function, sizes)
best_label, best_fit = analyze_complexity(sizes, times)
plot_results(sizes, times, best_fit, best_label)

print(f"Complexidade estimada: {best_label}")
