import click
from sayhello import app, db
from sayhello.models import Message
from faker import Faker

#創建假資料
@app.cli.command()
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge(count):
    """Generate fake messages."""

    db.drop_all()
    db.create_all()

    fake = Faker()
    click.echo('Working...')

    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)

    db.session.commit()
    click.echo('Created %d fake messages.' % count)