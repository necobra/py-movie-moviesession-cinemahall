from django.db.models import QuerySet


from db.models import Movie, Actor, Genre


def get_movies(
        genres_ids: list[int] = None, actors_ids: list[int] = None
) -> QuerySet:
    movies = Movie.objects
    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)
    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)
    return movies.all()


def get_movie_by_id(movies_id: int) -> Movie:
    return Movie.objects.get(id=movies_id)


def create_movie(
        movie_title: str, movie_description: str,
        genres_ids: list[int] = None, actors_ids: list[int] = None
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.set(
            Genre.objects.filter(id__in=genres_ids)
        )
    if actors_ids:
        movie.actors.set(
            Actor.objects.filter(id__in=actors_ids)
        )
