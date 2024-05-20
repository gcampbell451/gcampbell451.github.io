﻿using System.Text.Json.Serialization; // to use [JsonInclude]

namespace Packt.Shared;

public class Book
{
    // constructor to set non-nullable property
    public Book(string title)
    {
        Title = title;
    }

    // properties
    public string Title { get; set; }
    public string? Author { get; set; }

    // fields
    [JsonInclude] // include this field
    public DateTime PublishDate;
    [JsonInclude]
    public DateTimeOffset Created;

    public ushort Pages;
}
