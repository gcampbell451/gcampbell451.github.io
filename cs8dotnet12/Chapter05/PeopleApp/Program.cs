using Packt.Shared; // to use Person

ConfigureConsole();  // sets current culture ot US English.

Person bob = new();

#region Setting and outputting field values/ using object initializer syntax

bob.Name = "Bob Smith";

bob.Born = new DateTimeOffset(
    year: 1965, month: 12, day: 22,
    hour: 16, minute: 28, second: 0,
    offset: TimeSpan.FromHours(-5)); // US Eastern Standard Time

WriteLine(format: "{0} was born on {1:D}.", bob.Name, bob.Born);

Person alice = new()
{
    Name = "Alice Jones",
    Born = new(1998, 3, 7, 16, 28, 0, TimeSpan.Zero)
};

WriteLine(format:"{0} was born on {1:d}.", alice.Name, alice.Born);

# endregion

#region Storing a value/multiple values using an enum type

bob.FavoriteAncientWonder = WondersOfTheAncientWorld.StatueOfZeusAtOlympia;

WriteLine(format: "{0}'s favorite wonder is {1}. Its integer is {2}.", bob.Name, bob.FavoriteAncientWonder, (int)bob.FavoriteAncientWonder);

bob.BucketList = WondersOfTheAncientWorld.HangingGardensOfBabylon | WondersOfTheAncientWorld.MausoleumAtHalicarnassus;

WriteLine($"{bob.Name}'s bucket list is {bob.BucketList}.");

# endregion

#region Storing multiple values using collections

// works with all versions of C#.
Person alfred = new Person();
alfred.Name = "Alfred";
bob.Children.Add(alfred);

// works with C# 3 and later
bob.Children.Add(new Person { Name = "Bella" });

// works with C# 9 and later
bob.Children.Add(new() { Name = "Zoe" });

WriteLine($"{bob.Name} has {bob.Children.Count} children:");
foreach (Person child in bob.Children)
{
    WriteLine($"> {child.Name}");
}

#endregion

#region Making a field static

BankAccount.InterestRate = 0.012M; // store a shared value in static field

BankAccount jonesAccount = new();
jonesAccount.AccountName = "Mrs. Jones";
jonesAccount.Balance = 2400;
WriteLine(format: "{0} earned {1:C} interest.", jonesAccount.AccountName, jonesAccount.Balance * BankAccount.InterestRate);

BankAccount gerrierAccount = new();
gerrierAccount.AccountName = "Mrs. Gerrier";
gerrierAccount.Balance = 98;
WriteLine(format: "{0} earned {1:C} interest.", gerrierAccount.AccountName, gerrierAccount.Balance * BankAccount.InterestRate);

#endregion

#region Making a field constant

// constant fields are accessible via the type.
WriteLine($"{bob.Name} is a {Person.Species}.");

#endregion

#region Making a field read-only

// read-only fileds are accessible via the variable.
WriteLine($"{bob.Name} was born on {bob.HomePlanet}.");

#endregion
