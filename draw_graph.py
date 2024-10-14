import matplotlib.pyplot as plt

class DrawGraph:
    def __init__(self) -> None:
        self.control = plt     
    
    def draw_graph_cpu(self, data_cpu):
        fig, ax = self.control.subplots()
        self.control.plot(data_cpu, label='Нагрузка процессора', color='blue', linestyle='-', marker='o')
        self.control.legend(loc='upper left', frameon=True)
        self.control.grid(True)
        ax.set_facecolor('#444444')
        self.control.show()
        
    def draw_graph_gpu(self, data_gpu):
        fig, ax = self.control.subplots()
        self.control.plot(data_gpu, label='Нагрузка GPU', color='blue', linestyle='-', marker='o')
        self.control.legend(loc='upper left', frameon=True)
        self.control.grid(True)
        ax.set_facecolor('#444444')
        self.control.show()
        
    def draw_graph_gpu_temp(self, data_gpu_temp):
        fig, ax = self.control.subplots()
        self.control.plot(data_gpu_temp, label='Температура GPU', color='red', linestyle='-', marker='o')
        self.control.legend(loc='upper left', frameon=True)
        self.control.grid(True)
        ax.set_facecolor('#444444')
        self.control.show()