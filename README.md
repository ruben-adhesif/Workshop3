# E-commerce Platform with Synchronous Mirroring

## Overview
This section of the practical work enhances the reliability and data integrity of our e-commerce platform by implementing synchronous mirroring. This approach ensures real-time data availability across two storage systems, providing robust protection against data loss and enabling high availability.

## Implementation Details

### Synchronous Mirroring
We've modified the server implementation to write data simultaneously to two databases (`db.json` and `db_mirror.json`). This ensures every transaction made to the primary database is concurrently mirrored to the secondary database, maintaining a consistent state across both.

### Server Modification
The `server.js` file was adapted to include functions for reading from and writing to both the primary and mirrored databases. This guarantees data synchronization across both storage systems at all times, providing a fallback in case the primary database becomes inaccessible.

### Frontend Interactions
The frontend (`index.html`) allows users to interact with the e-commerce platform, enabling them to add products, create orders, and manage their shopping cart. The frontend communicates with the backend through API endpoints defined in `server.js`.

### Data Structure
The data is structured into products, orders, and carts, stored in `db.json` and `db_mirror.json`. Synchronous mirroring ensures that both databases are always up-to-date with the latest changes.

## Testing Synchronous Mirroring

- Start the e-commerce server by running `node server.js` in the terminal. This initiates the server on port 3002 and serves the frontend via `http://localhost:3002`.
- Interact with the e-commerce platform through the provided frontend interface. Add products, create orders, and add items to the cart.
- Verify that changes are reflected in both `db.json` and `db_mirror.json` to confirm synchronous mirroring is functioning correctly.

## Conclusion
Implementing synchronous mirroring in our e-commerce platform significantly enhances data reliability and system availability. By maintaining a real-time mirror of our database, we ensure our platform can withstand unforeseen data disruptions, providing a seamless experience for our users.
