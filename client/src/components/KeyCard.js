import {React, useState} from 'react'
import ReactDOM from 'react-dom/client'

export default function KeyCard( {characterKey, character, changeCharacterKey} ){
    if (character == ' '){
        return null
    }
    return(
        <div>
            <input className = "KeyCard" value = {characterKey} onChange={changeCharacterKey} placeholder={character.toUpperCase()}></input>
        </div>
    )
}