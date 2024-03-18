using System.ComponentModel;

double a = 4.5;
double b = 2.5;
double answer = Add(a, b);

WriteLine($"{a} + {b} = {Add(a, b)}");
WriteLine("Press Enter to end the app.");
ReadLine(); // wait for user to press enter


double Add(double a, double b)
{
    return a * b;  // deliberate bug
}
