import React from 'react'
import { Link } from "react-router-dom";
import p1 from "./Assets/p1.png"
import p2 from "./Assets/p2.png"
import p3 from "./Assets/p3.png"
import p4 from "./Assets/p4.png"

const MODAL_STYLES = {
    position: 'fixed',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    backgroundColor: '#FFF',
    padding: '50px',
    zIndex: 1000,
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

const style_image = {
    width: '50vw'
}

export default function StartModal({closeModal}){
    return (
        <>
            <div style={OVERLAY_STYLES}>
                <div style = {MODAL_STYLES}>
                    <h1 id = 'ex'>How to Play</h1>
                    <p id ='ex'>Guess the cyphered quote as quickly as possible!</p>
                        <li id='ex'>The correct quote is scrambled using random letters.</li>
                        <li id='ex'>All instances of the correct letter will appear and turn green when inputted.</li>
                        <li id='ex'>Your score is calculated based on the time it takes you to solve the cyper.</li>
                        <p>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</p>
                        <br></br>
                    <h2 id='ex'>Examples</h2>
                        <img style = {style_image} src={p4}></img>
                        <p id = 'ex'>White tiles indicate you have not made any guesses yet.</p>
                        <img style = {style_image} src={p1}></img>
                        <p id = 'ex'><b>H</b> is the correct letter in many tiles.</p>
                        <img style = {style_image} src={p2}></img>
                        <p id = 'ex'><b>H</b> is the correct letter, but <b>I</b> is wrong in many tiles.</p>
                        <img style = {style_image} src={p3}></img>
                        <p id='ex'>You solved the Lit🔥 Crypt🧩!</p>
                        <p>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</p>
                        <Link className="link" to='/signup'>Login or signup to view and compare your scores!</Link>
                        <p>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</p>
                    <button class="glow-on-hover" onClick = {closeModal}>START GAME</button>
                    
                </div> 
            </div>
        </>
    )
}