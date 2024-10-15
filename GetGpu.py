import GPUtil

class GetGPU:
    def __init__(self):
        self.control_data = GPUtil.getGPUs()
    
    def get_name_GPU(self):
        call = []
        result = ''
    
        for i in range(len(self.control_data)):
            get_gpu_name = self.control_data[i]
        
            call.append({'GPU_name': getattr(get_gpu_name, 'name', 'Unknown'),})
            result += call[i].get('GPU_name')
        
    
        return result
    
    def get_temp_GPU(self):
        call = []
        result = ''
    
        for i in range(len(self.control_data)):
            get_gpu_temperature = self.control_data[i]
        
            call.append({'temperature': getattr(get_gpu_temperature, 'temperature', 'Unknown'),})
            result += str(call[i].get('temperature'))
        
    
        return result
    
    def get_memory_used_GPU(self):
        call = []
        result = ''
    
        for i in range(len(self.control_data)):
            get_gpu_memoru_used = self.control_data[i]
        
            call.append({'memoryUsed': getattr(get_gpu_memoru_used, 'memoryUsed', 'Unknown'),})
            result += str(call[i].get('memoryUsed'))
        
    
        return result
    
    def get_memory_total_GPU(self):
        call = []
        result = ''
    
        for i in range(len(self.control_data)):
            get_gpu_total_memory = self.control_data[i]
        
            call.append({'memoryTotal': getattr(get_gpu_total_memory, 'memoryTotal', 'Unknown'),})
            result += str(call[i].get('memoryTotal'))
        
    
        return result