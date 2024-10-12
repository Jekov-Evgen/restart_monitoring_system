import socket
import cpuinfo
import psutil
import GPUtil

exact_conversion_to_GB = 1073741824

class PC:
    def __init__(self) -> None:
        pass
    
    def machine_name(self):
        return socket.gethostname()
    
    def cpu_name(self):
        call = cpuinfo.get_cpu_info()
        result = call.get('brand_raw')
        return result
    
    def memory_total(self):
        call = psutil.virtual_memory()
        
        return str(round(call[0] / exact_conversion_to_GB, 2))
    
    def gpu_name(self):
        call = GPUtil.getGPUs()
        result = ''
        
        for i in call:
            result += i.name
            
        return result
    
    def memory_disk(self):
        all_disks = []
        self.information_of_all_disks = []
        result = []
        
        for i in psutil.disk_partitions():
            all_disks.append(i[0])
            
        for i in all_disks:
            self.information_of_all_disks.append(psutil.disk_usage(i))
            
        for i in self.information_of_all_disks:
            result.append(str(round(i[0] / exact_conversion_to_GB)))
        
        return result
    
    def disk_load(self):
        self.memory_disk()
        data = self.information_of_all_disks
        res = []
        
        for i in data:
            res.append(data[0][3])
            
        return res
    
    
tt = PC()

print(tt.disk_load())