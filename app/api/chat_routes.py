from flask import Blueprint, jsonify, request, current_app, render_template

chat_bp = Blueprint('chat', __name__, url_prefix='/chat')


@chat_bp.route('/input', methods=['POST'])
def chat():
    try:
        current_app.logger.info(f"Request path: {request.path}")
        current_app.logger.info(f"Request full path: {request.full_path}")
        current_app.logger.info(f"Request URL: {request.url}")
        current_app.logger.info("Received request to chat")
        user_message = request.json.get('message', '').strip()
        if not user_message:
            current_app.logger.error("Message cannot be empty")
            return jsonify({"error": "Message cannot be empty"}), 400

        current_app.logger.info(f"Received message: {user_message}")
        
        response = current_app.llm_service.generate_response(user_message)
        return jsonify({"response": response})

    except Exception as e:
        current_app.logger.error(f"Error generating response: {str(e)}")
        return jsonify({"error": str(e)}), 500


@chat_bp.route('/chat-interface')
def chat_interface():
    current_app.logger.info("Rendering chat interface")
    return render_template('llm-chat.html')
