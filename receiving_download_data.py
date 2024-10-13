import ctypes
import GPUtil

def processor_integration():
    try:
        lib = ctypes.CDLL(r"C++\dataRequest.dll")
    except OSError as e:
        print(f"Ошибка загрузки библиотеки: {e}")
        return None
    
    lib.GetCPULoad.restype = ctypes.c_float
    result = lib.GetCPULoad()
    
    return str(round(result, 3) * 1000)

def memory_integration():
    try:
        lib= ctypes.CDLL(r"C++\dataRequest.dll")
    except OSError as e:
        print(f"Ошибка загрузки библиотеки: {e}")
        return None

    lib.GetMemory.restype = ctypes.c_float
    result = lib.GetMemory()

    return str(round(result, 2))

def GPU_integration():
    result = ''
    
    try:
        data_GPU = GPUtil.getGPUs()
        
        for gpu in data_GPU:
            result += str(gpu.load)
    except:
        print("Ошибка получения данных")
        return None
        
    return result