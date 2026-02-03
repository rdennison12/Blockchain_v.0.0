import React, {useState, useEffect} from "react";
import {Link} from "react-router-dom";
import logo from '../assets/logo.png';
import {API_BASE_URL} from "../config";
// import Blockchain from "./Blockchain";
// import ConductTransaction from "./ConductTransaction";

function App() {
    const [walletInfo, setWalletInfo] = useState({});

    useEffect(() => {
        fetch(`${API_BASE_URL}/wallet/info`)
            .then(response => response.json())
            .then(json => setWalletInfo(json))
            .catch(error => console.error('fetchWalletInfo error:', error));
    }, []);

    const {address, balance} = walletInfo;

    return (
        <div className="App">
            <img src={logo} className="logo" alt="logo"/>
            <h3>Welcome to Pychain</h3>
            <br/>
            <Link to="/blockchain">Blockchain</Link>
            <Link to="/conduct-transaction">Conduct Transaction</Link>
            <Link to="/transaction-pool">Transaction Pool</Link>
            <br/>
            <div className="WalletInfo">
                <div>Wallet Address: {address}</div>
                <div>Wallet Balance: {balance}</div>
            </div>
        </div>
    );
}

export default App;
