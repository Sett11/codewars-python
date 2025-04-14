from concurrent.futures import ThreadPoolExecutor

def task_master(functions):
    total = 0
    with ThreadPoolExecutor(max_workers=len(functions)) as executor:
        futures = [executor.submit(func) for func in functions]
        for future in futures:
            total += future.result()
    return total