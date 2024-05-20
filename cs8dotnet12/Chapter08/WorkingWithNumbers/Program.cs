﻿using System.Numerics; // to use BigInteger

#region Working with big integers and complex numbers

const int width = 40;

WriteLine("ulong.MaxValue vs a 30-digit BigInteger");
WriteLine(new string('-', width));

ulong big = ulong.MaxValue;
WriteLine($"{big,width:N0}");

BigInteger bigger = BigInteger.Parse("123456789012345678901234567890");
WriteLine($"{bigger,width:N0}");

Complex c1 = new(real: 4, imaginary: 2);
Complex c2 = new(real: 3, imaginary: 7);
Complex c3 = c1 + c2;

// output using the default ToString implementation
WriteLine($"{c1} added to {c2} is {c3}");

// output using a custom format
WriteLine("{0} + {1}i added to {2} + {3}i is {4} + {5}i",
    c1.Real, c1.Imaginary,
    c2.Real, c2.Imaginary,
    c3.Real, c3.Imaginary);

#endregion

#region Generating random numbers and GUIDs

Random r = Random.Shared;

// minValue is an inclusive lower bound, maxValue is an exclusive upper bound
int dieRoll = r.Next(1, 7);
WriteLine($"Random die roll: {dieRoll}");

double randomReal = r.NextDouble(); // returns 0.0 <= rand < 1.0
WriteLine($"Random double: {randomReal}");

byte[] arrayOfBytes = new byte[256];
r.NextBytes(arrayOfBytes); // fills array with 256 random bytes
Write("Random bytes: ");
for (int i = 0; i < arrayOfBytes.Length; i++)
{
    Write($"{arrayOfBytes[i]:X2} ");
}
WriteLine();

string[] beatles = r.GetItems(
    choices: new[] { "John", "Paul", "George", "Ringo" },
    length: 10);

Write("Random ten beatles:"); 
foreach (string beatle in beatles) 
{
    Write($" {beatle}");
}
WriteLine();

r.Shuffle(beatles);

Write("Shuffled beatles:");
foreach (string beatle in beatles)
{
    Write($" {beatle}");
}
WriteLine();

WriteLine($"Empty GUID: {Guid.Empty}.");
Guid g = Guid.NewGuid();
WriteLine($"Random GUID: {g}.");

byte[] guidAsBytes = g.ToByteArray();
Write("GUID as byte array: ");
for (int i = 0;i < guidAsBytes.Length;i++)
{
    Write($"{guidAsBytes[i]:X2} ");
}
WriteLine();

#endregion



