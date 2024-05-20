using System.Globalization; // to use CultureInfo
using System.Reflection; // to use AssemblyName
using System.Reflection.Emit; // to use AssemblyBuilder

WriteLine("This is an ahead-of-time (AOT) compiled console app.");
WriteLine("Current culture: {0}", CultureInfo.CurrentCulture.DisplayName);
WriteLine("OS version : {0}", Environment.OSVersion);

Write("Press any key to exit.");
ReadKey(intercept: true); // do not output the key that was pressed

// AssemblyBuilder ab = AssemblyBuilder.DefineDynamicAssembly(
//    new AssemblyName("MyAssembly"), AssemblyBuilderAccess.Run);
