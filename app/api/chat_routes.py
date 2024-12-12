from flask import Blueprint, jsonify, request, current_app, render_template
chat_bp = Blueprint('chat', __name__, url_prefix='/chat')


@chat_bp.route('/input', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '').strip()
        chart_context = request.json.get('chartContext')

        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400

        response = current_app.llm_service.generate_response(
            user_message,
            chart_context=chart_context
        )
        return jsonify({"response": response})

    except Exception as e:
        current_app.logger.error(f"Error generating response: {str(e)}")
        return jsonify({"error": str(e)}), 500
