using System.Diagnostics.CodeAnalysis; // to use [SetsRequiredMembers]
namespace Packt.Shared;

public class Book
{
    // needs .NET 7 or later as well as C# 11 or later
    public required string? Isbn;
    public required string? Title;

    // works with any version of .NET
    public string? Author;
    public int PageCount;

    // constructor for use with object initializer syntax
    public Book() { }

    // constructor with parameters to set required fields
    [SetsRequiredMembers]
    public Book(string? isbn, string? title)
    {
        Isbn = isbn;
        Title = title;  
    }
}
