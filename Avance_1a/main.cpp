#include <iostream>
#include <windows.h>
#include <vector>
#include <SFML/Graphics.hpp>
#include "GenerarLaberinto.h"

void Agregar_Fila_Columna(sf::RenderWindow *Ventana);
void Agregar_Texto_tabla(sf::RenderWindow *Ventana);
void Dibujar_laberinto(sf::RenderWindow *Ventana);
void Generar_Cuadricula(sf::RenderWindow *Ventana);
void Movimiento(sf::RenderWindow *Ventana, int *X, int *Y);

using namespace sf;

int main()
{
    //Obtenemos datos importantes del documento "Laberinto.txt"
    //Cordenadas iniciales
    int X = 3;
    int Y = 10;
    int Filas = Numero_Filas();
    int Columnas = Numero_Columnas();
    vector<vector<int>> Matriz = Generar_Laberinto(); //Matriz numérica del documento "Laberinto.txt"

    RenderWindow Ventana(VideoMode(1000, 1000), "Laberinto"); // Creación de la ventana

    //Abriendo la ventana
    while (Ventana.isOpen())
    {
        Event evento;
        while (Ventana.pollEvent(evento))
        {
            if (evento.type == Event::Closed)
            {
                Ventana.close();
            }
        }

        // Borra la Ventana
        Ventana.clear();


    //Creación del laberinto
        //Variables
        const int Tamano_cuadro = 50;


        Agregar_Fila_Columna(&Ventana);
        Agregar_Texto_tabla(&Ventana);
        Dibujar_laberinto(&Ventana);
        Generar_Cuadricula(&Ventana);



        Movimiento(&Ventana, &X, &Y);

        // Muestra la Ventana en pantalla
        Ventana.display();
    }


    return 0;
}


///Dibujamos la fila y columna verde
void Agregar_Fila_Columna(sf::RenderWindow *Ventana)
{
    //Variables
    int Filas = Numero_Filas();
    const int Tamano_cuadro = 50;
    RectangleShape Fondo(Vector2f(1000, 1000));
    RectangleShape Cuadro_Eje_Y(Vector2f(Tamano_cuadro, Tamano_cuadro));
    RectangleShape Cuadro_Eje_X(Vector2f(Tamano_cuadro, Tamano_cuadro));

    //Colocando fondo blanco
    Fondo.setPosition(0, 0);
    Fondo.setFillColor(sf::Color:: White);
    Ventana->draw(Fondo);

    Cuadro_Eje_Y.setFillColor(sf::Color(35, 155, 86));
    Cuadro_Eje_X.setFillColor(sf::Color(35, 155, 86));


    //FInsertando en la tabla la fila y columna verde
    for(unsigned short int i = 0; i < Filas + 1; i++)
    {
        Cuadro_Eje_Y.setPosition(0, Tamano_cuadro*i);
        Cuadro_Eje_X.setPosition(Tamano_cuadro*i, 0);

        Ventana->draw(Cuadro_Eje_Y);
        Ventana->draw(Cuadro_Eje_X);
    }
}

///Agregamos caracteres a la tabla
void Agregar_Texto_tabla(sf::RenderWindow *Ventana)
{
    //Variables
    int Filas = Numero_Filas();
    int Tamano_cuadro = 50;
    Font Fuente;
    sf:: Text Texto_Columna_X;
    sf:: Text Texto_Columna_Y;
    vector<char> Caracter = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'L', 'O'};

    Fuente.loadFromFile("../arial/arial.ttf"); //Cargamos la fuente

    //Texto de la tabla
    Texto_Columna_X.setFillColor(sf::Color::Black);
    Texto_Columna_Y.setFillColor(sf::Color::Black);

    Texto_Columna_X.setCharacterSize(24);
    Texto_Columna_Y.setCharacterSize(24);

    Texto_Columna_X.setFont(Fuente);
    Texto_Columna_Y.setFont(Fuente);

    //Ingresamos caracteres
    for(unsigned short int i = 0; i < Filas; i++)
    {
        Texto_Columna_X.setString(Caracter[i]);
        Texto_Columna_Y.setString(to_string(Caracter[i] - 64));

        if(i == 0) Texto_Columna_X.setPosition(67, 10);
        else Texto_Columna_X.setPosition( Tamano_cuadro*(1 + i + 0.4), 10);

        if(i < 9) Texto_Columna_Y.setPosition(18, Tamano_cuadro*(1 + i + 0.3));
        else Texto_Columna_Y.setPosition(12, Tamano_cuadro*(1 + i + 0.3));

        Ventana->draw(Texto_Columna_X);
        Ventana->draw(Texto_Columna_Y);
    }
}

///Creamos el laberinto a partir de las coordenadas generadas de la matriz [#]
void Dibujar_laberinto(sf::RenderWindow *Ventana)
{
    //Obtenemos datos importantes del documento "Laberinto.txt"
    int Filas = Numero_Filas();
    int Columnas = Numero_Columnas();
    vector<vector<int>> Matriz = Generar_Laberinto(); //Matriz numérica del documento "Laberinto.txt" [#]
    const int Tamano_cuadro = 50;

    // Dibuja la matriz de cuadrados
    for (int i = 0; i < Filas; i++)
    {
        for (int j = 0; j < Columnas; j++)
        {
            RectangleShape cuadro(Vector2f(Tamano_cuadro, Tamano_cuadro));
            cuadro.setPosition(Tamano_cuadro*(1 + j), Tamano_cuadro*(1 + i));

            if(Matriz[i][j] == 0) cuadro.setFillColor(Color(52, 73, 94)); // Cuadros grises en 0
            else cuadro.setFillColor(Color:: White); // Ingresando color blanco en 1

            Ventana-> draw(cuadro);
        }
    }
}

void Generar_Cuadricula(sf::RenderWindow *Ventana)
{
    //Obtenemos datos importantes del documento "Laberinto.txt"
    const int Tamano_cuadro = 50;
    int Filas = Numero_Filas();
    int Columnas = Numero_Columnas();
    vector<vector<int>> Matriz = Generar_Laberinto(); //Matriz numérica del documento "Laberinto.txt" [#]

    //Cuadriculado
    for(int i = 0; i < Filas; i++)
    {
        for(int j = 0; j < Columnas; j++)
        {
            // Crea un cuadro en la posición actual
            RectangleShape Contorno(Vector2f(Tamano_cuadro, Tamano_cuadro));
            Contorno.setPosition(Tamano_cuadro*(1 + j), Tamano_cuadro*(1 + i));

            if(Matriz[i][j] == 0)
            {
                Contorno.setOutlineThickness(2);
                Contorno.setFillColor(Color::Transparent);
            }

            else
            {
                Contorno.setPosition(Tamano_cuadro*(1 + j) + 0.1, Tamano_cuadro*(1 + i) + 0.1);
                Contorno.setOutlineThickness(0.8);
                Contorno.setOutlineColor(Color::Black);
                Contorno.setFillColor(Color::Transparent);
            }

            Ventana-> draw(Contorno);
        }
    }
}

void Movimiento(sf::RenderWindow *Ventana, int *X, int *Y)
{
    int Tamano_cuadro = 50;
    vector<vector<int>> Matriz = Generar_Laberinto(); //Matriz numérica del documento "Laberinto.txt" [#]


    // Crea un cuadro en la posición actual
    RectangleShape Contorno(Vector2f(Tamano_cuadro, Tamano_cuadro));
    Contorno.setOutlineThickness(0.6);
    Contorno.setOutlineColor(Color::Red);
    Contorno.setFillColor(Color::Black);

    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
    {
        if(*X > 0 && Matriz[*Y][*X - 1] == 1) *X = *X - 1;
    }

    if(sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
    {
        if(*X < 14 && Matriz[*Y][*X + 1] == 1) *X = *X + 1;
    }

    if(sf::Keyboard::isKeyPressed(sf::Keyboard::Up))
    {
        if(*Y > 0 && Matriz[*Y - 1][*X] == 1) *Y = *Y - 1;
    }

    if(sf::Keyboard::isKeyPressed(sf::Keyboard::Down))
    {
        if(*Y < 14 && Matriz[*Y + 1][*X] == 1) *Y = *Y + 1;
    }




    Contorno.setPosition(Tamano_cuadro*(1 + *X) + 0.2, Tamano_cuadro*(1 + *Y) + 0.2);



    Ventana-> draw(Contorno);
    char x = *X + 65;

    cout<<"[" <<x <<", "<< *Y + 1<<" ]" << endl;
    Sleep(80);
}

