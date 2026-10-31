"""
Projeto: Calculadora Simples em Python
Imersão Engenharia de Software: Dev na Era da IA (Alura & Google)
Objetivo: Executar operações matemáticas no terminal de forma interativa e robusta.
"""

def somar(a: float, b: float) -> float:
    """Retorna a soma de dois números."""
    return a + b


def subtrair(a: float, b: float) -> float:
    """Retorna a diferença entre dois números."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Retorna o produto de dois números."""
    return a * b


def dividir(a: float, b: float) -> float:
    """
    Retorna a divisão entre dois números.
    Lança ZeroDivisionError caso o denominador seja zero.
    """
    if b == 0:
        raise ZeroDivisionError("Não é possível realizar divisão por zero.")
    return a / b


def exibir_menu() -> None:
    """Exibe o menu de opções disponíveis para o usuário."""
    print("\n" + "=" * 32)
    print("      CALCULADORA SIMPLES      ")
    print("=" * 32)
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Sair")
    print("=" * 32)


def obter_numero(mensagem: str) -> float:
    """
    Solicita a entrada de um número ao usuário e repete até que
    um valor numérico válido (inteiro ou decimal) seja informado.
    """
    while True:
        entrada = input(mensagem)
        try:
            return float(entrada)
        except ValueError:
            print("Erro: Entrada inválida! Por favor, digite um número válido.")


def executar_calculadora() -> None:
    """Controla o fluxo principal e a repetição do programa."""
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()

        # Condição de saída do programa
        if opcao == "5":
            print("\nObrigado por utilizar a calculadora. Programa encerrado!")
            break

        # Validação do menu
        if opcao not in ("1", "2", "3", "4"):
            print("Erro: Opção inválida! Escolha um número de 1 a 5.")
            continue

        # Coleta dos números
        num1 = obter_numero("Digite o primeiro número: ")
        num2 = obter_numero("Digite o segundo número: ")

        # Execução das operações
        if opcao == "1":
            resultado = somar(num1, num2)
            print(f"\nResultado: {num1} + {num2} = {resultado}")

        elif opcao == "2":
            resultado = subtrair(num1, num2)
            print(f"\nResultado: {num1} - {num2} = {resultado}")

        elif opcao == "3":
            resultado = multiplicar(num1, num2)
            print(f"\nResultado: {num1} * {num2} = {resultado}")

        elif opcao == "4":
            try:
                resultado = dividir(num1, num2)
                print(f"\nResultado: {num1} / {num2} = {resultado}")
            except ZeroDivisionError as erro:
                print(f"\nErro de cálculo: {erro}")


if __name__ == "__main__":
    executar_calculadora()