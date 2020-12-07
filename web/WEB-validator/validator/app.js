const express = require('express')
const express_static = require('express-static')
const fs = require('fs')
const path = require('path')

const app = express()
const port = 9000

app.use(express.json())
app.use(express.urlencoded({
    extended: true
}))

let info = []

const {
    body,
    validationResult
} = require('express-validator')

middlewares = [
    body('*').trim(),
    body('password').isLength({ min: 6 }),
]

app.use(middlewares)

readFile = function (filename) {
	var data = fs.readFileSync(filename)
	return data.toString()
}

app.post("/login", (req, res) => {
    console.log(req.body)
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
    }

    if (req.body.password == "D0g3_Yes!!!"){
        console.log(info.system_open)
        if (info.system_open == "yes"){
            const flag = readFile("/flag")
            return res.status(200).send(flag)
        }else{
            return res.status(400).send("The login is successful, but the system is under test and not open...")
        }
    }else{
        return res.status(400).send("Login Fail, Password Wrong!")
    }
})

app.get("/", (req, res) => {
    const login_html = readFile(path.join(__dirname, "login.html"))
    return res.status(200).send(login_html)
})

app.use(express_static("./"))

app.listen(port, () => {
    console.log(`server listening on ${port}`)
})

