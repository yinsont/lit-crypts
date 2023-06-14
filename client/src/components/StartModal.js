import React from 'react'
import { Link } from "react-router-dom";
import ex1 from "./Assets/puzzle_pic1.png"
import ex2 from "./Assets/puzzle_pic2.png"
import correct from "./Assets/puzzle_img1.png"
const MODAL_STYLES = {
    position: 'fixed',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    backgroundColor: '#FFF',
    padding: '50px',
    zIndex: 1000
}

const OVERLAY_STYLES = { //Makes background dark and unclickable
    position: 'fixed',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: 'rgba(0,0,0,.75)',
    zIndex: 1000,
}


export default function StartModal({closeModal}){
    return (
        <>
            <div style={OVERLAY_STYLES}>
                <div style = {MODAL_STYLES}>
                    <h1>How to Play</h1>
                    <p>Guess the cypher as quickly as possible!</p>
                        <li>The correct quote is coded using emojis</li>
                        <li>All instances of the correct letter will appear and turn green when inputted</li>
                        <p>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</p>
                        <br></br>
                    <h2>Examples</h2>
                        <img src={ex1}></img>
                        <p><b>P</b> is in the word and in the correct spot.</p>
                        <img src={ex2}></img>
                        <p><b>E</b> is in many correct spots.</p>
                        <img src={correct}></img>
                        <p>You solved the Lit🔥 Crypt🧩!</p>
                        <p>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</p>
                        <Link className="link" to='/signup'>Login or signup to view and compare your scores!</Link>
                    <button onClick = {closeModal}>Close</button>
                    
                </div> 
            </div>
        </>
    )
}