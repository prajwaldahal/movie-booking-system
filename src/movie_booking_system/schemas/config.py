from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Business and safety limits. Override any of them in .env or as an environment variable,
    e.g. MAX_SEATS_PER_HOLD=50, with no code change."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    hold_minutes: int = 5  # how long a held seat waits for payment
    max_seats_per_hold: int = 30  # sanity cap on one hold request
    max_seats_per_audi: int = 2000  # sanity cap on one audi's whole layout


settings = Settings()
