# O código utiliza a biblioteca curses, que vem por padrão no Python para Linux ou MacOS
# No Windows pode ser instalado através do seguinte comando
# pip install windows-curses
# Ou encontrado no seguinte repositório
# https://github.com/zephyrproject-rtos/windows-curses

# O programa não irá ser executado corretamente em terminal de IDE como o Visual Studio Code
# Para executar o programa basta abrir um terminal (como o cmd) e executar o seguinte comando
# python main.py
# Ou abrir o arquivo start.bat que está sendo enviado junto ao código.

import curses;
import misc;
import exponencial;
import segundoGrau;
import matriz;

titulo = misc.titulo;
subtitulo = misc.subtitulo;
opcoes = misc.opcoes;

def printMenu(stdscr, selecionado):
    stdscr.clear();
    stdscr.addstr(titulo, curses.A_BOLD);
    stdscr.addstr(1, 0, subtitulo);

    for i in opcoes:
        if(i==selecionado):
            stdscr.attron(curses.color_pair(1));
            stdscr.addstr(i+2, 0, "> "+opcoes[i]);
            stdscr.attroff(curses.color_pair(1));
        else:
            stdscr.addstr(i+2, 2, opcoes[i]);

def main(stdscr):
    curses.curs_set(0);
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE);

    selecionado = 0;
    printMenu(stdscr, selecionado);
    while 1:
        key = stdscr.getch();
        if key == curses.KEY_UP:
            if selecionado > 0: selecionado-=1;
            else: selecionado = len(opcoes)-1;
        elif key == curses.KEY_DOWN:
            if selecionado < len(opcoes)-1: selecionado+=1;
            else: selecionado = 0;
        elif key == curses.KEY_ENTER or key in [10,13]:
            if(selecionado==0):
                while 1:
                    segundoGrau.menu(stdscr);
                    break;
            if(selecionado==1):
                while 1:
                    exponencial.menu(stdscr);
                    break;
            if(selecionado==2):
                while 1:
                    matriz.menu(stdscr);
                    break;
            if(selecionado==3): break;
        printMenu(stdscr, selecionado);

    stdscr.refresh();

curses.wrapper(main);