HttpClient client = new();

HttpResponseMessage response = await client.GetAsync("http://www.apple.com");

WriteLine("Apple's home page has {0:n0} bytes.", response.Content.Headers.ContentLength);