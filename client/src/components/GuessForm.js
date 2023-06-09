import {React, useState} from 'react'
import ReactDOM from 'react-dom/client'

export default function GuessForm({handleGuess}){


    return(
            <input onChange = {(e) => handleGuess(e.target.value)} placeholder='Take Your Guess!'></input>
    )
}