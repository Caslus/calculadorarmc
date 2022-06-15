import curses;
import numpy as np;
import matplotlib.pyplot as plt
import misc;

titulo = misc.titulo;
subtitulo = misc.subtitulo;
opcoes = misc.opcoes;
erro = misc.erro;
fx = misc.fx;
valorParaX = misc.valorParaX;
valorParaA = misc.valorParaA;
valorParaB = misc.valorParaB;
enterVolta = misc.enterVolta;
opcoesExponencial = {
    0 : "Verificar se é crescente ou decrescente",
    1 : "Calcular função em x pedido",
    2 : "Gerar gráfico",
    3 : "Voltar"
};
equacaoExponencial = "f(x) = ab^x";
funcaoE = "A função é ";
decrescente = "decrescente";
crescente = "crescente";
linear = "linear";

def menu(stdscr):
    while 1:
        stdscr.clear();
        stdscr.addstr(titulo, curses.A_BOLD);
        stdscr.addstr(1, 0, opcoes[1], curses.A_BOLD);
        stdscr.addstr(2, 0, equacaoExponencial);
        stdscr.addstr(4, 0, valorParaA);
        curses.curs_set(1);
        curses.echo();
        a = stdscr.getstr(5,0).decode(encoding="utf-8");
        if(misc.isValidNumber(a)): 
            a = float(a);
            if a > 0: break;
    while 1:
        stdscr.clear();
        stdscr.addstr(titulo, curses.A_BOLD);
        stdscr.addstr(1, 0, opcoes[1], curses.A_BOLD);
        stdscr.addstr(2, 0, equacaoExponencial);
        stdscr.addstr(4, 0, valorParaB);
        curses.curs_set(1);
        curses.echo();
        b = stdscr.getstr(5,0).decode(encoding="utf-8");
        if(misc.isValidNumber(b)): 
            b = float(b);
            if b > 0: break;
    curses.curs_set(0);

    selecionado = 0;
    printMenu(stdscr, selecionado, a, b);
    while 1:
        key = stdscr.getch();
        if key == curses.KEY_UP:
            if selecionado > 0: selecionado-=1;
            else: selecionado = len(opcoesExponencial)-1;
        elif key == curses.KEY_DOWN:
            if selecionado < len(opcoesExponencial)-1: selecionado+=1;
            else: selecionado = 0;
        elif key == curses.KEY_ENTER or key in [10,13]:
            if(selecionado==0): verificarCrescenteDecrescente(stdscr, a, b);
            if(selecionado==1): calc(stdscr, a, b);
            if(selecionado==2): plot(a, b);
            elif(selecionado==3): return;
        printMenu(stdscr, selecionado, a, b);

    stdscr.refresh();

def calc(stdscr, a, b):
    while 1:
        stdscr.clear();
        stdscr.addstr(titulo, curses.A_BOLD);
        stdscr.addstr(1, 0, opcoes[1], curses.A_BOLD);
        stdscr.addstr(2, 0, formarEquacao(a,b));
        stdscr.addstr(3, 0, valorParaX);
        curses.curs_set(1);
        curses.echo();
        x = stdscr.getstr(4,0).decode(encoding="utf-8");
        if(misc.isValidNumber(x)): 
            x = float(x);
            break;
    if(x % 1 == 0): x = int(x);

    try:
        res = a*b**x;
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

def plot(a, b):
    x = np.linspace(-2, 2, 100);
    y = a*b**x;

    fig, ax = plt.subplots();
    ax.axhline(y=0, color="k");
    ax.axvline(x=0, color="k");
    plt.plot(x, y);
    ax.set_title(formarEquacao(a,b));
    plt.grid(True);
    plt.show();

def printMenu(stdscr, selecionado, a,b):
    stdscr.clear();
    stdscr.addstr(titulo, curses.A_BOLD);
    stdscr.addstr(1, 0, opcoes[1], curses.A_BOLD);
    stdscr.addstr(2, 0, formarEquacao(a,b));
    stdscr.addstr(3, 0, subtitulo);

    for i in opcoesExponencial:
        if(i==selecionado):
            stdscr.attron(curses.color_pair(1));
            stdscr.addstr(i+4, 0, "> "+opcoesExponencial[i]);
            stdscr.attroff(curses.color_pair(1));
        else:
            stdscr.addstr(i+4, 2, opcoesExponencial[i]);

def formarEquacao(a,b):
    if(a % 1 == 0): a = int(a);
    if(b % 1 == 0): b = int(b);
    return "f(x) = %s*%s^x"%(a,b);

def verificarCrescenteDecrescente(stdscr, a, b):
    stdscr.clear();
    stdscr.addstr(titulo, curses.A_BOLD);
    stdscr.addstr(1, 0, opcoes[1], curses.A_BOLD);
    stdscr.addstr(2, 0, formarEquacao(a,b));
    if b < 1: f =  decrescente;
    elif b == 1: f = linear;
    else : f = crescente;
    stdscr.addstr(3,0, funcaoE+f);

    stdscr.addstr(5, 0, enterVolta);
    while 1:
        key = stdscr.getch();
        if key == curses.KEY_ENTER or key in [10,13]:
            return; 
