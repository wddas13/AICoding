from flask import current_app


def parse_pagination_args(args):
    default_page = current_app.config.get("PAGINATION_DEFAULT_PAGE", 1)
    default_size = current_app.config.get("PAGINATION_DEFAULT_SIZE", 10)
    max_size = current_app.config.get("PAGINATION_MAX_SIZE", 100)
    page_raw = args.get("page", default_page)
    size_raw = args.get("size", default_size)
    try:
        page = int(page_raw)
    except Exception:
        page = default_page
    try:
        size = int(size_raw)
    except Exception:
        size = default_size
    if page < 1:
        page = 1
    if size < 1:
        size = 1
    if size > max_size:
        size = max_size
    return page, size

