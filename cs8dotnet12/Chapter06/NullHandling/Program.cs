using Packt.Shared; // to use address

#region making a value type nullable

using Packt.Shared;
using System.Net.NetworkInformation;

int thisCannotBeNull = 4;
// thisCannotBeNull = null;
WriteLine(thisCannotBeNull);

int? thisCouldBeNull = null;

WriteLine(thisCouldBeNull);
WriteLine(thisCouldBeNull.GetValueOrDefault());

thisCouldBeNull = 7;

WriteLine(thisCouldBeNull);
WriteLine(thisCouldBeNull.GetValueOrDefault());

// the actual type of int? is Nullable<int>
Nullable<int> thisCouldAlsoBeNull = null;
thisCouldAlsoBeNull = 9;
WriteLine(thisCouldAlsoBeNull);

#endregion

#region Declaring non-nullable variables and parameters

Address address = new(city: "London")
{
    Building = null,
    Street = null!,
    Region = "UK"
};

WriteLine(address.Building?.Length);

if (address.Street is not null)
{
    WriteLine(address.Street.Length);

}

#endregion

#region Checking for null

string authorName = null;
int authorNameLength;

// the following throws a NullReferenceException
authorNameLength = authorName.Length;

// instead of throwing an exception, null is assigned
authorNameLength = (int)(authorName?.Length);

// result will be 25 if authorName?.Length is null
authorNameLength = authorName?.Length ?? 25;

#endregion