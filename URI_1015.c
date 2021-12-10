#include <stdio.h>
#include <math.h>

int main()
{
    float x1, x2, p1, y1, y2, p2, distancia = 0;

    scanf("%f", &x1);
    scanf("%f", &y1);
    scanf("%f", &x2);
    scanf("%f", &y2);

    p1 = (x2 - x1);
    p2 = (y2 - y1);

    p1 = pow(p1, 2);
    p2 = pow(p2, 2);


    distancia = sqrt(p1 + p2);


    printf("%.4f\n", distancia);

    return 0;
}
