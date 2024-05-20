using System.Xml.Serialization; // to use XmlSerializer
using FastJson = System.Text.Json.JsonSerializer; // alias to avoid naming conflicts
using Packt.Shared; // to use Person


#region Serializing as XML, Generating compact XML
List<Person> people = new()
{
    new(initialSalary: 20_000M)
    {
        FirstName = "Alice",
        LastName = "Smith",
        DateOfBirth = new(1974, 3, 14)
    },
    new(initialSalary: 40_000M)
    {
        FirstName = "Bob",
        LastName = "Jones",
        DateOfBirth = new(1969, 11, 23)
    },
    new(initialSalary: 20_000M)
    {
        FirstName = "Charlie",
        LastName = "Cox",
        DateOfBirth = new(1984, 5, 4),
        Children = new()
        {
            new(initialSalary: 0M)
            {
                FirstName = "Sally",
                LastName = "Cox",
                DateOfBirth = new(2012, 7, 12)
            }
        }
    }
};

SectionTitle("Serializing as XML");

// create serializer to format a "List of Person" as XML
XmlSerializer xs = new(type: people.GetType());

// create a file to write to 
string path = Combine(CurrentDirectory, "people.xml");

using (FileStream stream = File.Create(path))
{
    // serialize the object graph to the stream
    xs.Serialize(stream, people);
}// closes the stream

OutputFileInfo(path);

#endregion

#region Deserializing XML files

SectionTitle("Deserializing XML files");

using (FileStream xmlLoad = File.Open(path, FileMode.Open))
{
    // deserialize and cast the object graph into a "List of Person"
    List<Person>? loadedPeople =
        xs.Deserialize(xmlLoad) as List<Person>;

    if (loadedPeople is not null)
    {
        foreach (Person p in loadedPeople)
        {
            WriteLine("{0} has {1} children.",
                p.LastName, p.Children?.Count ?? 0);
        }
    }
}

#endregion

#region Serializing with JSON

SectionTitle("Serializing with JSON");

// create a file to write to
string jsonPath = Combine(CurrentDirectory, "people.json");

using (StreamWriter jsonStream = File.CreateText(jsonPath))
{
    Newtonsoft.Json.JsonSerializer jss = new();

    // serialize the object graph into a string
    jss.Serialize(jsonStream, people);
} // closes the file stream and releases resources

OutputFileInfo(jsonPath);

SectionTitle("Deserializing JSON files");

await using (FileStream jsonLoad = File.Open(jsonPath, FileMode.Open))
{
    // deserialize object graph into a "list of person"
    List<Person>? loadedPeople =
        await FastJson.DeserializeAsync(utf8Json: jsonLoad,
           returnType: typeof(List<Person>)) as List<Person>;

    if (loadedPeople is not null)
    {
        foreach (Person p in loadedPeople)
        {
            WriteLine("{0} has {1} children.",
                p.LastName, p.Children?.Count ?? 0);
        }
    }
}

#endregion
