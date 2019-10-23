from app import app


def main():
    print("This is the main method")


if __name__ == "__main__":
    with app.app_context():
        main()
