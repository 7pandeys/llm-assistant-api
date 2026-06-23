import wikipedia


def search_wikipedia(
    query: str
):

    try:

        return wikipedia.summary(
            query,
            sentences=3
        )

    except Exception as e:

        return str(e)