using Packt.Shared;
using System.Diagnostics.CodeAnalysis;

Person harry = new()
{
    Name = "Harry",
    Born = new(year: 2001, month: 3, day: 25,
               hour: 0, minute: 0, second: 0,
               offset: TimeSpan.Zero)
};

// harry.WriteToConsole();

#region Implementing functionality using methods

// Implementing functionality using methods
Person lamech = new() { Name = "Lamech" };
Person adah = new() { Name = "Adah" };
Person zillah = new() { Name = "Zillah" };

// call the instance method to marry Lamech and Adah.
lamech.Marry(adah);

// call the static method to marry Lamech and Zillah.
// Person.Marry(lamech, zillah);

if (lamech + zillah)
{
    WriteLine($"{lamech.Name} and {zillah.Name} successfully got married.");
}

lamech.OutputSpouses();
adah.OutputSpouses();
zillah.OutputSpouses();

// call the instance method to make a baby.
Person baby1 = lamech.ProcreateWith(adah);
baby1.Name = "Jabal";
WriteLine($"{baby1.Name} was born on {baby1.Born}.");

// call the static method to make a baby
Person baby2 = Person.Procreate(zillah, lamech);
baby2.Name = "Tubalcain";

// use the * operator to "multiply"
Person baby3 = lamech * adah;
baby3.Name = "Jubal";

Person baby4 = zillah * lamech;
baby4.Name = "Naamah";

adah.WriteChildrenToConsole();
zillah.WriteChildrenToConsole();
lamech.WriteChildrenToConsole();

for (int i = 0; i < lamech.Children.Count; i++)
{
    WriteLine(format: "   {0}'s child #{1} is named \"{2}\".",
        lamech.Name, i + 1, lamech.Children[i].Name);
}


#endregion

#region Working with non-generic types

// non-generic lookup collection
System.Collections.Hashtable lookupObject = new();
lookupObject.Add(1, "Alpha");
lookupObject.Add(2, "Beta");
lookupObject.Add(3, "Gamma");
lookupObject.Add(harry, "Delta");

int key = 2; // look up the value that has 2 as its key

WriteLine(format: "Key {0} has value: {1}", key, lookupObject[key]);

// look up the value that has harry as its key
WriteLine(format: "Key {0} has value: {1}", harry, lookupObject[harry]);


#endregion

#region Working with generic types

// define a generic lookup collection
Dictionary<int, string> lookupIntString = new();
lookupIntString.Add(1, "Alpha");
lookupIntString.Add(2, "Beta");
lookupIntString.Add(3, "Gamma");
lookupIntString.Add(4, "Delta");

key = 3;
WriteLine("Key {0} has value: {1}", key, lookupIntString[key]);

#endregion

#region Defining and handling delegates

// asign the method(s) to the Shout event delegate
harry.Shout += Harry_Shout;
harry.Shout += Harry_Shout_2;

// call the Poke method that eventually raises the Shout event
harry.Poke();
harry.Poke();
harry.Poke();
harry.Poke();


#endregion

#region Comparing objects when sorting

Person?[] people =
{
    null,
    new() { Name = "Simon" },
    new() { Name = "Jenny" },
    new() { Name = "Adam" },
    new() { Name = null },
    new() { Name = "Richard" }
};

OutputPeopleNames(people, "Initial list of people:");

Array.Sort(people);

OutputPeopleNames(people, "After sorting using Person's IComparable implementation: ");

#endregion

#region Comparing objects using a separate class

Array.Sort(people, new PersonComparer());

OutputPeopleNames(people, "After sorting using PersonComparer's IComparer implementation");

#endregion

#region Equality of types

int a = 3;
int b = 3;
WriteLine($"a: {a}, b: {b}");
WriteLine($"a == b: {a ==b}");

Person p1 = new() { Name = "Kevin" };
Person p2 = new() { Name = "Kevin" };
WriteLine($"p1: {p1}, p2: {p2}");
WriteLine($"p1.Name: {p1.Name}, p2.Name: {p2.Name}");
WriteLine($"p1 == p2: {p1 == p2}");

Person p3 = p1;
WriteLine($"p3: {p3}");
WriteLine($"p3.Name: {p3.Name}");
WriteLine($"p1 == p3: {p1 == p3}");

// string is the only class reference type implemented to 
// act like a value type for equality
WriteLine($"p1.Name: {p1.Name}, p2.Name : {p2.Name}");
WriteLine($"p1.Name == p2.Name: {p1.Name == p2.Name}");

#endregion

#region Defining struct types

DisplacementVector dv1 = new(3, 5);
DisplacementVector dv2 = new(-2, 7);
DisplacementVector dv3 = dv1 + dv2;

WriteLine($"({dv1.X}, {dv1.Y}) + ({dv2.X}, {dv2.Y}) = ({dv3.X}, {dv3.Y})");

DisplacementVector dv4 = new();
WriteLine($"({dv4.X}, {dv4.Y})");

DisplacementVector dv5 = new(3, 5);
WriteLine($"dv1.Equal(dv5): {dv1.Equals(dv5)}");
WriteLine($"dv1 == dv5: {dv1 == dv5}");

#endregion

#region Inheriting from classes

Employee john = new()
{
    Name = "John Jones",
    Born = new(1990, 7, 28, 0, 0, 0, offset: TimeSpan.Zero)
};

john.WriteToConsole();


#endregion

#region Extending clases to add functionality, hiding members

john.EmployeeCode = "JJ001";
john.HireDate = new(2014, 11, 23);
WriteLine($"{john.Name} was hired on {john.HireDate: yyyy-MM-dd}.");


#endregion

#region Overriding members

WriteLine(john.ToString());



#endregion

#region Understanding polymorphism

Employee aliceInEmployee = new()
{ Name = "Alice", EmployeeCode = "AA123" };

Person aliceInPerson = aliceInEmployee;
aliceInEmployee.WriteToConsole();
aliceInPerson.WriteToConsole();
WriteLine(aliceInEmployee.ToString());
WriteLine(aliceInPerson.ToString());

#endregion

#region Casting within inheritance hierarchies, using as to cast a type
if (aliceInPerson is Employee)
{
    WriteLine($"{nameof(aliceInPerson)} is an Employee.");

    Employee explicitAlice = (Employee)aliceInPerson;

    // explicitAlice can now be used without throwing an InvalidCastException
}

Employee? aliceAsEmployee = aliceInPerson as Employee;

if (aliceAsEmployee is not null)
{
    WriteLine($"{nameof(aliceInPerson)} as an Employee");

    // aliceAsEmployee can now be used without throwing a NullReferenceException
}


#endregion

#region Inheriting exceptions

try
{
    john.TimeTravel(when: new(1999, 12, 31));
    john.TimeTravel(when: new(1950, 12, 25));
}
catch (PersonException ex)
{
    WriteLine(ex.Message);
}

#endregion

#region extending types when you can't inherit

string email1 = "pamela@test.com";
string email2 = "ina&test.com";

WriteLine("{0} is a valid email address: {1}",
    email1, StringExtensions.IsValidEmail(email1));
WriteLine("{0} is a valid email address: {1}", 
    email2 , StringExtensions.IsValidEmail(email2));

WriteLine("{0} is a valid email address: {1}",
    email1, email1.IsValidEmail());
WriteLine("{0} is a valid email address: {1}",
    email2, email2.IsValidEmail());

#endregion

#region Mutablitiy and records

C1 c1 = new() { Name = "Bob" };
c1.Name = "Bill";

C2 c2 = new(Name: "Bob");
// c2.Name = "Bill";

S1 s1 = new() { Name = "Bob" };
s1.Name = "Bill";

S2 s2 = new(Name: "Bob");
s2.Name = "Bill";

S3 s3 = new(Name: "Bob");
// s3.Name = "Bill";

#endregion


