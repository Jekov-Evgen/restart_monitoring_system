import cpuinfo

conversion_to_megabytes = 1024

class GetCPU:
    def __init__(self):
        self.contol_data = cpuinfo.get_cpu_info()
        
    def all_result(self):
        return self.contol_data
    
    def get_name_CPU(self):
        return self.contol_data.get('brand_raw')
    
    def get_arch_CPU(self):
        return self.contol_data.get('arch')
    
    def get_hz_actual_CPU(self):
        return self.contol_data.get('hz_actual_friendly')
    
    def get_hz_advertised_CPU(self):
        return self.contol_data.get('hz_advertised_friendly')
    
    def get_L2_cache_CPU(self):
        return str(int(self.contol_data.get('l2_cache_size')) / (conversion_to_megabytes * conversion_to_megabytes))
    
    def get_L3_cache_CPU(self):
        return str(int(self.contol_data.get('l3_cache_size')) / (conversion_to_megabytes * conversion_to_megabytes))
    
    def get_bool_ht_CPU(self):
        check = self.contol_data.get('flags')
        
        if "ht" in check:
            return "Поддержка многопоточности присутствует"
        else:
            return "Нет поддержки многопоточности"
    
    def get_bool_aes_CPU(self):
        check = self.contol_data.get('flags')
        
        if "aes" in check:
            return "Поддержка аппаратного шифрования присутствует"
        else:
            return "Нет поддержки аппаратного шифрования"
        
    def get_bool_vec_CPU(self):
        check = self.contol_data.get('flags')
        
        if (("avx" in check) and ("avx2" in check) and ("sse" in check)
            and ("sse2" in check) and ("sse4_1" in check) and ("sse4_2" in check)):  
               
            return "Поддержка векторных инструкций присутствует"
        else:
            return "Нет поддержки векторных инструкций"
        
    def get_count_CPU(self):
        return str(self.contol_data.get('count'))