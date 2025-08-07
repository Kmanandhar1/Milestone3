# Final Submission - Event-Driven Architecture Project

## 📌 Event Type Chosen

**Azure Service Bus Queue**

We chose Azure Service Bus Queue for its reliable FIFO delivery, decoupling, and robust message handling features, which are ideal for notifying suppliers about low inventory asynchronously.

---

## 🔁 Message Format and Flow

### Format (JSON)
```json
{
  "productId": "12345",
  "name": "Product A",
  "quantity": 2,
  "correlationId": "abc-123-xyz"
}

Flow
Backend service detects low stock.

It sends a message to Azure Service Bus Queue with a correlation ID.

Azure Function triggers from the queue.

The function calls the Supplier API, forwarding the correlation ID.

Logs from all services track this ID for observability.

🚀 Deployment & Testing Instructions
Prerequisites
Azure Subscription
Azure CLI
Python 3.12+
Node.js & Azure Functions Core Tools
Git or ZIP extractor

Steps
Deploy Azure Resources

Create a Service Bus namespace and queue.

Deploy the Azure Function to Azure.

Run Backend

cd backend
pip install -r requirements.txt
python main.py
Run Supplier API

cd supplier-api
pip install -r requirements.txt
python app.py
Start Function Locally (for testing)

cd inventory-function
func start
Send test request
The backend will automatically send to the queue and log the correlation ID.
