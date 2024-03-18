using System.Reflection;    // to use Assembly, TypeName, etc.

// declare some unused variables useing tyes in additional assemblies 
// to make them load as well
System.Data.DataSet ds = new();
HttpClient client = new();

// get the assembly that is the entry point for this app
Assembly? myApp = Assembly.GetEntryAssembly();

// if the previous line returned nothing then end the app
if (myApp is null) return;

// loop throught he assemblies that myApp references
foreach(AssemblyName name in myApp.GetReferencedAssemblies())
{
    // load the assembly so we can read its details
    Assembly a = Assembly.Load(name);

    // declare a variable to count the number of methods
    int methodCount = 0;

    // loop through all the types in the assembly
    foreach (TypeInfo t in a.DefinedTypes)
    {
        // add up the counts of all the methods
        methodCount += t.GetMethods().Length;
    }

    // output the count of types and their methods
    Console.WriteLine("{0:N0} types with {1:N0} methods in {2} assembly.",
        arg0: a.DefinedTypes.Count(),
        arg1: methodCount,
        arg2: name.Name);
}

