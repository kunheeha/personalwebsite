from personalwebsite import create_app_from_config

app = create_app_from_config()

if __name__ == "__main__":
    app.run(debug=True)
