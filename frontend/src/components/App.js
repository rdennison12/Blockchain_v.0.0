import React, {useState, useEffect} from "react";
import logo from '../assets/logo.png';
import {API_BASE_URL} from "../config";
import Blockchain from "./Blockchain";

function App() {
    const [walletInfo, setWalletInfo] = useState({});

    useEffect(() => {
        fetch(`${API_BASE_URL}/wallet/info`)
            .then(response => response.json())
            .then(json => setWalletInfo(json));
    }, []);

    const {address, balance} = walletInfo;

    return (
        <div className="App">
            <img src={logo} className="logo" alt="logo"/>
            <h3>Welcome to Pychain</h3>
            <br/>
            <div className="WalletInfo">
                <div>Wallet Address: {address}</div>
                <div>Wallet Balance: {balance}</div>
            </div>
            <br/>
            <Blockchain/>
        </div>
    );
}

export default App;
