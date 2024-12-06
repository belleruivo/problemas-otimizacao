import os
from entrada import Entrada
from calculadora import Calculadora

class OtimizadorCilindro:
    def __init__(self, entrada, calculadora):
        self.entrada = entrada
        self.calculadora = calculadora

    def executar(self):
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
            primeira_derivada = self.calculadora.primeira_derivada(volume, custo_base, custo_lateral, ponto_critico, n_bases)
            segunda_derivada = self.calculadora.verificar_minimo(volume, custo_base, custo_lateral, ponto_critico, n_bases)
            
            self.mostrar_resultados(raio, altura, custo_base_total, custo_lateral_total, custo_total, ponto_critico, primeira_derivada, segunda_derivada)
            
            repetir = input("\nDeseja calcular novamente? (s/n): ").strip().lower()
            if repetir != 's':
                break

    def mostrar_resultados(self, raio, altura, custo_base_total, custo_lateral_total, custo_total, ponto_critico, primeira_derivada, segunda_derivada):
        print("\n=== 📊 RESULTADOS DA OTIMIZAÇÃO 📊 ===")
        print(f"\nDimensões ótimas do recipiente:")
        print(f"📏 Raio: {raio:.2f} cm")
        print(f"📏 Altura: {altura:.2f} cm")
        print(f"📏 Diâmetro: {2 * raio:.2f} cm")
        
        print(f"\n💰 Custos:")
        print(f"💵 Custo da(s) base(s): R$ {custo_base_total:.2f}")
        print(f"💵 Custo lateral: R$ {custo_lateral_total:.2f}")
        print(f"💵 Custo total: R$ {custo_total:.2f}")
        
        print("\n=== 📈 DERIVADAS 📈 ===")
        print(f"📍 Ponto crítico (raio ótimo): {ponto_critico:.2f} cm")
        print(f"📉 Primeira derivada no ponto crítico: {primeira_derivada:.2f}")
        print(f"📈 Segunda derivada no ponto crítico: {segunda_derivada:.2f}")
        
        if segunda_derivada > 0:
            print("✅ Como a segunda derivada é positiva, confirmamos que é um ponto de mínimo!")
        else:
            print("❌ A segunda derivada não é positiva, o ponto crítico não é um mínimo!")

if __name__ == "__main__":
    entrada = Entrada()
    calculadora = Calculadora()
    otimizador = OtimizadorCilindro(entrada, calculadora)
    otimizador.executar()
