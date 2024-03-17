#region Pattern matching with the if statement
/*
// add and remove the "" to change between string and int
object o = 3;
int j = 4;

if (o is int i)
{
    WriteLine($"{i} x {j} = {i * j}");
}
else
{
    WriteLine("o is not an int so it cannot multiply!");
}
*/
#endregion

#region Branching with the switch staetment
/*
int number = Random.Shared.Next(1, 7);
WriteLine($"My random number is {number}");

switch (number)
{
    case 1:
        WriteLine("One");
        break;

    case 2:
        WriteLine("Two");
        goto case 1;

    case 3: // multiple case section

    case 4:
        WriteLine("Three or Four");
        goto case 1;

    case 5:
        goto A_Label;

    default:
        WriteLine("Default");
        break;
}
WriteLine("After end of switch");
A_Label:
WriteLine($"After A_Label");
*/
#endregion

#region Pattern matching with the switch statement
/*
var animals = new Animal?[]
{
    new Cat { Name = "Karen", Born = new(2022, 8, 23), Legs = 4, IsDomestic = true },
    null,
    new Cat { Name = "Mufasa", Born = new(1994, 6, 12) },
    new Spider { Name = "Sid Vicious", Born = DateTime.Today, IsPoisonous = true },
    new Spider { Name = "Captain Furry", Born = DateTime.Today }
};

foreach (Animal? animal in animals)
{
    string message;

    switch (animal)
    {
        case Cat fourLeggedCat when fourLeggedCat.Legs == 4:
            message = $"The cat named {fourLeggedCat.Name} has four legs.";
            break;
        case Cat wildCat when wildCat.IsDomestic == false:
            message = $"The non-domestic cat is named {wildCat.Name}";
            break;
        case Cat cat:
            message = $"The cat is named {cat.Name}";
            break;
        default:
            message = $"{animal.Name} is a {animal.GetType().Name}";
            break;
        case Spider spider when spider.IsPoisonous:
            message = $"The {spider.Name} spider is poisonous. Run!";
            break;
        case null:
            message = "The animal is null.";
            break;
    }
    WriteLine($"switch statment: {message}");

    message = animal switch
    {
        Cat fourLeggedCat when fourLeggedCat.Legs == 4
            => $"The cat named {fourLeggedCat.Name} has four legs.",
        Cat wildCat when wildCat.IsDomestic == false
            => $"The non-domestic cat is named {wildCat.Name}",
        Cat cat
            => $"The cat is named {cat.Name}.",
        Spider spider when spider.IsPoisonous
            => $"The {spider.Name} spider is poisonous. Run!",
        null
            => "The animal is null.",
        _
            => $"{animal.Name} is a {animal.GetType().Name}."
    };
    WriteLine($"switch expression: {message}");
}
*/
#endregion

