from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# This will store our orders (like a simple database)
orders = []

@app.route('/order', methods=['POST'])
def make_order():
    # Get the order details from whoever is calling us
    order_info = request.get_json()
    
    # Create a simple order
    new_order = {
        "order_id": len(orders) + 1,
        "product": order_info.get('productId', 'Unknown'),
        "quantity": order_info.get('requestedQuantity', 0),
        "status": "Ordered!"
    }
    
    # Save the order
    orders.append(new_order)
    
    print(f"New order received: {new_order}")
    
    # Send back confirmation
    return jsonify({"success": True, "order": new_order})

@app.route('/orders', methods=['GET'])
def see_all_orders():
    # Show all orders we've received
    return jsonify({"orders": orders})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)