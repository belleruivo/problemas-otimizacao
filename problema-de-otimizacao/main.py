''' “Um recipiente cilíndrico, aberto em cima, deve ter a capacidade de 375π cm³. O custo do material usado para a base do recipiente é de R$ 0,15 por cm² e o custo do material usado na lateral é de R$ 0,05 por cm². Se não há perda de material, determine as dimensões que MINIMIZAM o custo do material para construí-lo." '''

import os
from entrada import Entrada
from calculadora import Calculadora

class OtimizadorCilindro:
    def __init__(self, entrada, calculadora):
        self.entrada = entrada
        self.calculadora = calculadora

    def executar(self):
        self.entrada.introducao()
        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            # obtendo os inputs do usuário
            volume = self.entrada.obter_volume()
            tem_tampa = self.entrada.obter_tampa()
            custo_base, custo_lateral = self.entrada.obter_custos()
            
            n_bases = 2 if tem_tampa else 1
            
            # calculando dimensões ótimas
            raio, altura, custo_base_total, custo_lateral_total, custo_total = self.calculadora.calcular_dimensoes(
                volume, tem_tampa, custo_base, custo_lateral
            )
            
            # calculando ponto crítico e derivadas
            ponto_critico = self.calculadora.calcular_ponto_critico(volume, custo_base, custo_lateral, n_bases)

            segunda_derivada = self.calculadora.verificar_minimo(volume, custo_base, custo_lateral, ponto_critico, n_bases)
            
            self.mostrar_resultados(raio, altura, custo_base_total, custo_lateral_total, custo_total, ponto_critico, segunda_derivada)
            
            repetir = input("\nDeseja calcular novamente? (s/n): ").strip().lower()
            if repetir != 's':
                break

    def mostrar_resultados(self, raio, altura, custo_base_total, custo_lateral_total, custo_total, ponto_critico, segunda_derivada):
        print("\n=== 📊 RESULTADOS DA OTIMIZAÇÃO 📊 ===")
        print(f"\nDimensões ótimas do recipiente:")
        print(f"📏 Raio: {raio:.2f} cm")
        print(f"📏 Altura: {altura:.2f} cm")
        print(f"📏 Diâmetro: {2 * raio:.2f} cm")
        
        print(f"\n💰 Custos:")
        print(f"💵 Custo da(s) base(s): R$ {custo_base_total:.2f}")
        print(f"💵 Custo lateral: R$ {custo_lateral_total:.2f}")
        print(f"💵 Custo total da embalagem: R$ {custo_total:.2f}")

        print(f"\n📍 Ponto crítico (raio ótimo): {ponto_critico:.2f} cm")
        
        if segunda_derivada > 0:
            print("✅ Como a segunda derivada é positiva, confirmamos que é um ponto de mínimo!")
        else:
            print("❌ A segunda derivada não é positiva, o ponto crítico não é um mínimo!")

if __name__ == "__main__":
    entrada = Entrada()
    calculadora = Calculadora()
    otimizador = OtimizadorCilindro(entrada, calculadora)
    otimizador.executar()
