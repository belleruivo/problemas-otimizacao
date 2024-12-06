import time

class Entrada:

    @staticmethod
    def introducao():
        # Introdução explicativa
        print("\n=== 📏 CALCULADORA DE OTIMIZAÇÃO DE CILINDRO 📏 ===")
        time.sleep(1)
        print("\nBem-vindo à calculadora de otimização de cilindros!")
        time.sleep(1)
        
        # Importância do exercício
        print("\nNeste programa, vamos calcular as dimensões ótimas de um recipiente cilíndrico.")
        time.sleep(1)
        print("\nEsse tipo de otimização é importante em muitos cenários, como no design de embalagens,")
        print("onde buscamos minimizar o uso de materiais enquanto mantemos o volume desejado do recipiente.")
        time.sleep(2)
        
        # Conceitos usados (Derivadas)
        print("\nVamos utilizar conceitos de cálculo, especificamente derivadas, para encontrar as dimensões ideais.")
        time.sleep(1)
        print("\nA derivada é uma ferramenta matemática que nos ajuda a entender como uma função muda.")
        print("No caso deste exercício, ela será usada para determinar os valores de raio e altura do cilindro")
        print("que minimizam o custo de material, maximizando a eficiência da produção.")
        time.sleep(3)
        
        # Conceito de ponto crítico
        print("\nUtilizando a primeira e segunda derivada, encontramos o ponto crítico, que nos dá o valor ideal do raio.")
        print("A segunda derivada nos ajuda a confirmar que esse ponto é realmente o de mínimo custo.")
        time.sleep(2)
        
        # Orientação e início
        print("\nPressione 'Enter' para começar a inserção dos dados.")
        input()

    @staticmethod
    def obter_volume():
        while True:
            print("\n=== 📏 CALCULADORA DE OTIMIZAÇÃO DE CILINDRO 📏 ===")
            volume = input("\nDigite o volume do recipiente em ml (1ml = 1cm³): ")
            
            # Verifica se o volume é um número inteiro ou decimal
            if not volume.replace('.', '', 1).isdigit():
                print("❌ ERRO: O volume deve ser um número válido!")
                continue
            
            volume = float(volume)
            if volume <= 0:
                print("❌ ERRO: O volume precisa ser positivo!")
                continue
            return volume


    @staticmethod
    def obter_tampa():
        while True:
            tem_tampa = input("\nO recipiente tem tampa? (s/n): ").strip().lower()
            if tem_tampa in ['s', 'n']:
                return tem_tampa == 's'
            print("❌ ERRO: Digite 's' para sim ou 'n' para não!")

    @staticmethod
    def obter_custos():
        while True:
            try:
                print("\n=== 💰 CUSTOS DOS MATERIAIS 💰 ===")
                
                # Recebe o custo da base e valida
                custo_base = input("\nDigite o custo do material da base (R$/cm²): ").strip()
                if ',' in custo_base:
                    print("❌ ERRO: Use ponto (.) ao invés de vírgula (,) para separar os decimais!")
                    continue
                if not custo_base.replace('.', '', 1).isdigit():
                    print("❌ ERRO: O custo precisa ser um número válido!")
                    continue
                custo_base = float(custo_base)
                
                if custo_base <= 0:
                    print("❌ ERRO: O custo precisa ser positivo!")
                    continue
                
                # Recebe o custo lateral e valida
                custo_lateral = input("Digite o custo do material lateral (R$/cm²): ").strip()
                if ',' in custo_lateral:
                    print("❌ ERRO: Use ponto (.) ao invés de vírgula (,) para separar os decimais!")
                    continue
                if not custo_lateral.replace('.', '', 1).isdigit():
                    print("❌ ERRO: O custo precisa ser um número válido!")
                    continue
                custo_lateral = float(custo_lateral)
                
                if custo_lateral <= 0:
                    print("❌ ERRO: O custo precisa ser positivo!")
                    continue
                
                return custo_base, custo_lateral
            except ValueError:
                print("❌ ERRO: O custo precisa ser um número válido!")