using static System.Console;

// do not define a namespace so this class goes ain the default empty namespace
// just like th auto-generated partial Program class.

partial class Program
{
    static void WhatsMyNamespace()
    {
        WriteLine("Namespace of Program class: {0}", typeof(Program).Namespace ?? "null");
    }
}