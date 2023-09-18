#ifndef _GENERAR_LABERINTO

#include <iostream>
#include <iterator>
#include <vector>
#include <fstream>
using namespace std;

int Numero_Filas();
int Numero_Columnas();
vector<vector<int>> Generar_Laberinto();


///Creamos una matriz de 15x15 para generar el laberinto
vector<vector<int>> Generar_Laberinto()
{
    //Variables
    ifstream Archivo;
    string Renglon;
    int Iterador = 0;

//Creando la matriz que contendrá los datos del documento
    vector<vector<int>> Matriz(Numero_Filas(), vector<int>()); // Un arreglo de N arreglos
    vector<int> Aux; //Almacenamos los números de cada fila

    Archivo.open("../Laberinto.txt", ios::in); //Abrimos el documento en modo lectura

    //Recorremos todas los renglones del documento hasta llegar al último
    while(!Archivo.eof())
    {
        if(!Aux.empty()) Aux.clear(); //Si el vector auxiliar no está vacío, lo vaciamos

        getline(Archivo, Renglon); //Copiamos el renglón actual del documento
        for(char i: Renglon)
            if(i != ',')
                Aux.push_back(i - 48); //Solo insertamos valores entre 0 y 1. Restamos 48 para convertir el caracter en entero

        Matriz[Iterador] = Aux; //Guardamos los elementos del vector auxiliar en la matriz
        Iterador++;
    }

    Archivo.close();

    //Mostramos el valor de la matriz
    /*
    for(short int i = 0; i < Filas; i++)
    {
        for(short int j = 0; j < Aux.size(); j++)
        {
            cout<< Matriz[i][j]<< " ";
        }
        cout<< endl;
    }
    */

    return Matriz;
}

///Obtenemos el número de renglones (filas) contenidas en el documento "Laberinto.txt"
int Numero_Filas()
{
    //Variables
    ifstream Archivo;
    string Aux;
    int FILAS = 0;

    Archivo.open("../Laberinto.txt", ios::in); //Abrimos el documento "Laberinto.txt"
    if(Archivo.fail()) cout<< "Error al abrir el archivo"<< endl;

    while(getline(Archivo, Aux)) FILAS++; //Contamos los saltos de líneas. Ignorar la función getline
    Archivo.close();

    return FILAS;
}

///Obtenemos el número de columnas contenidas en cada fila del documento "Laberinto.txt"
int Numero_Columnas()
{
    //Variables
    ifstream Archivo;
    string Aux;
    vector<int> Columnas;

    Archivo.open("../Laberinto.txt", ios::in); //Abrimos el documento "Laberinto.txt"
    if(Archivo.fail()) cout<< "Error al abrir el archivo"<< endl;

    getline(Archivo, Aux); //Copiamos el renglón actual del documento
    for(char i: Aux) // Nos importa contar el número de elementos que exista en Aux
        if(i != ',') Columnas.push_back(i); //Contamos los datos y los enviamos
    Archivo.close();

    return Columnas.size();
}


#endif
