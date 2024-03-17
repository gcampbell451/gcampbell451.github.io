int numberOfApples = 12;
decimal pricePerApple = 0.35M;

WriteLine(
    format: "{0} apples cost {1:C}",
    arg0: numberOfApples,
    arg1: pricePerApple * numberOfApples);

string formatted = string.Format(
    format: "{0} apples cost {1:C}",
    arg0: numberOfApples,
    arg1: pricePerApple * numberOfApples);

WriteLine(formatted);

WriteLine("{0} {1} lived in {2}.", "Roger", "Cevung", "Stockholm");

string applesText = "Apples";
int applesCount = 1234;
string bananasText = "Bananas";
int bananasCount = 56789;

WriteLine();

WriteLine(format: "{0, -10} {1,6}", "Name", "Count");
WriteLine(format: "{0, -10} {1,6:N0}", applesText, applesCount);
WriteLine(format: "{0, -10} {1,6:N0}", bananasText, bananasCount);


Write("Type your first name and press ENTER: ");
string? firstName = ReadLine();
Write("Type your age and press ENTER: ");
string age = ReadLine()!;
WriteLine($"Hello, {firstName}, you look good for {age}!");


Write("Press any key combination: ");
ConsoleKeyInfo key = ReadKey();
WriteLine();
WriteLine("Key: {0}, Char: {1}, Modifiers: {2}", key.Key, key.KeyChar, key.Modifiers);
