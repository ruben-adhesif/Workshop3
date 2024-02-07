# Asynchronous Replication for E-Commerce Platform

This part of the project demonstrates the implementation of asynchronous replication in an e-commerce platform. Asynchronous replication is a method where data is replicated to a secondary storage system with some delay, providing redundancy and enhancing disaster recovery capabilities.

## Overview

In this implementation, changes made to the primary database are queued and then asynchronously replicated to a secondary database after a simulated delay. This setup mimics a real-world scenario where data replication occurs over a Wide Area Network (WAN) to a geographically remote site for disaster recovery purposes.

## Implementation Details

- **Primary Database (`db.json`):** The main database where all transactions and data modifications are first recorded.
- **Secondary Database (`db_async.json`):** The replica database where data from the primary database is replicated asynchronously.
- **Asynchronous Replication Logic:** Implemented in the `server.js` within the `Asynchronous-Replication` folder, this logic introduces a delay when replicating data to the secondary database, simulating the asynchronous nature of the replication process.

## Key Functions

- `readDB()`: Reads data from the primary database.
- `writeDB(data)`: Writes data to the primary database and initiates asynchronous replication to the secondary database.
- `asyncWriteDB(data)`: Simulates a delayed write operation to the secondary database, mimicking the behavior of data replication over a WAN.

## Testing the Implementation

To test asynchronous replication:
1. Perform various operations (create, update, delete) on the e-commerce platform.
2. Observe the immediate changes in the primary database (`db.json`).
3. After the simulated delay, verify that the changes are replicated to the secondary database (`db_async.json`).

## Error Handling

The implementation includes basic error handling for write operations. In a real-world scenario, more robust error handling, including retry mechanisms and alerts, would be necessary to ensure data consistency and integrity across the primary and secondary databases.

## Conclusion

This asynchronous replication setup provides a foundational understanding of how data redundancy and disaster recovery mechanisms can be implemented. It highlights the importance of asynchronous replication in ensuring data availability and integrity, especially in geographically dispersed systems.

