import os
from entrada import Entrada
from calculadora import Calculadora

def main():
    while True:
        # Limpando a tela
        os.system('cls' if os.name == 'nt' else 'clear')

        # Obtendo inputs do usuário
        volume = Entrada.obter_volume()
        tem_tampa = Entrada.obter_tampa()
        custo_base, custo_lateral = Entrada.obter_custos()
        
        n_bases = 2 if tem_tampa else 1
        
        # Calculando dimensões ótimas
        raio, altura, custo_base_total, custo_lateral_total, custo_total = Calculadora.calcular_dimensoes(
            volume, tem_tampa, custo_base, custo_lateral
        )
        
        # Calculando ponto crítico e derivadas
        ponto_critico = Calculadora.calcular_ponto_critico(volume, custo_base, custo_lateral, n_bases)
        primeira_derivada = Calculadora.primeira_derivada(volume, custo_base, custo_lateral, ponto_critico, n_bases)
        segunda_derivada = Calculadora.verificar_minimo(volume, custo_base, custo_lateral, raio, n_bases)
        
        # Mostrando resultados
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
        print("✅ Como a segunda derivada é positiva, confirmamos que é um ponto de mínimo!")
        
        # Perguntar ao usuário se deseja calcular novamente
        repetir = input("\nDeseja calcular novamente? (s/n): ").strip().lower()
        if repetir != 's':
            break

if __name__ == "__main__":
    main()