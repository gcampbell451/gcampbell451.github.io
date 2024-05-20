using static System.Console;
using System.Text.RegularExpressions;


Write("Enter your age: ");
string input = ReadLine()!;
Regex ageChecker = DigitsOnly();
WriteLine(ageChecker.IsMatch(input) ? "Thank you!" : $"This is not a valid age: {input}");


string films = """
    "Monsters, Inc.", "I, Tonya", "Lock, Stock, and Two Smoking Barrels"
    """;

WriteLine($"Films to split: {films}");

string[] filmsDumb = films.Split(',');

WriteLine("Splitting with string.Split method: ");
foreach (string film in filmsDumb)
{
    WriteLine($"  {film}");
}
Regex csv = CommaSeparator();

MatchCollection filmsSmart = csv.Matches(films);

WriteLine("Splitting with regular expression:");
foreach (Match film in filmsSmart)
{
    WriteLine($"  {film.Groups[2].Value}");
}