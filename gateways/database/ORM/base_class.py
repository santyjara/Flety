from typing import Any, Dict, Iterable, List, Union

from sqlalchemy import inspect
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def as_dict(
        self,
        *,
        only: Iterable[str] = set(),
        exclude: Iterable[str] = set(),
        follow: Union[List[str], Dict[str, dict]] = {},
    ) -> dict:
        """
        Gets a dictionary from an ORM object.

        Args:
            only:
                If this argument is specified, only the columns in the passed
                iterable will be included in the dictionary. This argument should
                not be specified at the same time as `exclude`.
            exclude:
                If this argument is specified, all the columns but the ones in the
                passed iterable will be included in the dictionary. This argument
                should not be specified at the same time as `only`.
            follow:
                Specifies the relationships that should be recursively turned into
                dictionaries. If it is a list, the `asdict` method will be applied to
                all relationships in it with the default arguments. If it is a
                dictionary, the relationships must be the keys and the values must be
                dictionaries specifying the arguments that will be passed to `asdict`
                when called on said relationships. Notably, further `follow` arguments
                can be specified to get a deeper nested dictionary.

        Returns:
            A dictionary with the required attributes and relationships as keys and
            populated with the appropriate values.

        Example:
            Input:
            ```
                statement = (
                    select(ExamInstanceORM)
                    .options(
                        joinedload(ExamInstanceORM.user),
                        joinedload(ExamInstanceORM.exam_design)
                        .joinedload(ExamDesignORM.exam_sections),
                    )
                    .filter(ExamInstanceORM.id == 2500)
                )
                result = await db.execute(statement)
                exam = result.unique().scalar_one()

                exam.asdict(
                    only={"user_id", "score"},
                    follow={
                        "user": {"exclude": {"id", "hashed_password"}},
                        "exam_design": {"follow": ["exam_sections"]},
                    },
                )
            ```

            Output:
            ```
                {
                    "score": None,
                    "user_id": 468,
                    "user": {"email": "email418@email.com", "name": None},
                    "exam_design": {
                        "id": 5,
                        "name": "Mock Test New",
                        "created_on": datetime(2021, 8, 3, 2, 1, 51, 483061),
                        "exam_sections": [
                            {"id": 6, "exam_design_id": 5, "skill_id": 54},
                            {"id": 7, "exam_design_id": 5, "skill_id": 105},
                        ],
                    },
                }
            ```

        """
        if only and exclude:
            raise ValueError("You can specify either `only` or `exclude`, but not both")

        if isinstance(follow, list):
            follow = dict.fromkeys(follow, {})

        info = inspect(self)

        # Determine the columns to include:

        columns = set(info.mapper.column_attrs.keys())

        if only:
            only = set(only)
            columns = only.intersection(columns)
            if only != columns:
                raise ValueError(
                    "The following attributes passed to `only` are not columns of the "
                    "ORM object: "
                    f"{', '.join(only - columns)}"
                )

        elif exclude:
            exclude = set(exclude)
            columns = columns - exclude

        result = {column: getattr(self, column) for column in columns}

        relationships = info.mapper.relationships.keys()

        for relationship in relationships:
            if relationship in follow:
                kwargs = follow[relationship]
                rel = getattr(self, relationship)
                if isinstance(rel, list):
                    result[relationship] = [row.asdict(**kwargs) for row in rel]
                else:
                    result[relationship] = rel.asdict(**kwargs)

        return result
