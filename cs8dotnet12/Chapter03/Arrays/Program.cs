﻿#region Working with multi-dimensional arrays
/*
string[,] grid1 =
{
    { "Alpha", "Beta", "Gamma", "Delta" },
    { "Anne", "Ben", "Charlie", "Doug" },
    { "Aardvark", "Bear", "Cat", "Dog" }
};

Console.WriteLine($"1st dimension, lower bound: {grid1.GetLowerBound(0)}");
Console.WriteLine($"1st dimension, upper bound: {grid1.GetUpperBound(0)}");
Console.WriteLine($"2nd dimension, lower bound: {grid1.GetLowerBound(1)}");
Console.WriteLine($"2nd dimension, upper bound: {grid1.GetUpperBound(1)}");

for (int row = 0; row <= grid1.GetUpperBound(0); row++)
{
    for (int col = 0; col <= grid1.GetUpperBound(1); col++)
    {
        Console.WriteLine($"Row {row}, Col {col}: {grid1[row, col]}");
    }
}
*/

#endregion

#region List pattern matching with arrays
int[] sequentialNumbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
int[] oneTwoNumbers = { 1, 2 };
int[] oneTwoTenNumbers = { 1, 2, 10 };
int[] oneTwoThreeTenNumbers = { 1, 2, 3, 10};
int[] primeNumbers = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 };
int[] fibonacciNumbers = {  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89};
int[] emptyNumbers = { };
int[] threeNumbers = { 9, 7, 5 };
int[] sixNumbers = { 9, 7, 5, 4, 2, 10 };

Console.WriteLine($"{nameof(sequentialNumbers)}: {CheckSwitch(sequentialNumbers)}");
Console.WriteLine($"{nameof(oneTwoNumbers)}: {CheckSwitch(oneTwoNumbers)}");
Console.WriteLine($"{nameof(oneTwoTenNumbers)}: {CheckSwitch(oneTwoTenNumbers)}");
Console.WriteLine($"{nameof(oneTwoThreeTenNumbers)}: {CheckSwitch(oneTwoThreeTenNumbers)}");
Console.WriteLine($"{nameof(primeNumbers)}: {CheckSwitch(primeNumbers)}");
Console.WriteLine($"{nameof(fibonacciNumbers)}: {CheckSwitch(fibonacciNumbers)}");
Console.WriteLine($"{nameof(emptyNumbers)}: {CheckSwitch(emptyNumbers)}");
Console.WriteLine($"{nameof(threeNumbers)}: {CheckSwitch(threeNumbers)}");
Console.WriteLine($"{nameof(sixNumbers)}: {CheckSwitch(sixNumbers)}");

static string CheckSwitch(int[] values) => values switch
{
    [] => "Empty array",
    [1, 2, _, 10] => "Contains 1, 2, any single number, 10.",
    [1, 2, .., 10] => "Contains 1, 2, any range including empty, 10.",
    [1, 2] => "Contains 1 then 2.",
    [int item1, int item2, int item3] => $"Contains {item1} then {item2} then {item3}",
    [0, _] => "Starts with 0, then one other number.",
    [0, ..] => "Starts with 0, then any range of numbers.",
    [2, .. int[] others] => $"Starts with 2, then {others.Length} more numbers.",
    [..] => "Any items in any order.",
};
#endregion