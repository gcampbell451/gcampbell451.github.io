using Microsoft.EntityFrameworkCore; // to use DbContext etc
using Microsoft.EntityFrameworkCore.Diagnostics; // to use RelationalEventId

namespace Northwind.EntityModels;

// this manages interactions with the Northwind database
public class NorthwindDb : DbContext
{
    // these two properties map to tables in the database
    public DbSet<Category> Categories { get; set; }
    public DbSet<Product> Products { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        string databaseFile = "Northwind.db";
        string path = Path.Combine(Environment.CurrentDirectory, databaseFile);

        string connectionString = $"Data Source={path}";
        WriteLine($"Connection: {connectionString}");
        optionsBuilder.UseSqlite(connectionString);

        optionsBuilder.LogTo(WriteLine, // this is the Console method
            new[] { RelationalEventId.CommandExecuting })
        #if DEBUG
            .EnableSensitiveDataLogging() // include SQL parameters
            .EnableDetailedErrors()
        #endif
        ;

        optionsBuilder.UseLazyLoadingProxies();
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        // example of using Fluent API instead of attributes
        // to limit the length of a category name to 15
        modelBuilder.Entity<Category>()
            .Property(category => category.CategoryName)
            .IsRequired() // NOT nULL
            .HasMaxLength(15);

        // SQLite-specific configurations
        if (Database.ProviderName?.Contains("Sqlite") ?? false)
        {
            // to fix the lack of decimal support in SQLite
            modelBuilder.Entity<Product>()
                .Property(product => product.Cost)
                .HasConversion<double>();
        }

        //  a global filter to remove discontinued products
        modelBuilder.Entity<Product>()
            .HasQueryFilter(p => !p.Discontinued);
    }
}
