from app import app

# __name__ is a special variable used by the Python interpreter to understand if a file is the main program
if __name__ == "__main__":
    app.run(port=6001, debug=True)
