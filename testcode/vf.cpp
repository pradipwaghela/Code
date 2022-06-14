#include<iostream>
using namespace std;
class A{
public:
virtual  void display(){
    cout<<"This is base class"<<endl;
}
};
class B : public A{
public:
void display(){
    cout<<"This is derived class"<<endl;
}
};


int main(){
    A *b;//base class Pointer 
    B d;//Derived class object
    b=&d;//Derived class reference to base class
    b->display();
    return 0;
}
/**
 * @brief Virtul Function
 * Can not be static member 
 * Should be  member of  same class
 * Only using pointer 
 * must be define even u dont use
 * 
 */