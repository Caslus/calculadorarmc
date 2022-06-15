titulo = "Calculadora RMC";
subtitulo = "↑ e ↓ para navegar, ENTER para confirmar";
opcoes = {
    0 : "Funções de segundo grau",
    1 : "Funções exponenciais",
    2 : "Matrizes",
    3 : "Sair"
};
erro = "Houve um erro ao calcular";
enterVolta = "Aperte ENTER para voltar";
fx = "f(%s) = ";
valorParaX = "Valor de x:";
valorParaA = "Valor de a:";
valorParaB = "Valor de b:";
valorParaC = "Valor de c:";

def isValidNumber(n):
    try:
        float(n);
        return True;
    except:
        return False;