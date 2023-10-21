## How to install
1. Clone this project
2. Install requirements.txt
3. To install requirements.txt run on the terminal pip install -r requirements.txt

## How to use this project
1. only GET request http://127.0.0.1:8000/api - Returns all Blogs
2. only POST request http://127.0.0.1:8000/api/new - Endpoint to add new Blog
3. only GET request http://127.0.0.1:8000/api/id - Show Blog with <id> (detail view)
4. only DELETE request http://127.0.0.1:8000/api/id/delete - Deletes a Blog with <id>
5. only PUT/PATCH request http://127.0.0.1:8000/api/id/update - Updates the data of the Blog with <id>
6. only GET request http://127.0.0.1:8000/api/username - Returns all Blogs by user <username>
7. only GET request http://127.0.0.1:8000/api/sort/field - Sorts Blogs by the given <filed>
