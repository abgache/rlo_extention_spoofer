#include <windows.h>
int main(void) {
    ShellExecuteA(NULL, "open", "C:\\Windows\\System32\\calc.exe", NULL, NULL, SW_SHOWNORMAL);
    return 0;}