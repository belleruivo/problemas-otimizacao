class Entrada:
    @staticmethod
    def obter_volume():
        while True:
            try:
                print("\n=== 📏 CALCULADORA DE OTIMIZAÇÃO DE CILINDRO 📏 ===")
                volume = float(input("\nDigite o volume do recipiente em ml (1ml = 1cm³): "))
                if volume <= 0:
                    print("❌ ERRO: O volume precisa ser positivo!")
                    continue
                return volume
            except ValueError:
                print("❌ ERRO: Digite um número válido!")

    @staticmethod
    def obter_tampa():
        while True:
            tem_tampa = input("\nO recipiente tem tampa? (s/n): ").lower()
            if tem_tampa in ['s', 'n']:
                return tem_tampa == 's'
            print("❌ ERRO: Digite 's' para sim ou 'n' para não!")

    @staticmethod
    def obter_custos():
        while True:
            try:
                print("\n=== 💰 CUSTOS DOS MATERIAIS 💰 ===")
                custo_base = float(input("\nDigite o custo do material da base (R$/cm²): "))
                if custo_base <= 0:
                    print("❌ ERRO: O custo precisa ser positivo!")
                    continue
                
                custo_lateral = float(input("Digite o custo do material lateral (R$/cm²): "))
                if custo_lateral <= 0:
                    print("❌ ERRO: O custo precisa ser positivo!")
                    continue
                
                return custo_base, custo_lateral
            except ValueError:
                print("❌ ERRO: Digite números válidos!")