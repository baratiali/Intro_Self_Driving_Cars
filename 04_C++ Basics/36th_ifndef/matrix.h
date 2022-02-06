/*
ifndef
In this case, you don't really need an ifndef statement because the code is simple. 
You have only written one class, so there isn't a way to mistakenly include another class multiple times. 
However, it's a good habit to write inclusion guards with an ifndef statement.

For this exercise, use the ifndef syntax to write an inclusion guard in the matrix.h file.
*/




#ifndef MATRIX_H
#define MATRIX_H

#include <vector>
#include <iostream>
#include <stdexcept>

class Matrix
{
    private:

        std::vector< std::vector<float> > grid;
        std::vector<float>::size_type rows;
        std::vector<float>::size_type cols;

    public:

        // constructor functions
        Matrix ();
        Matrix (std::vector< std::vector<float> >);

        // set functions
        void setGrid(std::vector< std::vector<float> >);

        // get functions
        std::vector< std::vector<float> > getGrid();
        std::vector<float>::size_type getRows();
        std::vector<float>::size_type getCols();

        // matrix functions
        Matrix matrix_transpose();
        Matrix matrix_addition(Matrix);

        // matrix printing
        void matrix_print();

};

#endif /* MATRIX_H */