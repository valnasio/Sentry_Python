import sentry_sdk
import os
from dotenv import load_dotenv
from sentry_sdk.integrations.otlp import OTLPIntegration


load_dotenv()

dsn = os.getenv("SENTRY_DSN")

sentry_sdk.init(
    dsn=dsn,
    # Add data like request headers and IP for users, if applicable;
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    integrations=[
        OTLPIntegration(),
    ],
)

division_by_zero = 11 / 0