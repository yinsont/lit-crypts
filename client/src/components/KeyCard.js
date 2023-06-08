import {React, useState} from 'react'
import ReactDOM from 'react-dom/client'

export default function KeyCard( {characterKey, character, changeCharacterKey} ){
    //console.log(characterKey)
    //console.log(characterKey)

    if (character == ' '){
        return 'space'
    }
    return(
        <div>
            <input className = "KeyCard" value = {characterKey} onChange={changeCharacterKey} placeholder={character.toUpperCase()}></input>
        </div>
    )
}