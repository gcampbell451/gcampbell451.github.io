// ALL types in this file will be defined in this file-scoped namespace
namespace Packt.Shared;

public class Person : object
{
    #region Fields: Data or state for this person.

    public string? Name; // ? means it can be null.
    public DateTimeOffset Born;
    public WondersOfTheAncientWorld FavoriteAncientWonder;
    public WondersOfTheAncientWorld BucketList;
    public List<Person> Children = new();

    // constant fields, fixed at compilation
    public const string Species = "Homo Sapiens";

    // read-only fields, can be set at runtime
    public readonly string HomePlanet = "Earth";

    #endregion

}
