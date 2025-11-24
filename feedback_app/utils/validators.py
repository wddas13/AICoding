def validate_feedback_payload(data):
    content = (data.get("content") or "").strip()
    contact = (data.get("contact") or "").strip()
    errors = []
    if not content:
        errors.append("content is required")
    if len(contact) > 255:
        errors.append("contact too long")
    return errors

