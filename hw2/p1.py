def unique_geo_searcher(ids: dict[str, list[int]]) -> set[int]:
    """
    Return a set of unique geo tags from given dictionary of user ids.

    The dictionary values are lists of geo tags.
    """
    assert ids, 'Внимание, гео-метки пусты!'
    assert isinstance(ids, dict), 'Внимание, аргумент `ids` должен быть словарём!'

    unique_geo_tags: set[int] = set()
    for geo_tags in ids.values():
        unique_geo_tags |= set(geo_tags)

    return unique_geo_tags


def main():
    ids: dict[str, list[int]] = {
        'user1': [213, 213, 213, 15, 213],
        'user2': [54, 54, 119, 119, 119],
        'user3': [213, 98, 98, 35],
    }
    result: set[int] = unique_geo_searcher(ids)
    assert result == {98, 35, 54, 119, 15, 213}


if __name__ == '__main__':
    main()
