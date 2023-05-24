Sure, let's get you started with Express.js.

**Step 1: Install Node.js and npm**

First, you need to have Node.js and npm (Node Package Manager) installed on your machine. If they are not installed, you can download and install them from the [official Node.js website](https://nodejs.org/). The npm comes bundled with Node.js.

**Step 2: Create a New Node.js Application**

Navigate to the directory where you want to create your application and initialize a new Node.js application by running the following command:

```bash
npm init -y
```

This command will create a new `package.json` file in your directory. The `package.json` file contains metadata about your application, such as its name, version, and dependencies.

**Step 3: Install Express**

Next, install Express.js in your application by running the following command:

```bash
npm install express --save
```

The `--save` option adds Express as a dependency in your `package.json` file.

**Step 4: Create Your Express Application**

Now you're ready to create your Express application. Create a new file, usually named `app.js` or `server.js`, and write the following code:

```javascript
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello, World!');
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
```

In this script, we:

1. Require the `express` module.
2. Create an instance of an Express application.
3. Define a route handler for the path `/` that sends 'Hello, World!' as a response.
4. Start the server on port 3000.

**Step 5: Run Your Express Application**

Run your Express application with the following command:

```bash
node app.js
```

Or if your main file is named `server.js`:

```bash
node server.js
```

You should see the message `Server is running at http://localhost:3000` printed to the console. If you open your browser and navigate to `http://localhost:3000`, you should see the text 'Hello, World!'.

And that's it! You now have a running Express.js application. You can start adding more routes, middleware, etc., as needed for your application. Express.js has a powerful routing system, support for middleware, template engine support, and much more. For more detailed information, check out the [Express.js documentation](https://expressjs.com/).