def filterWishlistDeals(deals: list[dict], wishlist: list[str]) -> tuple[list[dict], list[str]]:
    """
    Returns:
    - matched_deals: deals that match something on the wishlist
    - not_on_sale: wishlist games that weren't found in the deals
    """
    matched_deals = []
    not_on_sale   = []

    for game in wishlist:
        match = next(
            (d for d in deals if game.lower() in d["name"].lower()),
            None
        )
        if match:
            matched_deals.append(match)
        else:
            not_on_sale.append(game)

    return matched_deals, not_on_sale