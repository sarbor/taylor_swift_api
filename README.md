# Taylor Swift API - FastAPI Implementation

This project is a FastAPI implementation of a Taylor Swift API, which provides access to Taylor Swift's albums, songs, and lyrics data.

Peak traffic of 170k requests a day

<img width="1499" alt="Screen Shot 2023-11-24 at 3 15 55 AM" src="https://github.com/sarbor/taylor_swift_api/assets/15257226/bb2723fb-5320-4242-8fd6-a8cb318e4b0b">

The Taylor Swift API allows you to access information about Taylor Swift's albums, songs, and lyrics. You can retrieve data such as album details, song info and lyrics for a specific song.

You can even request N verses of lyrics from the api to use as Lorem Ipsum.

This API is hosted on Cloudflare Workers and the data is stored inside PlanetScale

[User Friendly Documentation for this API](https://bump.sh/sarbor/doc/taylor-swift-api)

Projects using this API
+ [Taylor Ipsum Generator](https://taylor-ipsum-website.pages.dev/)

## Features

- RESTful API endpoints to retrieve albums, songs, and lyrics.
- Data served in JSON format.
- Simple and intuitive API design.

## Local Setup

To run this project locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/your-username/taylorSwiftAPIDevin.git
   cd taylorSwiftAPIDevin
   ```

2. Set up a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Start the FastAPI server:
   ```
   uvicorn main:app --reload
   ```

The API will be available at `http://127.0.0.1:8000`.

## Deployment to Heroku

To deploy this application to Heroku, you will need an existing Heroku account and the Heroku CLI installed.

1. Log in to Heroku:
   ```
   heroku login
   ```

2. Create a new Heroku app:
   ```
   heroku create your-app-name
   ```

3. Set up the Git remote for Heroku:
   ```
   heroku git:remote -a your-app-name
   ```

4. Push the code to Heroku:
   ```
   git push heroku main
   ```

5. Ensure at least one instance of the app is running:
   ```
   heroku ps:scale web=1
   ```

6. Open the app in your browser:
   ```
   heroku open
   ```

For more information on deploying to Heroku, visit the [Heroku Dev Center](https://devcenter.heroku.com/articles/getting-started-with-python).

## API Endpoints

The following endpoints are available:

- `GET /albums`: Retrieve all albums.
- `GET /albums/{albumID}`: Retrieve songs within an album.
- `GET /songs`: Retrieve all songs.
- `GET /songs/{songID}`: Retrieve song information for a specific song.
- `GET /lyrics/{songID}`: Retrieve lyrics for a given song.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).
