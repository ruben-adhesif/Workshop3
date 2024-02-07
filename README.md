# E-commerce Redundancy Test

This README outlines the steps to simulate a server failure and test the redundancy setup for the e-commerce application.

## Setup

Ensure that you have three servers running:
- E-commerce app running on `localhost:3002`
- DNS server running on `localhost:4000`
- Hello World server running on `localhost:3001`

## Testing Steps

1. **Start the Servers**: Ensure all three servers are running.

2. **Check E-commerce Server**: Visit `http://localhost:3002` and verify that the e-commerce application is running.

3. **Check DNS Server Response**: Visit `http://localhost:4000/getServer` and verify that it returns the e-commerce server address (`localhost:3002`).

4. **Simulate E-commerce Server Failure**: Manually stop the e-commerce app server to simulate its failure.

5. **Toggle DNS Response**: Simulate the DNS server detecting the failure by visiting `http://localhost:4000/toggleEcommerceServer`. This toggles the internal flag to represent the e-commerce server being down.

6. **Check DNS Server Redirect**: Visit `http://localhost:4000/getServer` again. It should now return the "Hello World" server address (`localhost:3001`).

7. **Verify Redirect**: Finally, visit `http://localhost:3001` to confirm that the "Hello World" server is running and can serve requests in place of the e-commerce app.

## Notes

In a real-world scenario, the DNS server would automatically detect the health of the e-commerce server and switch over to the backup server. This manual toggle is only for simulation purposes.
