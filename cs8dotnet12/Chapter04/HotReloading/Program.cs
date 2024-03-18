// visual studio 2022: run the app, change the message, click Hot RelLoad.
// visual studio code: run the app using dotnet watch, change the message.

while (true)
{
    WriteLine("Hello, Hot Reload!");
    await Task.Delay(2000);
}