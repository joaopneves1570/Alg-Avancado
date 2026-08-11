#include <iostream>
#include <vector>

using namespace std;

template <typename T1, typename T2>
T1 add(T1 a, T2 b) {
    return a + b;
}

class NossoFunctor {
    public:

        NossoFunctor(int i_) : 

        int incrementa(){
            i++;
            return i;
        }

        int operator()() {
            return incrementa();
        }

        NossoFunctor operator+(NossoFunctor b) {
            return NossoFunctor(i - b.i);
        }

        bool operator<=(NossoFunctor b) {
            return (a + b).i < 0
        }
};

struct GreaterThan{
    bool operator()(int a, int b){
        return a > b;
    }
};


int main() {

    int i = 0;
    cout << "Hello W" << i << "rld!" << endl;

    //template
    vector<int> vetor = {1, 2, 3, 4, 5};

    cout << add(1, 2.5) << endl;
    cout << add(2.5, 1) << endl;

    //functors
    NossoFunctor diversao = NossoFunctor();
    diversao();
    diversao();
    diversao();
    diversao();
    cout << diversao() << endl;

    for (vector<int>::iterator it = vetor.begin(); it < vetor.end(); it++){
        cout << *it << endl;
    }
}