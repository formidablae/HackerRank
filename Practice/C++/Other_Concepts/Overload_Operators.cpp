//Overload operators + and << for the class complex
//+ should add two complex numbers as (a+ib) + (c+id) = (a+c) + i(b+d)
//<< should print a complex number in the format "a+ib"

Complex operator + (Complex c1, Complex c2) 
{
    return {c1.a + c2.a, c1.b + c2.b };
}

ostream& operator << (ostream& os, const Complex& c)
{
    return os << c.a << (c.b > 0 ? '+' : '-') << 'i' << c.b;
}

