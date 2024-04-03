// ALL types in this file will be defined in this file-scoped namespace
namespace Packt.Shared;

public partial class Person : object
{
    #region Fields: Data or state for this person.

    public string? Name; // ? means it can be null.
    public DateTimeOffset Born;
    
    // this has been moved to PersonAutoGen.cs as a property
    // public WondersOfTheAncientWorld FavoriteAncientWonder;

    public WondersOfTheAncientWorld BucketList;
    public List<Person> Children = new();

    // constant fields, fixed at compilation
    public const string Species = "Homo Sapiens";

    // read-only fields, can be set at runtime
    public readonly string HomePlanet = "Earth";
    public readonly DateTime Instantiated;


    #endregion

    #region Initializing fields with constructors

    public Person()
    {
        // constructors can set default values for fields
        // including any read-only fileds like Instantiated
        Name = "Unknown";
        Instantiated = DateTime.Now;
    }

    public Person(string initialName, string homePlanet)
    {
        Name = initialName;
        HomePlanet = homePlanet;
        Instantiated = DateTime.Now;
    }

    #endregion

    #region Methods: Actions the type can perform

    public void WriteToConsole()
    {
        WriteLine($"{Name} was born on a {Born:dddd}.");
    }

    public string GetOrigin()
    {
        return $"{Name} was born on {HomePlanet}.";
    }

    public string SayHello()
    {
        return $"{Name} says 'Hello!'";
    }

    public string SayHello(string name)
    {
        return $"{Name} says 'Hello, {name}!'";
    }

    public string OptionalParameters(int count, string command = "Run!", double number = 0.0, bool active = true)
    {
        return string.Format(
            "command is {0}, number is {1}, active is {2}", command, number, active );
    }
  
    public void PassingParameters(int w, in int x, ref int y, out int z)
    {
        // out parameters cannot have a default and they must be initialized inside the method
        z = 100;

        // increment each parameter except the read-only x.
        w++;
        // x++; // gives a compiler error
        y++;
        z++;

        WriteLine($"In the method: w={w}, x={x}, y={y}, z={z}");
    }

    // method that returns a tuple: (string, int)
    public (string, int) GetFruit()
    {
        return ("Apples", 5);
    }

    // method that returns a tuple with named fields
    public (string Name, int Number) GetNamedFruit()
    {
        return ("Apples", 5);
    }

    // deconstructors: break down this object into parts, can have as many as want as long as they have diff signatures
    public void Deconstruct(out string? name, out DateTimeOffset dob)
    {
        name = Name;
        dob = Born;
    }

    public void Deconstruct(out string? name, out DateTimeOffset dob, out WondersOfTheAncientWorld fav)
    {
        name = Name;
        dob = Born;
        fav = FavoriteAncientWonder;
    }

    public static int Factorial(int number)
    {
        if (number < 0)
        {
            throw new ArgumentException($"{nameof(number)} cannot be less than zero.");
        }
        return localFactorial(number);

        int localFactorial(int localNumber) // local function
        {
            if (localNumber == 0) return 1;
            return localNumber * localFactorial(localNumber - 1);
        }
    }

 

    #endregion
}



