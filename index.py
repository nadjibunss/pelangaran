from app import app

# Vercel requires an entry point named 'handler'
def handler(event, context):
    return app(event, context)
