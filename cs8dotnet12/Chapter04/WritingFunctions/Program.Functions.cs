﻿using static System.Console;
using System.Globalization;
using System.Diagnostics; // to use CultureInfo
partial class Program
{
    static void TimesTable(byte number, byte size = 12)
    {
        WriteLine($"This is the {number} times table with {size} rows:");
        WriteLine();

        for (int row = 1; row <= size; row++)
        {
            WriteLine($"{row} x {number} = {row * number}");
        }
        WriteLine();
    }

    static decimal CalculateTax(decimal amount, string twoLetterRegionCode)
    {
        decimal rate = twoLetterRegionCode switch
        {
            "CH" => 0.08M, // Switzerland
            "DK" or "NO" => 0.25M, // Denmark, Norway
            "GB" or "FR" => 0.2M, // UK, France
            "HU" => 0.27M, // Hungary
            "OR" or "AK" or "MT" => 0.0M, // Oregon, Alaska, Montana
            "ND" or "WI" or "ME" or "VA" => 0.05M, // North Dakota, Wisconsin, Maine, Virginia
            "CA" => 0.0825M, // California
            _ => 0.06M // Most other states
        };

        return amount * rate;
    }

    static void ConfigureConsole(string culture = "en-US", bool useComputerCulture = false)
    {
        // to enable Unicode characters like Euro symbol in the console
        OutputEncoding = System.Text.Encoding.UTF8;

        if (!useComputerCulture)
        {
            CultureInfo.CurrentCulture = CultureInfo.GetCultureInfo(culture);
        }
        WriteLine($"CurrentCulture: {CultureInfo.CurrentCulture.DisplayName}");
    }

    /// <summary>
    /// Pass a 32-bit unsighned integer and it will be converted into its
    /// ordinal equivalent.
    /// </summary>
    /// <param name="number"></param> Number as a cardinal value, e.g. 1, 2, 3, etc.
    /// <returns></returns> Number as an ordinal value, e.g. 1st, 2nd, 3rd, etc.
    static string CardinalToOrdinal(uint number)
    {
        uint lastTwoDigits = number % 100;

        switch (lastTwoDigits)
        {
            case 11: // special cases for 11th to 13th
            case 12:
            case 13:
                return $"{number:N0}th";
            default:
                uint lastDigit = number % 10;

                string suffix = lastDigit switch
                {
                    1 => "st",
                    2 => "nd",
                    3 => "rd",
                    _ => "th",
                };

                return $"{number:N0}{suffix}";
        }
    }

    static int Factorial(int number)
    {
        if (number < 0)
        {
            throw new ArgumentOutOfRangeException(message: $"The factorial function is defined for non-negative integers only. Input: {number}", paramName: nameof(number));
        }
        else if (number == 0)
        {
            return 1;
        }
        else
        {
            checked // for overflow
            {
                return number * Factorial(number - 1);
            }
            
        }
    }

    static void RunFactorial()
    {
        for (int i = -2; i <=15; i++)
        {
            try
            {
                WriteLine($"{i}! = {Factorial(i):N0}");
            }
            catch (OverflowException)
            {
                WriteLine($"{i}! is too big for a 32-bit integer.");
            }
            catch (Exception ex)
            {
                WriteLine($"{i}! throws {ex.GetType()}: {ex.Message}");
            }
            
        }
    }

}
