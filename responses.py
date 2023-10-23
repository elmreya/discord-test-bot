def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == '.hello':
        return 'Hi! How can I help you?'

    if p_message == '.help':
        return 'Use ".reminder" and then a message to set a reminder'

