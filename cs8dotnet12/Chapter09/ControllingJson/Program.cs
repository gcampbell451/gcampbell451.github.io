using Packt.Shared; // to use Book
using System.Security.Cryptography;
using System.Text.Json; // to use JsonSerializer

Book csharpBook = new(title:
    "C# 12 and .NET 8 - Modern Cross-Platform Development Fundamentals")
{
    Author = "Mark J Price",
    PublishDate = new(2023, 11, 14),
    Pages = 823,
    Created = DateTimeOffset.UtcNow,
};

JsonSerializerOptions options = new()
{
    IncludeFields = true, // includes all fields
    PropertyNameCaseInsensitive = true,
    WriteIndented = true,
    PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
};

string path = Combine(CurrentDirectory, "book.json");

using (Stream fileStream = File.Create(path))
{
    JsonSerializer.Serialize(utf8Json: fileStream, value: csharpBook, options);
}

WriteLine("**** File Info ****");
WriteLine($"File: {GetFileName(path)}");
WriteLine($"Path: {GetDirectoryName(path)}");
WriteLine($"Size {new FileInfo(path).Length:N0} DeriveBytes");
WriteLine("/-------------------");
WriteLine(File.ReadAllText(path));
WriteLine("------------------/");
