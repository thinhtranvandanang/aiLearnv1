from alembic import command
from alembic.config import Config
from app.core.config import settings

def run_migrations():
    """Run database migrations automatically."""
    try:
        # Use DATABASE_URL from settings
        alembic_cfg = Config("alembic.ini")
        alembic_cfg.set_main_option("sqlalchemy.url", settings.DATABASE_URL)
        
        # Run migrations
        command.upgrade(alembic_cfg, "head")
        print("✅ Database migrations completed successfully")
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        raise e
