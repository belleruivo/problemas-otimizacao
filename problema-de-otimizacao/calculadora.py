import math 
from typing import Tuple # Importa Tuple para definir tipos de retorno das funções

class Calculadora:
    @staticmethod
    def calcular_dimensoes(volume: float, tem_tampa: bool, custo_base: float, custo_lateral: float) -> Tuple[float, float, float, float, float]:
        n_bases = 2 if tem_tampa else 1 
        
        # volume
        volume_real = volume * math.pi

        # raio ótimo - isso está na conta da folha!
        raio = (volume_real * custo_lateral / (math.pi * custo_base * n_bases)) ** (1/3)
        
        # altura - isso está na conta da folha!
        altura = volume_real / (math.pi * raio**2)
        
        # custos - isso está na conta da folha!
        area_base = math.pi * raio**2
        area_lateral = 2 * math.pi * raio * altura
        custo_base_total = n_bases * custo_base * area_base
        custo_lateral_total = custo_lateral * area_lateral
        custo_total = custo_base_total + custo_lateral_total

        return raio, altura, custo_base_total, custo_lateral_total, custo_total

    @staticmethod
    def calcular_ponto_critico(volume, custo_base, custo_lateral, n_bases):
        return (volume * custo_lateral / (n_bases * custo_base * math.pi)) ** (1/3)

    @staticmethod
    def primeira_derivada(volume, custo_base, custo_lateral, raio, n_bases):
        return 2 * math.pi * custo_base * n_bases * raio - (2 * volume * custo_lateral) / (raio**2)

    @staticmethod
    def verificar_minimo(volume, custo_base, custo_lateral, raio, n_bases):
        return 2 * math.pi * custo_base * n_bases + 4 * volume * custo_lateral / (raio**3)
