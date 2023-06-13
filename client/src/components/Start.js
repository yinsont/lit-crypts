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
        <div classsName = 'Start'>
            <h1>Welcome to Lit🔥 Crypts🧩</h1>
            <h3>Try to decipher the encrypted sentence using as little time as possible</h3>

            <button onClick = {handleClickPlay}>Play</button>
        </div>
    )
}