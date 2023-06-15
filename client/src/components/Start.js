import {React, useState} from 'react'
import Home from './Home'

export default function Start(){

    const [play, setPlay] = useState(false)

    function handleClickPlay(){
        setPlay(!play)
        console.log('toggle')
    }

    if (play){
        return(
            <Home/>
        )
    }

    return(
        <div id ='opener'>
            <h1 id='welcome'>Welcome to Lit🔥 Crypts🧩</h1>
            <h2 id='try'>Try to decipher the encrypted sentence using as little time as possible</h2>
            <button className='glow-on-hover' onClick = {handleClickPlay}>Close</button>
        </div>
    )
}