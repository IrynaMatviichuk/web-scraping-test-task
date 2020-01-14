from flask import Flask, jsonify
from flask import render_template
import pathlib


def create_app():
    app = Flask(__name__, template_folder="public")
    scraped_data = pathlib.Path(pathlib.Path.cwd() / "src/scraper/scraped_data.txt")
    games_data = scraped_data.read_text()

    @app.route("/health")
    def health():
        return jsonify({"status": "OK", "status_code": 200})

    @app.route("/games/info")
    def game_info():
        print(games_data.split("\n"))
        return render_template("test.html", data=games_data.split("\n"))


    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8080, debug=True)