from pydantic import BaseModel, HttpUrl


class DailyQuizesResponse(BaseModel):
    class DailyQuiz(BaseModel):
        screenshots: list[HttpUrl]

    daily_quizes: list[DailyQuiz]