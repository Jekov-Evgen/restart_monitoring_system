import ctypes
import GPUtil

def data_CPU_C():
    try:
        receiving_CPU_data_C = ctypes.CDLL(r"C++\dataRequest.dll")
    except OSError as e:
        print(f"Ошибка загрузки библиотеки: {e}")
        return None
    
    receiving_CPU_data_C.GetCPULoad.restype = ctypes.c_float
    result = receiving_CPU_data_C.GetCPULoad()
    
    return str(round(result, 3) * 1000)

def data_memory_C():
    try:
        receiving_memory_data_C = ctypes.CDLL(r"C++\dataRequest.dll")
    except OSError as e:
        print(f"Ошибка загрузки библиотеки: {e}")
        return None

    receiving_memory_data_C.GetMemory.restype = ctypes.c_float
    result = receiving_memory_data_C.GetMemory()

    return str(round(result, 2))

def data_GPU():
    result = ''
    
    try:
        receiving_GPU_data_C = GPUtil.getGPUs()
        
        for gpu in receiving_GPU_data_C:
            result += str(gpu.load)
    except:
        print("Ошибка получения данных")
        return None
        
    return result