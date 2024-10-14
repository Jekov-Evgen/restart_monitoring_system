import psutil

class GetProcess:
    def __init__(self) -> None:
        pass
    
    def get_process(self):
        call =  [proc.name() for proc in psutil.process_iter() if proc.status() == psutil.STATUS_RUNNING]
        result = []
        
        for i in range(len(call)):
            temp = call[i].split('.')
            result.append(temp[0])
        
        return result
