#include "hamming.h"
#include <string.h>

int compute(const char *lhs, const char *rhs) {
    int n = strlen(lhs);
    int m = strlen(rhs);
    if (n != m)
        return -1;
    int distance = 0;
    for (int i = 0; i < n; i++)
        if (lhs[i] != rhs[i])
            distance++;
    return distance;
}