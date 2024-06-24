﻿using Microsoft.EntityFrameworkCore; // to use ExecuteUpdate, ExecuteDelete
using Microsoft.EntityFrameworkCore.ChangeTracking;  // to use EntityEntry<T>
using Northwind.EntityModels;  // to use Northwind, Product

partial class Program
{
    private static void ListProducts(
        int[]? productIdsToHighlight = null)
    {
        using NorthwindDb db = new();

        if (db.Products is null || !db.Products.Any())
        {
            Fail("There are no products.");
            return;
        }

        WriteLine("| {0,-3} | {1,-35} | {2,8} | {3,5} | {4} |",
            "Id", "Product Name", "Cost", "Stock", "Disc.");

        foreach (Product p in db.Products)
        {
            ConsoleColor previousColor = ForegroundColor;

            if (productIdsToHighlight is not null && productIdsToHighlight.Contains(p.ProductId))
            {
                ForegroundColor = ConsoleColor.Green;
            }

            WriteLine("| {0:000} | {1,-35} | {2,8:$#,##0.00} | {3,5} | {4} |",
                p.ProductId, p.ProductName, p.Cost, p.Stock, p.Discontinued);

            ForegroundColor = previousColor;
        }
    }

    private static (int affected, int productId) AddProduct(
        int categoryId, string productName, decimal? price, short stock)
    {
        using NorthwindDb db = new();

        if (db.Products is null) return (0, 0);

        Product p = new()
        {
            CategoryId = categoryId,
            ProductName = productName,
            Cost = price,
            Stock = stock
        };

        // set product as added in change tracking
        EntityEntry<Product> entity = db.Products.Add(p);
        WriteLine($"State: {entity.State}, ProductId: {p.ProductId}");

        // save tracked change to database
        int affected = db.SaveChanges();
        WriteLine($"State {entity.State}, Product Id: {p.ProductId}");

        return (affected, p.ProductId);
    }

    private static (int affected, int productId) IncreaseProductPrice(
        string productNameStartsWith, decimal amount)
    {
        using NorthwindDb db = new();

        if (db.Products is null) return (0, 0);

        // get the first product whose name starts with the parameter value
        Product updateProduct = db.Products.First(
            p => p.ProductName.StartsWith(productNameStartsWith));

        updateProduct.Cost += amount;

        int affected = db.SaveChanges();
        return (affected, updateProduct.ProductId); 
    }

    private static int DeleteProducts(string productNameStartsWith)
    {
        using NorthwindDb db = new();

        IQueryable<Product>? products = db.Products?.Where(
            p => p.ProductName.StartsWith(productNameStartsWith));

        if (products is null || !products.Any())
        {
            WriteLine("No products found to delete.");
            return 0;
        }
        else
        {
            if (db.Products is null) return 0;
                    db.Products.RemoveRange(products);
        }

        int affected = db.SaveChanges();
        return affected;
    }

    private static (int affected, int[]? productIds) IncreasProductPricesBetter(
        string productNameStartsWith, decimal amount)
    {
        using NorthwindDb db = new();

        if (db.Products is null) return (0, null);

        // get products whose name starts with the parameter value
        IQueryable<Product>? products = db.Products.Where(
            p => p.ProductName.StartsWith(productNameStartsWith));

        int affected = products.ExecuteUpdate(s => s.SetProperty(
            p => p.Cost, // property selector Lambda expression
            p => p.Cost + amount)); // value to update to Lambda expression

        int[] productIds = products.Select(p => p.ProductId).ToArray();

        return (affected, productIds);
    }

    private static int DeleteProductsBetter(string productNameStartsWith)
    {
        using NorthwindDb db = new();

        int affected = 0;

        IQueryable<Product>? products = db.Products?.Where(
            p => p.ProductName.StartsWith(productNameStartsWith));

        if (products is null || !products.Any())
        {
            WriteLine("No products found to delete.");
            return 0;
        }
        else
        {
            affected = products.ExecuteDelete();
        }
        return affected;
    }
}