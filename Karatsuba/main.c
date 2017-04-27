#include "karatsuba.h"

int main(){

    intal *num1 = create_intal("+1587229839919605783299999942151299514241512519999125124213139");
    intal *num2 = create_intal("-1502725675504136130899999512411241299999995212424124142411252591");
    intal *res;

    printf("\nMULTIPLICATION of : %c%s * %c%s\n\n Result: \n",num1->sign, num1->num, num2->sign,num2->num );

    res = karatsuba(num1, num2);
    print_intal(res);

    delete_intal(&num1);
    delete_intal(&num2);
    delete_intal(&res);

}
