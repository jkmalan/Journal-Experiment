import sys

from app import create_app

app = create_app()


def print_help():
    print("-- Command Help --")
    print("  python app.py create")
    print("      Create all database tables")
    print("  python app.py drop")
    print("      Drop all database tables")
    print("  python app.py fill")
    print("      Populate all tables with test data")


def main():
    from app.core import db
    if len(sys.argv) > 1:
        if sys.argv[1] == 'create':
            db.create_all()
        elif sys.argv[1] == 'drop':
            db.drop_all()
        elif sys.argv[1] == 'fill':
            db.populate()
        else:
            print_help()
    else:
        app.run()


if __name__ == "__main__":
    with app.app_context():
        main()
