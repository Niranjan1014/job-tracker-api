# Job Tracker API

## Environment Variables
- `PORT`: Port on which the application runs (default: 3000)
- `DB_URI`: MongoDB connection string.
- `JWT_SECRET`: Secret for signing JWT tokens.

## Complete API Endpoints
- **GET /jobs**: Retrieve a list of jobs.
- **POST /jobs**: Create a new job.
  - Required fields: title, description, company.
- **GET /jobs/:id**: Retrieve a job by ID.
- **PUT /jobs/:id**: Update a job by ID.
- **DELETE /jobs/:id**: Delete a job by ID.

## Database Setup
To set up the database, ensure MongoDB is running. Run the following command to seed the database:

```bash
node seed.js
```

## Example Requests
### Create Job Request (POST /jobs)
```json
{
  "title": "Software Engineer",
  "description": "Develop and maintain web applications.",
  "company": "Tech Company"
}
```

### Retrieve All Jobs (GET /jobs)
```http
GET /jobs HTTP/1.1
Host: api.jobtracker.com
```

## Testing
Run tests using Jest:

```bash
npm test
```

## License
This project is licensed under the MIT License.