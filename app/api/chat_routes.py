from flask import Blueprint, jsonify, request, current_app, render_template
chat_bp = Blueprint('chat', __name__, url_prefix='/chat')


@chat_bp.route('/', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '').strip()
        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400

        current_app.logger.info(f"Received message: {user_message}")

        response = current_app.llm_service.generate_response(user_message)
        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@chat_bp.route('/chat-interface')
def chat_interface():
    return render_template('llm-chat.html')
