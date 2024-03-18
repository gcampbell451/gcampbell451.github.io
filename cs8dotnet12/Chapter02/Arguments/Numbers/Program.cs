uint naturalNumber = 23;
float realNumber = 2.3f;


int decimalNotation = 2_000_000;
int binaryNotation = 0b_0001_1110_1000_0100_1000_0000;
int hexadecimalNotation = 0x_001E_8480;

// check the 3 variables have the ame value
WriteLine($"{decimalNotation == binaryNotation}");
WriteLine($"{decimalNotation == hexadecimalNotation}");

// output the variable values in decimal
WriteLine($"{decimalNotation:N0}");
WriteLine($"{binaryNotation:N0}");
WriteLine($"{hexadecimalNotation:N0}");

// output the variable values in hexadecimal
WriteLine($"{decimalNotation:X}");
WriteLine($"{binaryNotation:X}");
WriteLine($"{hexadecimalNotation:X}");

// output the variable values in binary
WriteLine($"{decimalNotation:B}");
WriteLine($"{binaryNotation:B}");
WriteLine($"{hexadecimalNotation:B}");


WriteLine($"int uses {sizeof(int)} bytes and can store numbers in the range {int.MinValue:N0} to {int.MaxValue:N0}");
WriteLine($"double uses {sizeof(double)} bytes and can store numbers in the range {double.MinValue:N0} to {double.MaxValue:N0}");
WriteLine($"decimal uses {sizeof(decimal)} bytes and can store numbers in the range {decimal.MinValue:N0} to {decimal.MaxValue:N0}");

WriteLine("Using doubles: ");
double a = 0.1;
double b = 0.2;
if (a + b == 0.3)
{
    WriteLine($"{a} + {b} equals {0.3}");
}
else
{
    WriteLine($"{a} + {b} does NOT equal {0.3}");
}

WriteLine("Using decimals: ");
decimal c = 0.1M;
decimal d = 0.2M;
if (c + d == 0.3M)
{
    WriteLine($"{c} + {d} equals {0.3M}");
}
else
{
    WriteLine($"{c} + {d} does NOT equal {0.3M}");
}
object height = 1.88; // storing a double in an object
object name = "Amir"; // storing an string in an object
WriteLine($"{name} is {height} metres tall.");

//int length1 = name.Length; // this gives a compile error
int length2 = ((string)name).Length; // cast name to a string
WriteLine($"{name} has {length2} characters.");

dynamic something;

/// sotring an array of int values ina dynameic object.
// an array of any type has a Length property
something = new[] { 3, 5, 7 };

// storing an int in a dynamic object
// int does not have a Length property
something = 12;

// storing a string in a dynamic object
// string has a Length property
something = "Ahmed";

// this compiles but may throw an exception at runtime
WriteLine($"The length of something is {something.Length}");

// output the type of the something variable
WriteLine($"something is a {something.GetType()}");

var population = 67_000_000;
var weight = 1.88;
var price = 4.99M;
var fruit = "Apples";
var letter = 'Z';
var happy = true;


WriteLine($"default(int) = {default(int)}");
WriteLine($"default(bool) = {default(bool)}");
WriteLine($"default(DateTime) = {default(DateTime)}");
WriteLine($"default(string) = {default(string)}");

int number = 13;
WriteLine($"number set to: {number}");
number = default;
WriteLine($"number set to: {number}");



