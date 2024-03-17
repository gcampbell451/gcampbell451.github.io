class Animal // this is the base type for all animals
{
    public string? Name;
    public DateTime Born;
    public byte Legs;
}

class Cat : Animal // this is a subtype of animal
{
    public bool IsDomestic;
}

class Spider : Animal
{
    public bool IsPoisonous;
}
