// define an alias for a dictionary with string key and string value
using StringDictionary = System.Collections.Generic.Dictionary<string, string>;
using System.Collections.Immutable; // to use ImmutableDictionary<T, T>
using System.Collections.Frozen; // to use FrozenDictionary<T, T>

#region Working with lists

// simple syntax for creating a list and addinng three items
List<string> cities = new();
cities.Add("London");
cities.Add("Paris");
cities.Add("Milan");

/* alternative syntax that is converted by compiler into the 3 calls above
 * LIst<string> cities = new() { "London", "Paris", "Milan" }; */

/* alternative syntax that passes an array of string values to AddRange method
 * List<string> cities = new();
 * cities.AddRange(new[] { "London", "Paris", "Milan" }); */
/*
OutputCollection("Initial list", cities);
WriteLine($"The first city is {cities[0]}.");
WriteLine($"The last city is {cities[cities.Count - 1]}.");

cities.Insert(0, "Sydney");
OutputCollection("After inserting Sydney at index 0", cities);

cities.RemoveAt(1);
cities.Remove("Milan");
OutputCollection("After removing two cities", cities);
*/
#endregion

#region Working with dictionaries

// declare a dictionary without the alias
// dictionary<string, string> keywords=  new();

// use the alias to declare the dictionary
StringDictionary keywords = new();

// add using named parameters
keywords.Add(key: "int", value: "32-bit integer data type");

// add using positional parameters
keywords.Add("long", "64-bit integer data type");
keywords.Add("float", "Single precision floating point number");
/*
 * alternative syntax; complier converts this to calls to Add method
 * Dictionary<string, string> keywords = new()
 * {
 *      { "int", "32-bit integer data type" },
 *      { "long", "64-bit integer data type" },
 *      { "float", "Single precision floating point number" }
 * };
 * */

/*
 * alternative syntax; complier converts this to calls to Add method
 * Dictionary<string, string> keywords = new()
 * {
 *      ["int"] = "32-bit integer data type",
 *      ["long"] = "64-bit integer data type",
 *      ["float"] = "Single precision floating point number",
 * };
 * */

OutputCollection("Dictionary keys", keywords.Keys);
OutputCollection("Dictionary Values", keywords.Values);

WriteLine("Keywords and their definitions:");
foreach (KeyValuePair<string, string> item in keywords)
{
    WriteLine($"  {item.Key}: {item.Value}");
}

// look up a value using a key
string key = "long";
WriteLine($"The definition of {key} is {keywords[key]}");

#endregion

#region Sets, stacks and queues

HashSet<string> names = new();

foreach (string name in new[] { "Adam", "Barry", "Charlie", "Barry" })
{
    bool added = names.Add(name);
    WriteLine($"{name} was added: {added}.");
}

WriteLine($"Names set: {string.Join(", ", names)}");


Queue<string> coffee = new();

coffee.Enqueue("Damir");  // front of the queue
coffee.Enqueue("Andrea");
coffee.Enqueue("Ronald");
coffee.Enqueue("Amin");
coffee.Enqueue("Irina"); // end of the queue

OutputCollection("Initial queue from front to back", coffee);

// server handles the net person in queue
string served = coffee.Dequeue();
WriteLine($"Served: {served}");

// server handles next person in queue
served = coffee.Dequeue();  
WriteLine($"Served: {served}");
OutputCollection("Current queue from front to back", coffee);

WriteLine($"{coffee.Peek()} is next in line.");
OutputCollection($"Current queue from front to back", coffee);


PriorityQueue<string, int> vaccine = new();

// add some people
// 1 = high priority people in their 70s or poor health
// 2 = medium priority e.g. middle-aged
// 3 = low priority e.g. teens and twenties

vaccine.Enqueue("Pamela", 1);
vaccine.Enqueue("Rebecca", 3);
vaccine.Enqueue("Juliet", 2);
vaccine.Enqueue("Ian", 1);

OutputPQ("Current queue for vaccination", vaccine.UnorderedItems);

WriteLine($"{vaccine.Dequeue()} has been vaccinated.");
WriteLine($"{vaccine.Dequeue()} has been vaccinated.");
OutputPQ("Current queue for vaccination", vaccine.UnorderedItems);

WriteLine($"{vaccine.Dequeue()} has been vaccinated.");

WriteLine("Adding Mark to queue with priority 2.");
vaccine.Enqueue("Mark", 2);

WriteLine($"{vaccine.Peek()} will be next to be vaccinated.");
OutputPQ("Current queue for vaccination", vaccine.UnorderedItems);


//UseDictionary(keywords);
//UseDictionary(keywords.AsReadOnly());
UseDictionary(keywords.ToImmutableDictionary());

ImmutableDictionary<string, string> immutableKeywords = keywords.ToImmutableDictionary();

// call the Add method with a return value
ImmutableDictionary<string, string> newDictionary = immutableKeywords.Add(
                                                                      key: Guid.NewGuid().ToString(),
                                                                      value: Guid.NewGuid().ToString());

OutputCollection("Immutable keywords dictionary", immutableKeywords);
OutputCollection("New keywords dictionary", newDictionary);

// creating a frozen colleciton has an overhead to perform the sometimes complex optimizaitons
FrozenDictionary<string, string> frozenKeywords = keywords.ToFrozenDictionary();

OutputCollection("Frozen keywords dictionary", frozenKeywords);

// lookups are faster in a frozen dictionary
WriteLine($"Define long: {frozenKeywords["long"]}");

#endregion

#region using indexes, ranges, and spans

string name1 = "Samantha Jones";

// getting the lengths of the first and last names
int lengthOfFirst = name1.IndexOf(" ");
int lengthOfLast = name1.Length - lengthOfFirst - 1;

// using Substring
string firstName = name1.Substring(0, lengthOfFirst);

string lastName = name1.Substring(name1.Length - lengthOfLast, lengthOfLast);

WriteLine($"First: {firstName}, Last: {lastName}");

// using Spans
ReadOnlySpan<char> nameAsSpan = name1.AsSpan();
ReadOnlySpan<char> firstNameSpan = nameAsSpan[0..lengthOfFirst];
ReadOnlySpan<char> lastNameSpan = nameAsSpan[^lengthOfLast..];

WriteLine($"First: {firstNameSpan}, Last: {lastNameSpan}");

#endregion
