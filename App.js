import logo from './logo.svg';
import './App.css';
import React, {useState, useEffect} from 'react';
import { scryRenderedComponentsWithType } from 'react-dom/test-utils';

const App = () => {

  const [userData, setUserData] = useState("")
  const [username, setUsername] = useState("NULL")
  const [user, setUser] = useState("")

  const onSubmit = async () => {
    console.log("test")
  }

  const callAPI = async () => {
    fetch('http://localhost:9000/testAPI')
      .then(res=>res.text())
      .then(res=> console.log(res))
    
  }

  const sleep = (milliseconds) => {
    return new Promise(resolve => setTimeout(resolve, milliseconds))
  }
  const callAPIPost = async () => {
    fetch('http://localhost:9000/posts', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title: username })
    }).then(res=>res.text())
      .then(res=> console.log(res))
    await sleep(1000)
    var response = 'NULL'
    while (response == 'NULL' || response == '[[\"NULL\"]]') {
      fetch('http://localhost:9000/testAPI')
        .then(res=>res.text())
        .then(res=> response = res)
      console.log('reponse ' + response)
    await sleep(5000)
    }
    console.log('reponse ' + response)
    response = String(response);
    //response = response.replaceAll('[', '');
    //response = response.replaceAll(']', '');
    response = response.substring(3, response.length - 3)
    response = response.replaceAll('\\', '');
    setUserData(response)
    setUser(response)
      
  }
  
  const changeUsername = async (event) => {
    setUsername(event.target.value)
  }

  /*
          <h1 className='Title-top'>TikTok Scraper</h1>
          <h1 className='Title'>TikTok Scraper</h1>
          <h1 className='Title-bottom'>TikTok Scraper</h1>
  */
  return (
    <div className="App">
      <header className="App-header">
        <div>
          <h1 className='Title'>TikTok Scraper</h1>
          <input className='Textfield' placeholder="Enter a tik tok username" onChange={changeUsername}></input>
          <br className='Break'></br>
          <div className='Break'></div>
          <button className='Button'onClick={callAPIPost}>Load User Data</button>
          <p className='Account-body' text={userData}>{user}</p>
          <p text={userData}></p>
      </div>
      </header>
    </div>
  );
}

export default App;
