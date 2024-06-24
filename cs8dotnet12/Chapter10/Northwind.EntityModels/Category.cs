using System.ComponentModel.DataAnnotations.Schema; // to use [Column]
namespace Northwind.EntityModels;

public class Category
{
    // these properties map to columns in the database
    public int CategoryId { get; set; } // the primary key
    public string CategoryName { get; set; } = null!;
    [Column(TypeName = "ntext")]
    public string? Description { get; set; }

    // defines a navigation property for related rows
    public virtual ICollection<Product> Products { get; set; }
        // to enabel devs to add products to a Category, we must
        // initialize the navigation property to an empty collection.
        // this also avoids an exception if we get a member like Count
        = new HashSet<Product>();
}
