const {google} = require('googleapis');
const {GoogleAuth} = require('google-auth-library');

var express = require("express");
var router = express.Router();

readData = async() => {  
    const auth = new GoogleAuth({
        keyFile: './creds.json',
        scopes: 'https://www.googleapis.com/auth/spreadsheets'
    });
    const spreadsheetId = '1n58uvRsKE-SmwGBEZx-QyYlVy-W1mCPQP1U1VZHfsbg';
    const client = await auth.getClient();
    const googleSheets = google.sheets({version: "v4", auth: client});
    const metaData = await googleSheets.spreadsheets.values.get({
        auth, 
        spreadsheetId,
        range: "C2",
    });
    return(metaData.data.values);
}

router.get("/", async (req, res) => {
    res.send(await readData());
  });




module.exports = router;