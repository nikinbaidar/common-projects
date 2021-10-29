# include <iostream>
# include <stdlib.h>

using namespace std ;

class CubeDemo {
    public:
        int side;

        // constructor declaration
        CubeDemo() {
            side = 6;
        }

        // destructor declaration
        ~CubeDemo() {
            cout << "Destructor called \n";
        }

        int variable = 8;

    private:
};

int main() {

    // object creation

    CubeDemo cube;

    cout << cube.variable;

    return 0;
}
