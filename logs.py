# %% [markdown]
# # Análisis de Logs en JSON  
# ### Uso de listas, diccionarios y sets en Python
# En este ejercicio trabajaremos con un archivo JSON que contiene registros (logs) reales de un sistema web.  
# El objetivo es practicar estructuras de datos en Python usando **listas**, **diccionarios**, **sets**, **comprehensions**, etc.
# 

# %% [markdown]
# ## Dataset: logs.json
# 
# El archivo contiene una lista de registros con información sobre usuarios, acciones, IPs y estados de respuesta.
# 
# Cada registro es un diccionario:
# 
# ```json
# {
#     "user": "ana",
#     "action": "login",
#     "ip": "192.168.1.10",
#     "status": 200,
#     "timestamp": "2025-01-14T10:23:11"
# }
# 

# %%
import argparse
import json

# %% [markdown]
# # Ejercicios
# 
# Debes resolver los siguientes ejercicios.  
# Puedes usar **listas**, **sets** o **diccionarios**

# %% [markdown]
# ### **Ejercicio 1 — Contar acciones realizadas en los logs**
# Crea una función que cuente cuántas veces aparece cada acción dentro de la lista de logs.
# 
# - **Function name:** `count_actions`
# - **Entrada:** lista de diccionarios (`list[dict]`)
# - **Salida:** diccionario con acción → número de ocurrencias (`dict[str, int]`)

# %%
def count_actions(logs ):
    action_counts = {}
    for log in logs:
        action = log.get('action')
        if action:
            if action in action_counts:
                action_counts[action] += 1
            else:
                action_counts[action] = 1
    return action_counts

# %% [markdown]
# ### **Ejercicio 2 — Obtener lista de usuarios únicos**
# Crea una función que devuelva un conjunto con todos los usuarios distintos presentes en los logs.
# 
# - **Function name:** `get_unique_users`
# - **Entrada:** lista de diccionarios (`list[dict]`)
# - **Salida:** conjunto de strings (`set[str]`)

# %%
def get_unique_users(logs):
    users = set()
    for log in logs:
        user = log.get('user')
        users.add(user)
    return users

# %% [markdown]
# ### **Ejercicio 3 — Detectar qué usuarios han tenido errores (`status == 4XX`).**
# Crea una función que devuelva 
# 
# - **Function name:** `filter_by_status`
# - **Entrada:**  
#   - lista de diccionarios (`list[dict]`)  
# - **Salida:** conjunto de strings (`set[str]`)

# %%
def filter_by_status(logs):
    error_users = set()
    for log in logs:
        status = str (log.get('status'))
        if status.startswith('4'):
            user = log.get('user')
            error_users.add(user)
    return error_users

# %% [markdown]
# ### **Ejercicio 4 — Obtener IPs únicas de los logs**
# Crea una función que extraiga todas las direcciones IP de los logs, sin repetir ninguna.
# 
# - **Function name:** `get_unique_ips`
# - **Entrada:** lista de diccionarios (`list[dict]`)
# - **Salida:** conjunto de strings (`set[str]`)

# %%
def get_unique_ips(logs):
    ips = set()
    for log in logs:
        ip = log.get('ip')
        ips.add(ip)
    return ips

# %% [markdown]
# ### **Ejercicio 5 — Encontrar el usuario con más acciones registradas**
# Crea una función que determine qué usuario aparece más veces en los logs.
# 
# - **Function name:** `most_frequent_user`
# - **Entrada:** lista de diccionarios (`list[dict]`)
# - **Salida:** string con nombre del usuario (`str`)

# %%
def most_frequent_user(logs):
    user_counts = {}
    for log in logs:
        user = log.get('user')
        if user:
            if user in user_counts:
                user_counts[user] += 1
            else:
                user_counts[user] = 1
    most_frequent = max(user_counts, key=user_counts.get)
    return most_frequent

# %% [markdown]
# ### Ejercicio Final — `run_selected_exercise`
# 
# **Descripción:**  
# Crea una función llamada **`run_selected_exercise`** que reciba dos entradas:
# 
# 1. **`json_path`** (str):  
#    Un *path absoluto* hacia un archivo JSON local.  
#    Este JSON contiene una **lista de diccionarios** que simulan logs del sistema.
# 
# 2. **`exercise_number`** (int):  
#    Puede ser **1, 2, 3, 4 o 5**.  
#    Este número indica qué ejercicio anterior debe ejecutarse.
# 
# La función debe:
# 
# - Leer el archivo JSON desde `json_path`.
# - Cargar la lista de diccionarios de logs.
# - En función del número recibido:
#   - Llamar internamente a la función correspondiente al ejercicio **1**, **2**, **3**, **4** o **5**.
# - Recibir el resultado del ejercicio elegido.
# - **Imprimir** ese resultado por pantalla usando `print`.
# 
# **Entradas:**
# - `json_path` (str) — ruta absoluta a un archivo JSON.
# - `exercise_number` (int) — número de ejercicio a ejecutar (1, 2, 3, 4 o 5).
# 
# **Salida:**
# - Ninguna salida de retorno.  
# - La función **imprime** por pantalla el resultado del ejercicio seleccionado.
# 
# **Nombre de la función:**  
# `run_selected_exercise`
# 

# %%
def run_selected_exercise(json_path, exercise_number):
    with open(json_path, 'r') as file:
        logs = json.load(file)

    if exercise_number == 1:
        return count_actions(logs)
    elif exercise_number == 2:
        return get_unique_users(logs)
    elif exercise_number == 3:
        return filter_by_status(logs)
    elif exercise_number == 4:
        return get_unique_ips(logs)
    elif exercise_number == 5:
        return most_frequent_user(logs)
    else:
        return "Invalid exercise number."
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run selected log analysis exercise.')
    parser.add_argument('--jsonpath', type=str, help='Path to the JSON log file')
    parser.add_argument('--exercisenumber', type=int, help='Exercise number to run (1-5)')
    args = parser.parse_args()
    json_path = args.jsonpath  
    exercise_number = args.exercisenumber
    result = run_selected_exercise(json_path, exercise_number)
    print(result)


