using System.Text.RegularExpressions; // to use regex

namespace Packt.Shared;

public static class StringExtensions
{
    public static bool IsValidEmail(this string input)
    {
        // use a simple regex to check that the input string is a valid email

        return Regex.IsMatch(input,
            @"[a-zA-Z0-9\.-_]+@[a-zA-Z0-9\._]+");
    }
}
