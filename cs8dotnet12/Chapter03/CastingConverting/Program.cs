using static System.Convert; // to use the ToInt32 method
using static System.Console;
using System.Globalization; // to use CultureInfo

#region How negative numbers are represented in binary
/*
WriteLine("{0, 12} {1, 34}", "Decimal", "Binary");
WriteLine("{0, 12} {0, 34:B32}", int.MaxValue); 

for (int i = 8; i >= -8; i--)
{
    WriteLine("{0, 12} {0, 34:B32}", i);
}
WriteLine("{0, 12} {0, 34:B32}", int.MinValue);
*/
#endregion

#region Rounding numbers
/*
double g = 9.8;
int h = ToInt32(g); // a method of System.Convert
WriteLine($"g is {g} and h is {h}.");

double[,] doubles =
{
    { 9.49, 9.5, 9.51 },
    { 10.49, 10.5, 10.51 },
    { 11.49, 11.5, 11.51 },
    { 12.49, 12.5, 12.51 },
    { -9.49, -9.5, -9.51 },
    { -10.49, -10.5, -10.51 },
    { -11.49, -11.5, -11.51 },
    { -12.49, -12.5, -12.51 },

};

WriteLine($"| double | ToInt32 | double | ToInt32 | double | ToInt32 |");
for (int x = 0; x < 8; x++)
{
    for (int y = 0; y < 3; y++)
    {
        Write($"| {doubles[x, y],6} | {ToInt32(doubles[x, y]),7} ");
    }
    WriteLine("|");
}
WriteLine();

foreach (double n in doubles)
{
    WriteLine(format:
        "Math.Round({0}, 0, MidpointRounding.AwayFromZero) is {1}", n, Math.Round(n, 0, MidpointRounding.AwayFromZero));
}*/
#endregion

#region Converting types to string
/*
int number = 12;
bool boolean = true;
DateTime now = DateTime.Now;
object me = new();

WriteLine(number.ToString());   // WriteLine implicitly converts args to string, so invoking ToString() is unnecessary
WriteLine(boolean.ToString());
WriteLine(now.ToString());
WriteLine(me.ToString());
*/
#endregion

#region Converting from a binary object to a string
/*
// allocate an array of 128 bytes
byte[] binaryObject = new byte[128];

// populate the array with random bytes.
Random.Shared.NextBytes(binaryObject);

WriteLine("Binary Object as bytes:");
for (int index = 0; index < binaryObject.Length; index++)
{
    Write($"{binaryObject[index]:X2} ");
}
WriteLine(0);

// convert the array to Base 64 string and output as text.
string encoded = ToBase64String(binaryObject);
WriteLine($"Binary Object as Base64: {encoded}");
*/
#endregion

#region
/*
// set the current culture to make sure date parsing works
CultureInfo.CurrentCulture = CultureInfo.GetCultureInfo("en-US");

int friends = int.Parse("27");
DateTime birthday = DateTime.Parse("4 June 1980");
WriteLine($"I have {friends} friends to invite to my party.");
WriteLine($"My birthday is {birthday}.");
WriteLine($"My birthday is {birthday:D}.");
*/
#endregion
