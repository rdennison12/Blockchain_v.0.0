import React, {useState, useEffect} from "react";
import {API_BASE_URL} from "../config";
import Block from "./Block";

function Blockchain() {
    const [blockchain, setBlockchain] = useState([]);

    useEffect(() => {
        fetch(`${API_BASE_URL}/blockchain`)
            .then(response => response.json())
            .then(json => setBlockchain(json))
            .catch(err => console.log(err));
    }, []);

    return (
        <div className="Blockchain">
            <h3>Blockchain</h3>
            <div>
                {
                    blockchain.map(block =>  <Block key={block.hash} block={block}/>)
                }
            </div>
        </div>
    )
}

export default Blockchain;
