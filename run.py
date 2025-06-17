from app import create_app
from waitress import serve

app = create_app()

if __name__ == "__main__":
    print("algo")
    #serve(app, host="localhost", port=5000)
    app.run(debug=True)