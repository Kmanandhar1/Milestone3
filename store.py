import json
from azure.servicebus import ServiceBusClient, ServiceBusMessage

# Put your connection string here (from step 5)
CONNECTION_STRING = "Endpoint=sb://mystore-messages.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=FrZooWk3IdOcy5znJgARiLPM1FhiELCb0+ASbOrJDJs="

def check_stock_and_notify():
    # Pretend we're checking our store inventory
    products = [
        {"name": "apples", "current_stock": 3, "minimum_needed": 10},
        {"name": "bread", "current_stock": 1, "minimum_needed": 5}
    ]
    
    # Check each product
    for product in products:
        if product["current_stock"] < product["minimum_needed"]:
            print(f"⚠️  {product['name']} is low! Only {product['current_stock']} left!")
            
            # Create a message about low stock
            message_data = {
                "productId": product["name"],
                "currentStock": product["current_stock"],
                "requestedQuantity": product["minimum_needed"] * 2  # Order double
            }
            
            # Send message to queue
            send_message_to_queue(message_data)

def send_message_to_queue(message_data):
    try:
        # Connect to Azure message system
        with ServiceBusClient.from_connection_string(CONNECTION_STRING) as client:
            with client.get_queue_sender("low-stock") as sender:
                # Create and send message
                message = ServiceBusMessage(json.dumps(message_data))
                sender.send_messages(message)
                print(f"✅ Sent order request for {message_data['productId']}")
    except Exception as e:
        print(f"❌ Error sending message: {e}")

if __name__ == "__main__":
    print("🏪 Checking store inventory...")
    check_stock_and_notify()
    print("✅ Done checking inventory!")