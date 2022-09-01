const {google} = require('googleapis');
const {GoogleAuth} = require('google-auth-library');

var express = require("express");
var router = express.Router();

writeData = async(username) => {
    const auth = new GoogleAuth({
        keyFile: './creds.json',
        scopes: 'https://www.googleapis.com/auth/spreadsheets'
    });
    const spreadsheetId = '1n58uvRsKE-SmwGBEZx-QyYlVy-W1mCPQP1U1VZHfsbg';
    const client = await auth.getClient();
    const googleSheets = google.sheets({version: "v4", auth: client});
    var metadata = await googleSheets.spreadsheets.values.update({
        auth, 
        spreadsheetId,
        range: "C2",
        valueInputOption: "USER_ENTERED",
        resource: {
          values: [["NULL"]],
        },
    });
    console.log("username: " + username + "dd");
    metadata = await googleSheets.spreadsheets.values.update({
        auth, 
        spreadsheetId,
        range: "C1",
        valueInputOption: "USER_ENTERED",
        resource: {
          values: [[username]],
        },
    });
    return username
}


router.post("/", async (req, res, next) => {
    console.log(req)
    var { name } = req.body.title;
    console.log(req.body.title)
    console.log(name)
    await writeData(req.body.title);
    res.send("fetching");
})

module.exports = router;