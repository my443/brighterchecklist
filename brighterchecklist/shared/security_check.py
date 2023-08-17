def check_security(owner, user):
    """Returns True if the owner and user are the same.
        Initially this is a simple comparison.  Later there may
        be a comparison on a table that shows multiple possibilities
        of what the 'owner' might be."""

    return owner == user