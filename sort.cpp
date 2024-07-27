#include <iostream>
#include <algorithm>

int main() {
    int arr[5] = {5, 2, 8, 1, 3};
    
    int size = sizeof(arr) / sizeof(arr[0]);
    
    std::sort(arr, arr + size);
    for (int i = 0; i < size; ++i) {
        std::cout << arr[i] << " ";
    }
    return 0;
}