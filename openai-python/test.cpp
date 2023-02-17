int main()
{
// Create a thread pool with 2 worker threads
pool tp(2);

c
Copy code
// Connect to a Redis Cluster with 3 nodes
cluster redisCluster({{"127.0.0.1", 6379}, {"127.0.0.1", 6380}, {"127.0.0.1", 6381}});

// Add a task to the thread pool to get stock details and store in Redis Cache
tp.schedule(boost::bind(getAndStoreStockDetails, "AAPL", boost::ref(redisCluster)));

// Wait for all tasks to complete
tp.wait();

// Retrieve the stock details from Redis Cache using the stock symbol as key
StockDetails stockDetails = retrieveStockDetails("AAPL", redisCluster);

cout << "Stock Name: " << stockDetails.name << endl;
cout << "Stock Price: " << stockDetails.price << endl;

return 0;
}
