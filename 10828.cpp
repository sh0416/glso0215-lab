#include <iostream>
#include <stack>
#include <sstream>
#include <string>

int main()
{
    std::stack<int> myStack;

    int n;
    std::cin >> n;

    for (int i = 0; i < n; i++)
    {
        std::string input;
        std::string command;
        int value;

        std::getline(std::cin >> std::ws, input);

        std::istringstream iss(input);
        iss >> command >> value;
        
        if (command == "push") {
            myStack.push(value);
        }
        else if (command == "pop") {
            if (myStack.empty()) {
                std::cout << -1 << std::endl;
            }
            else {
                std::cout << myStack.top() << std::endl;
                myStack.pop();
            }   
        }
        else if (command == "size") {
            std::cout << myStack.size() << std::endl;
        }
        else if (command == "empty") {
            if (myStack.empty()) std::cout << 1 << std::endl;
            else std::cout << 0 << std::endl;
        }
        else if (command == "top") {
            if (myStack.empty()) {
                std::cout << -1 << std::endl;
            }
            else {
                std::cout << myStack.top() << std::endl;
            }   
        }
    }
}
