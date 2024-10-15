import psutil

class GetProcess:
    def __init__(self):
        pass
    
    def get_process(self):
        call =  [proc.name() for proc in psutil.process_iter() 
                 if proc.status() == psutil.STATUS_RUNNING]
        result = []
        
        for i in range(len(call)):
            segment = call[i].split('.')
            result.append(segment[0])
        
        return result
