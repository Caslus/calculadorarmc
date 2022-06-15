import curses;
import math;
import cmath;
import numpy as np;
import matplotlib.pyplot as plt;
import misc;


titulo = misc.titulo;
subtitulo = misc.subtitulo;
opcoes = misc.opcoes;
enterVolta = misc.enterVolta;
erro = misc.erro;
fx = misc.fx;
valorParaX = misc.valorParaX;
valorParaA = misc.valorParaA;
valorParaB = misc.valorParaB;
valorParaC = misc.valorParaC;
opcoesSegundoGrau = {
    0 : "Calcular raízes",
    1 : "Calcular função em x pedido",
    2 : "Calcular vértice",
    3 : "Gerar gráfico",
    4 : "Voltar"
};
equacaoSegundoGrau = "f(x) = ax² + bx + c";
raiz = "Raíz:";
raizes = "Raízes:";
raizesComplexas = "Raízes complexas:";
ponto = "Ponto ";
maximo = "máximo:";
minimo = "mínimo:";

def menu(stdscr):
    while 1:
        stdscr.clear();
        stdscr.addstr(titulo, curses.A_BOLD);
        stdscr.addstr(1, 0, opcoes[0], curses.A_BOLD);
        stdscr.addstr(2, 0, equacaoSegundoGrau);
        stdscr.addstr(4, 0, valorParaA);
        curses.curs_set(1);
        curses.echo();
        a = stdscr.getstr(5,0).decode(encoding="utf-8");
        if(misc.isValidNumber(a)): 
            a = float(a);
            break;
    while 1:
        stdscr.clear();
        stdscr.addstr(titulo, curses.A_BOLD);
        stdscr.addstr(1, 0, opcoes[0], curses.A_BOLD);
        stdscr.addstr(2, 0, equacaoSegundoGrau);
        stdscr.addstr(4, 0, valorParaB);
        curses.curs_set(1);
        curses.echo();
        b = stdscr.getstr(5,0).decode(encoding="utf-8");
        if(misc.isValidNumber(b)): 
            b = float(b);
            break;
    while 1:
        stdscr.clear();
        stdscr.addstr(titulo, curses.A_BOLD);
        stdscr.addstr(1, 0, opcoes[0], curses.A_BOLD);
        stdscr.addstr(2, 0, equacaoSegundoGrau);
        stdscr.addstr(4, 0, valorParaC);
        curses.curs_set(1)
        curses.echo();
        c = stdscr.getstr(5,0).decode(encoding="utf-8");
        if(misc.isValidNumber(c)): 
            c = float(c);
            break;
    
    curses.curs_set(0);

    selecionado = 0;
    printMenu(stdscr, selecionado, a, b, c);
    while 1:
        key = stdscr.getch();
        if key == curses.KEY_UP:
            if selecionado > 0: selecionado-=1;
            else: selecionado = len(opcoesSegundoGrau)-1;
        elif key == curses.KEY_DOWN:
            if selecionado < len(opcoesSegundoGrau)-1: selecionado+=1;
            else: selecionado = 0;
        elif key == curses.KEY_ENTER or key in [10,13]:
            if(selecionado==0): mostrarRaizes(stdscr, a, b, c);
            if(selecionado==1): calc(stdscr, a, b, c);
            if(selecionado==2): calcVertice(stdscr, a, b, c);
            if(selecionado==3): plot(a, b, c);
            elif(selecionado==4): return;
        printMenu(stdscr, selecionado, a, b, c);

    stdscr.refresh();

def formarEquacao(a,b,c):
    if(a % 1 == 0): a = int(a);
    if(a==1): a = '';
    if(a==-1): a = '-';
    if(b % 1 == 0): b = int(b);
    if(b==1): b = '';
    if(b==-1): b = '-';
    if(c % 1 == 0): c = int(c);
    return "f(x) = %sx² + %sx + %s"%(a,b,c);

def printMenu(stdscr, selecionado, a,b,c):
    stdscr.clear();
    stdscr.addstr(titulo, curses.A_BOLD);
    stdscr.addstr(1, 0, opcoes[0], curses.A_BOLD);
    stdscr.addstr(2, 0, formarEquacao(a,b,c));
    stdscr.addstr(3, 0, subtitulo);

    for i in opcoesSegundoGrau:
        if(i==selecionado):
            stdscr.attron(curses.color_pair(1));
            stdscr.addstr(i+4, 0, "> "+opcoesSegundoGrau[i]);
            stdscr.attroff(curses.color_pair(1));
        else:
            stdscr.addstr(i+4, 2, opcoesSegundoGrau[i]);

def mostrarRaizes(stdscr, a, b, c):
    stdscr.clear();
    stdscr.addstr(titulo, curses.A_BOLD);
    stdscr.addstr(1, 0, opcoes[0], curses.A_BOLD);
    stdscr.addstr(2, 0, formarEquacao(a,b,c));
    d = (b**2) - (4 * a * c);
    if d > 0:
        r1 = (-b-math.sqrt(d))/(2*a);
        r2 = (-b+math.sqrt(d))/(2*a);
        stdscr.addstr(3, 0, raizes);
        stdscr.addstr(4, 0, str(r1));
        stdscr.addstr(5, 0, str(r2));
    elif d == 0:
        r1 = (-b+math.sqrt(d))/(2*a);
        stdscr.addstr(3, 0, raiz);
        stdscr.addstr(4, 0, str(r1));
    else:
        r1 = (-b+cmath.sqrt(d))/(2*a);
        r2 = (-b-cmath.sqrt(d))/(2*a);
        stdscr.addstr(3, 0, raizesComplexas);
        stdscr.addstr(4, 0, str(r1));
        stdscr.addstr(5, 0, str(r2));

    stdscr.addstr(7, 0, enterVolta);
    while 1:
        key = stdscr.getch();
        if key == curses.KEY_ENTER or key in [10,13]:
            return;

def calc(stdscr, a, b, c):
    while 1:
        stdscr.clear();
        stdscr.addstr(titulo, curses.A_BOLD);
        stdscr.addstr(1, 0, opcoes[0], curses.A_BOLD);
        stdscr.addstr(2, 0, formarEquacao(a,b,c));
        stdscr.addstr(3, 0, valorParaX);
        curses.curs_set(1);
        curses.echo();
        x = stdscr.getstr(4,0).decode(encoding="utf-8");
        if(misc.isValidNumber(x)): 
            x = float(x);
            break;
    if(x % 1 == 0): x = int(x);

    try:
        res = a*(x**2)+b*x+c;
        if(res % 1 == 0): res = int(res);
    except:
        res = erro;

    curses.curs_set(0);
    curses.noecho();
    stdscr.move(3,0);
    stdscr.clrtoeol();
    stdscr.move(4,0);
    stdscr.clrtoeol();
    stdscr.addstr(3, 0, fx%(x)+str(res));
    stdscr.addstr(5, 0, enterVolta);
    stdscr.refresh();
    while 1:
        key = stdscr.getch();
        if key == curses.KEY_ENTER or key in [10,13]:
            return; 

def plot(a, b, c):
    x = np.linspace(-2, 2, 100);
    y = a*x**2+b*x+c;

    fig, ax = plt.subplots();
    ax.axhline(y=0, color="k");
    ax.axvline(x=0, color="k");
    plt.plot(x, y);
    ax.set_title(formarEquacao(a,b,c));
    plt.grid(True);
    plt.show();

def calcVertice(stdscr, a, b, c):
    stdscr.clear();
    stdscr.addstr(titulo, curses.A_BOLD);
    stdscr.addstr(1, 0, opcoes[0], curses.A_BOLD);
    stdscr.addstr(2, 0, formarEquacao(a,b,c));
    x = (-(b/(2*a)));
    if(x % 1 == 0): x = int(x);
    y = -((b**2-(4*a*c))/(4*a));
    if(y % 1 == 0): y = int(y);
    if a<0:
        stdscr.addstr(3,0, ponto+maximo);
        stdscr.addstr(4,0, "(%s, %s)"%(x,y));
    else:
        stdscr.addstr(3,0, ponto+minimo);
        stdscr.addstr(4,0, "(%s, %s)"%(x,y));

    stdscr.addstr(6, 0, enterVolta);
    while 1:
        key = stdscr.getch();
        if key == curses.KEY_ENTER or key in [10,13]:
            return; 
