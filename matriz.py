import curses
import numpy;
import misc;

titulo = misc.titulo;
subtitulo = misc.subtitulo;
opcoes = misc.opcoes;
valorLinhas = "Número de linhas:";
valorColunas = "Número de colunas:";
nomeMatrizA = "Matriz A";
nomeMatrizB = "Matriz B";
valorPara = "Valor para (%s, %s):";
enterVolta = misc.enterVolta;
opcoesMatriz = {
    0 : "Determinante (2X2 ou 3X3)",
    1 : "Multiplicação",
    2 : "Matriz transposta",
    3 : "Voltar"
};
erroTamanhoMatriz = "A matriz não é 2X2 ou 3X3.";
determinante = "Determinante: %s";
erroMultiplicacao = "Essa multiplicação não é possível.";
axb = "AxB=";

def menu(stdscr):

    linhas = pedirLinhas(stdscr, nomeMatrizA);
    colunas = pedirColunas(stdscr, nomeMatrizA);
    matrizA = pedirValores(stdscr, linhas, colunas, nomeMatrizA);
    
    selecionado = 0;
    printMenu(stdscr, selecionado, matrizA, colunas);
    while 1:
        key = stdscr.getch();
        if key == curses.KEY_UP:
            if selecionado > 0: selecionado-=1;
            else: selecionado = len(opcoesMatriz)-1;
        elif key == curses.KEY_DOWN:
            if selecionado < len(opcoesMatriz)-1: selecionado+=1;
            else: selecionado = 0;
        elif key == curses.KEY_ENTER or key in [10,13]:
            if(selecionado==0): calcDeterminante(stdscr, matrizA, colunas);
            if(selecionado==1): multiplicacao(stdscr, matrizA);
            if(selecionado==2): transposta(stdscr, matrizA, colunas);
            elif(selecionado==3): return;
        printMenu(stdscr, selecionado, matrizA, colunas);
    
    stdscr.refresh();

def printMenu(stdscr, selecionado, matriz, colunas):
    stdscr.clear();
    stdscr.addstr(titulo, curses.A_BOLD);
    stdscr.addstr(1, 0, opcoes[2], curses.A_BOLD);
    stdscr.addstr(2, 0, nomeMatrizA);
    mostrarMatriz(stdscr, matriz, 3);
    stdscr.addstr(3+colunas, 0, subtitulo);

    for i in opcoesMatriz:
        if(i==selecionado):
            stdscr.attron(curses.color_pair(1));
            stdscr.addstr(i+4+colunas, 0, "> "+opcoesMatriz[i]);
            stdscr.attroff(curses.color_pair(1));
        else:
            stdscr.addstr(i+4+colunas, 2, opcoesMatriz[i]);

def pedirLinhas(stdscr, nomeMatriz):
    while 1:
        stdscr.clear();
        stdscr.addstr(titulo, curses.A_BOLD);
        stdscr.addstr(1, 0, opcoes[2], curses.A_BOLD);
        stdscr.addstr(2, 0, nomeMatriz);
        stdscr.addstr(4, 0, valorLinhas);
        curses.curs_set(1);
        curses.echo();
        linhas = stdscr.getstr(5,0).decode(encoding="utf-8");
        if(misc.isValidNumber(linhas)): 
            try:
                linhas = int(linhas);
                if linhas > 0: break;
            except: '';
    curses.curs_set(0);
    return linhas;

def pedirColunas(stdscr, nomeMatriz):
    while 1:
        stdscr.clear();
        stdscr.addstr(titulo, curses.A_BOLD);
        stdscr.addstr(1, 0, opcoes[2], curses.A_BOLD);
        stdscr.addstr(2, 0, nomeMatriz);
        stdscr.addstr(4, 0, valorColunas);
        curses.curs_set(1);
        curses.echo();
        colunas = stdscr.getstr(5,0).decode(encoding="utf-8");
        if(misc.isValidNumber(colunas)): 
            try:
                colunas = int(colunas);
                if colunas > 0: break;
            except: '';
    curses.curs_set(0);
    return colunas;

def pedirValores(stdscr, linhas, colunas, nomeMatriz):
    matriz = numpy.zeros((linhas, colunas));
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            while 1:
                stdscr.clear();
                stdscr.addstr(titulo, curses.A_BOLD);
                stdscr.addstr(1, 0, opcoes[2], curses.A_BOLD);
                stdscr.addstr(2, 0, nomeMatriz);
                stdscr.addstr(4, 0, valorPara%(i, j));
                curses.curs_set(1);
                curses.echo();
                val = stdscr.getstr(5,0).decode(encoding="utf-8");
                if(misc.isValidNumber(val)): 
                    val = float(val);
                    matriz[i][j] = val;
                    break;
    curses.curs_set(0);
    curses.noecho();
    stdscr.refresh();
    return matriz;

def mostrarMatriz(stdscr, matriz, linha):
    for i in range(len(matriz)):
        stdscr.move(linha+i,0);
        stdscr.clrtoeol();

        if i == 0:
            stdscr.addstr(linha+i, 0, "ᒥ");
            stdscr.addstr(linha+i, len(matriz[i])*6+4, "ᒣ");
        elif i == len(matriz)-1:
            stdscr.addstr(linha+i, 0, "ᒪ");
            stdscr.addstr(linha+i, len(matriz[i])*6+4, "ᒧ");
        else:
            stdscr.addstr(linha+i, 0, "|");
            stdscr.addstr(linha+i, len(matriz[i])*6+4, "|");

        for j in range(len(matriz[i])):
            if matriz[i][j] % 1 == 0: n = str(int(matriz[i][j]));
            else: n = str(matriz[i][j]);
            stdscr.addstr(linha+i, j*6+4, n);
    stdscr.refresh();

def calcDeterminante(stdscr, matriz, colunas):
    stdscr.clear();
    stdscr.addstr(titulo, curses.A_BOLD);
    stdscr.addstr(1, 0, opcoes[2], curses.A_BOLD);
    stdscr.addstr(2, 0, opcoesMatriz[0]);
    stdscr.addstr(3, 0, nomeMatrizA);
    mostrarMatriz(stdscr, matriz, 4);
    if matriz.shape == (2,2) or matriz.shape == (3,3):
        det = numpy.linalg.det(matriz);
        det = round(det, 2);
        if(det % 1 == 0): det = int(det);
        stdscr.addstr(5+colunas, 0, determinante%(det));
    else:
        stdscr.addstr(5+colunas, 0, erroTamanhoMatriz);

    stdscr.addstr(6+colunas, 0, enterVolta);
    while 1:
        key = stdscr.getch();
        if key == curses.KEY_ENTER or key in [10,13]:
            return; 

def multiplicacao(stdscr, matrizA):
    linhasB = pedirLinhas(stdscr, nomeMatrizB);
    colunasB = pedirColunas(stdscr, nomeMatrizB);
    matrizB = pedirValores(stdscr, linhasB, colunasB, nomeMatrizB);

    stdscr.clear();
    stdscr.addstr(titulo, curses.A_BOLD);
    stdscr.addstr(1, 0, opcoes[2], curses.A_BOLD);
    stdscr.addstr(2, 0, opcoesMatriz[1]);
    try:
        resultado = numpy.matmul(matrizA, matrizB);
        stdscr.addstr(3, 0, axb);
        mostrarMatriz(stdscr, resultado, 4);
        stdscr.addstr(6+colunasB, 0, enterVolta);
    except:
        stdscr.addstr(3, 0, erroMultiplicacao);
        stdscr.addstr(5, 0, enterVolta);
    while 1:
        key = stdscr.getch();
        if key == curses.KEY_ENTER or key in [10,13]:
            return;

def transposta(stdscr, matriz, colunas):
    stdscr.clear();
    stdscr.addstr(titulo, curses.A_BOLD);
    stdscr.addstr(1, 0, opcoes[2], curses.A_BOLD);
    stdscr.addstr(2, 0, opcoesMatriz[2]);
    matrizTransposta = matriz.transpose();
    mostrarMatriz(stdscr, matrizTransposta, 3);
    stdscr.addstr(5+colunas, 0, enterVolta);
    while 1:
        key = stdscr.getch();
        if key == curses.KEY_ENTER or key in [10,13]:
            return;